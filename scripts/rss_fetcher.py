"""RSS 피드 수집 모듈 (feedparser 기반) — config/topics.yml 기반 토픽별 수집"""

import feedparser
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

logger = logging.getLogger(__name__)

LOOKBACK_HOURS = 48

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

# 개발자 소스용 AI 엔지니어링 키워드 필터 (Stack Overflow, Dev.to 등)
_DEVELOPER_KEYWORDS = {
    "copilot", "cursor", "devin", "cline", "windsurf", "code generation",
    "coding assistant", "ai coding", "vscode", "vs code",
    "llm api", "langchain", "llamaindex", "llama index", "vector database",
    "vector db", "embeddings", "rag pipeline", "mlops", "llmops",
    "ai engineering", "prompt engineering", "fine-tuning api", "inference",
    "model deployment", "ai infrastructure", "ai platform",
    "github copilot", "github models", "developer tools", "sdk", "open source model",
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


def fetch_topic(topic: dict, lookback_hours: int = LOOKBACK_HOURS) -> list[dict]:
    """topics.yml의 단일 토픽 설정으로 RSS 기사 수집.

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
        url = source_cfg["url"]
        logger.info(f"[{topic_slug}] Fetching RSS: {source_cfg['source']} ({url})")
        try:
            feed = feedparser.parse(url)
            if feed.bozo and not feed.entries:
                logger.warning(f"  Failed to parse {url}: {feed.bozo_exception}")
                continue

            keyword_filter = source_cfg.get("keyword_filter")
            filter_fn = _FILTER_FUNCS.get(keyword_filter) if keyword_filter else None

            count = 0
            for entry in feed.entries:
                if count >= source_cfg.get("max_items", 10):
                    break

                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                summary = entry.get("summary", "") or entry.get("description", "")

                if not title or not link:
                    continue

                # 키워드 사전 필터 (설정된 경우)
                if filter_fn and not filter_fn(title, summary):
                    continue

                # 48시간 lookback 필터
                published = _parse_published(entry)
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
                count += 1

            logger.info(f"  Collected {count} articles from {source_cfg['source']}")

        except Exception as e:
            logger.error(f"  Error fetching {url}: {e}")
            continue

    logger.info(f"[{topic_slug}] Total RSS articles collected: {len(articles)}")
    return articles
