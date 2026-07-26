"""RSS 피드 수집 모듈 (feedparser 기반) — config/topics.yml 기반 토픽별 수집"""

import feedparser
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

from html_scraper import SCRAPERS

logger = logging.getLogger(__name__)

LOOKBACK_HOURS = 48

# 일부 사이트(Reddit 등)가 feedparser 기본 User-Agent를 차단하므로 브라우저로 위장
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# arXiv 키워드 필터 (AI 관련 논문 선별)
_ARXIV_KEYWORDS = {
    "llm", "large language model", "agent", "reasoning", "multimodal",
    "rlhf", "fine-tuning", "fine tuning", "rag", "diffusion model",
    "vision-language", "vision language", "transformer", "foundation model",
    "instruction tuning", "alignment"
}

# 커뮤니티 소스용 AI 키워드 필터 (GeekNews, Reddit 등)
_COMMUNITY_KEYWORDS = {
    "ai", "llm", "gpt", "claude", "gemini", "llama", "mistral",
    "openai", "anthropic", "deepmind", "hugging face", "huggingface",
    "machine learning", "deep learning", "neural", "diffusion",
    "agent", "chatbot", "언어 모델", "인공지능", "머신러닝", "딥러닝",
}

# 개발자 소스용 AI 엔지니어링 키워드 필터 (Stack Overflow, Dev.to, GeekNews 등)
_DEVELOPER_KEYWORDS = {
    # 영어 — AI 코딩 도구
    "copilot", "cursor", "devin", "cline", "windsurf", "code generation",
    "coding assistant", "ai coding", "vscode", "vs code",
    "llm api", "langchain", "llamaindex", "llama index", "vector database",
    "vector db", "embeddings", "rag pipeline", "mlops", "llmops",
    "ai engineering", "prompt engineering", "fine-tuning api", "inference",
    "model deployment", "ai infrastructure", "ai platform",
    "github copilot", "github models", "developer tools", "sdk", "open source model",
    "mcp", "model context protocol", "vibe coding", "agentic", "ai agent",
    # 한국어 — GeekNews 한국어 기사 필터용
    "코파일럿", "코딩 어시스턴트", "ai 코딩", "개발 도구", "llm api",
    "벡터 데이터베이스", "임베딩", "파인튜닝", "모델 배포", "ai 에이전트",
    "오픈소스 모델", "프롬프트 엔지니어링", "랭체인", "ai 개발",
    "바이브 코딩", "모델 컨텍스트 프로토콜", "추론", "ai 인프라",
}

# 스킨케어 키워드 필터 (beauty 토픽, 영어/한국어/일본어)
_SKINCARE_KEYWORDS = {
    # English — product types
    "skincare", "skin care", "skin-care", "moisturizer", "moisturiser",
    "serum", "toner", "essence", "cleanser", "exfoliant", "exfoliator",
    "sunscreen", "spf", "retinol", "vitamin c", "niacinamide", "hyaluronic acid",
    "peptide", "aha", "bha", "pha", "ceramide", "collagen", "antioxidant",
    # English — concerns & outcomes
    "anti-aging", "anti-wrinkle", "anti aging", "hydration", "moisturizing",
    "acne", "pore", "brightening", "dark spot", "hyperpigmentation",
    "sensitive skin", "oily skin", "dry skin", "skin barrier",
    # English — brand / category context
    "k-beauty skincare", "korean skincare", "sheet mask", "face mask",
    "eye cream", "face cream", "face oil", "mist", "sleeping mask",
    # 한국어
    "스킨케어", "피부", "세럼", "토너", "에센스", "클렌저",
    "선크림", "자외선차단", "레티놀", "나이아신아마이드", "히알루론산",
    "수분크림", "보습", "미백", "주름", "트러블", "모공", "피부장벽",
    "시트마스크", "마스크팩",
    # 日本語
    "スキンケア", "化粧水", "美容液", "乳液", "クレンジング",
    "日焼け止め", "保湿", "美白", "シートマスク", "レチノール",
    "ヒアルロン酸", "ナイアシンアミド", "セラミド", "毛穴",
}

_FILTER_FUNCS = {
    "arxiv": lambda title, summary: any(
        kw in (title + " " + summary).lower() for kw in _ARXIV_KEYWORDS
    ),
    "community": lambda title, summary: any(
        kw in (title + " " + summary).lower() for kw in _COMMUNITY_KEYWORDS
    ),
    "developer": lambda title, summary: any(
        kw in (title + " " + summary).lower() for kw in _DEVELOPER_KEYWORDS
    ),
    "skincare": lambda title, summary: any(
        kw in (title + " " + summary).lower() for kw in _SKINCARE_KEYWORDS
    ),
}


def _parse_published(entry) -> Optional[datetime]:
    """feedparser entry에서 published datetime 추출"""
    for attr in ("published_parsed", "updated_parsed"):
        val = getattr(entry, attr, None)
        if val:
            try:
                return datetime(*val[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return None


def _select_articles(
    raw_entries: list[tuple], source_cfg: dict, cutoff: datetime, topic_slug: str
) -> list[dict]:
    """(title, link, summary, published) 튜플 목록에 키워드/lookback/max_items 필터 적용"""
    keyword_filter = source_cfg.get("keyword_filter")
    filter_fn = _FILTER_FUNCS.get(keyword_filter) if keyword_filter else None
    max_items = source_cfg.get("max_items", 10)

    articles = []
    for title, link, summary, published in raw_entries:
        if len(articles) >= max_items:
            break

        title = (title or "").strip()
        link = (link or "").strip()
        if not title or not link:
            continue

        if filter_fn and not filter_fn(title, summary):
            continue

        if published and published < cutoff:
            continue

        articles.append({
            "title": title,
            "url": link,
            "summary": summary[:500] if summary else "",
            "source": source_cfg["source"],
            "sub_category": source_cfg.get("sub_category", "news"),
            "topic": topic_slug,
            "published": published.isoformat() if published else "",
        })

    return articles


def fetch_topic(topic: dict, lookback_hours: int = LOOKBACK_HOURS) -> list[dict]:
    """topics.yml의 단일 토픽 설정으로 기사 수집 (RSS 피드 + HTML 직접 파싱).

    Args:
        topic: topics.yml의 토픽 dict (slug, rss_sources 등 포함)
        lookback_hours: 이 시간 이내 기사만 수집

    Returns:
        기사 dict 목록 (title, url, summary, source, sub_category, topic, published)
    """
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    articles = []
    topic_slug = topic["slug"]

    for source_cfg in topic.get("rss_sources", []):
        scraper_name = source_cfg.get("scraper")
        source_name = source_cfg["source"]

        try:
            if scraper_name:
                logger.info(f"[{topic_slug}] Scraping HTML: {source_name} ({scraper_name})")
                raw_entries = SCRAPERS[scraper_name]()
            else:
                url = source_cfg["url"]
                logger.info(f"[{topic_slug}] Fetching RSS: {source_name} ({url})")
                feed = feedparser.parse(url, agent=_BROWSER_UA)
                if feed.bozo and not feed.entries:
                    logger.warning(f"  Failed to parse {url}: {feed.bozo_exception}")
                    continue
                raw_entries = [
                    (
                        entry.get("title", ""),
                        entry.get("link", ""),
                        entry.get("summary", "") or entry.get("description", ""),
                        _parse_published(entry),
                    )
                    for entry in feed.entries
                ]

            new_articles = _select_articles(raw_entries, source_cfg, cutoff, topic_slug)
            articles.extend(new_articles)
            logger.info(f"  Collected {len(new_articles)} articles from {source_name}")

        except Exception as e:
            logger.error(f"  Error fetching {source_name}: {e}")
            continue

    logger.info(f"[{topic_slug}] Total RSS articles collected: {len(articles)}")
    return articles
