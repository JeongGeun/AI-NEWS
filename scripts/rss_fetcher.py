"""RSS 피드 수집 모듈 (feedparser 기반)"""

import feedparser
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

logger = logging.getLogger(__name__)

# arXiv 키워드 필터
ARXIV_KEYWORDS = {
    "llm", "large language model", "agent", "reasoning", "multimodal",
    "rlhf", "fine-tuning", "fine tuning", "rag", "diffusion model",
    "vision-language", "vision language", "transformer", "foundation model",
    "instruction tuning", "alignment"
}

# GeekNews·Reddit 등 커뮤니티 소스용 AI 키워드 필터
COMMUNITY_KEYWORDS = {
    "ai", "llm", "gpt", "claude", "gemini", "llama", "mistral",
    "openai", "anthropic", "deepmind", "hugging face", "huggingface",
    "machine learning", "deep learning", "neural", "diffusion",
    "agent", "chatbot", "언어 모델", "인공지능", "머신러닝", "딥러닝",
}

# 개발자 도구 및 AI 엔지니어링 소스용 키워드 필터
DEVELOPER_KEYWORDS = {
    # AI 개발 도구
    "copilot", "cursor", "devin", "cline", "windsurf", "code generation",
    "coding assistant", "ai coding", "ide", "vscode", "vs code",
    # AI 엔지니어링
    "llm api", "langchain", "llamaindex", "llama index", "vector database",
    "vector db", "embeddings", "rag pipeline", "mlops", "llmops",
    "ai engineering", "prompt engineering", "fine-tuning api", "inference",
    "model deployment", "ai infrastructure", "ai platform",
    # 개발자 도구 일반
    "github copilot", "github models", "developer tools", "sdk", "open source model",
}

RSS_SOURCES = [
    # arXiv
    {
        "url": "https://rss.arxiv.org/rss/cs.AI",
        "category": "research",
        "source": "arXiv cs.AI",
        "max_items": 10,
        "arxiv_filter": True,
    },
    {
        "url": "https://rss.arxiv.org/rss/cs.LG",
        "category": "research",
        "source": "arXiv cs.LG",
        "max_items": 10,
        "arxiv_filter": True,
    },
    {
        "url": "https://rss.arxiv.org/rss/cs.CL",
        "category": "research",
        "source": "arXiv cs.CL",
        "max_items": 10,
        "arxiv_filter": True,
    },
    # Industry blogs
    {
        "url": "https://huggingface.co/blog/feed.xml",
        "category": "industry",
        "source": "HuggingFace Blog",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://deepmind.google/blog/feed/basic/",
        "category": "industry",
        "source": "Google DeepMind Blog",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://blog.google/technology/ai/rss/",
        "category": "industry",
        "source": "Google AI Blog",
        "max_items": 5,
        "arxiv_filter": False,
    },
    # News
    {
        "url": "https://venturebeat.com/category/ai/feed/",
        "category": "news",
        "source": "VentureBeat AI",
        "max_items": 8,
        "arxiv_filter": False,
    },
    {
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "category": "news",
        "source": "TechCrunch AI",
        "max_items": 8,
        "arxiv_filter": False,
    },
    {
        "url": "https://www.technologyreview.com/feed/",
        "category": "news",
        "source": "MIT Technology Review",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "category": "news",
        "source": "The Verge AI",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://thegradient.pub/rss/",
        "category": "research",
        "source": "The Gradient",
        "max_items": 3,
        "arxiv_filter": False,
    },
    # Community & Curation
    {
        "url": "https://news.hada.io/rss",
        "category": "community",
        "source": "GeekNews",
        "max_items": 10,
        "arxiv_filter": False,
        "keyword_filter": True,
    },
    {
        "url": "https://hnrss.org/newest?q=LLM+AI+machine+learning+GPT&points=10",
        "category": "community",
        "source": "Hacker News",
        "max_items": 8,
        "arxiv_filter": False,
    },
    {
        "url": "https://www.reddit.com/r/MachineLearning/.rss",
        "category": "community",
        "source": "Reddit r/MachineLearning",
        "max_items": 5,
        "arxiv_filter": False,
        "keyword_filter": True,
    },
    {
        "url": "https://www.reddit.com/r/LocalLLaMA/.rss",
        "category": "community",
        "source": "Reddit r/LocalLLaMA",
        "max_items": 5,
        "arxiv_filter": False,
    },
    # Developer tools & AI engineering
    {
        "url": "https://github.blog/category/ai/feed/",
        "category": "developer",
        "source": "GitHub Blog (AI)",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://stackoverflow.blog/feed/",
        "category": "developer",
        "source": "Stack Overflow Blog",
        "max_items": 5,
        "arxiv_filter": False,
        "developer_filter": True,
    },
    {
        "url": "https://simonwillison.net/atom/everything/",
        "category": "developer",
        "source": "Simon Willison's Blog",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://blog.langchain.dev/rss/",
        "category": "developer",
        "source": "LangChain Blog",
        "max_items": 5,
        "arxiv_filter": False,
    },
    {
        "url": "https://dev.to/feed/",
        "category": "developer",
        "source": "Dev.to",
        "max_items": 5,
        "arxiv_filter": False,
        "developer_filter": True,
    },
    # Newsletters (Substack)
    {
        "url": "https://importai.substack.com/feed",
        "category": "newsletter",
        "source": "Import AI",
        "max_items": 3,
        "arxiv_filter": False,
    },
    {
        "url": "https://www.deeplearning.ai/the-batch/rss.xml",
        "category": "newsletter",
        "source": "The Batch (deeplearning.ai)",
        "max_items": 3,
        "arxiv_filter": False,
    },
]

LOOKBACK_HOURS = 48


def _matches_arxiv_filter(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(kw in text for kw in ARXIV_KEYWORDS)


def _matches_community_filter(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(kw in text for kw in COMMUNITY_KEYWORDS)


def _matches_developer_filter(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(kw in text for kw in DEVELOPER_KEYWORDS)


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


def fetch_all() -> list[dict]:
    """모든 RSS 소스에서 기사 수집, 48시간 내 항목만 반환"""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
    articles = []

    for source_cfg in RSS_SOURCES:
        url = source_cfg["url"]
        logger.info(f"Fetching RSS: {source_cfg['source']} ({url})")
        try:
            feed = feedparser.parse(url)
            if feed.bozo and not feed.entries:
                logger.warning(f"  Failed to parse {url}: {feed.bozo_exception}")
                continue

            count = 0
            for entry in feed.entries:
                if count >= source_cfg["max_items"]:
                    break

                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                summary = entry.get("summary", "") or entry.get("description", "")

                if not title or not link:
                    continue

                # arXiv 키워드 필터
                if source_cfg["arxiv_filter"] and not _matches_arxiv_filter(title, summary):
                    continue

                # 커뮤니티 소스 키워드 필터 (GeekNews, Reddit 등)
                if source_cfg.get("keyword_filter") and not _matches_community_filter(title, summary):
                    continue

                # 개발자 소스 키워드 필터 (Stack Overflow, Dev.to 등)
                if source_cfg.get("developer_filter") and not _matches_developer_filter(title, summary):
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
                    "category": source_cfg["category"],
                    "published": published.isoformat() if published else "",
                })
                count += 1

            logger.info(f"  Collected {count} articles from {source_cfg['source']}")

        except Exception as e:
            logger.error(f"  Error fetching {url}: {e}")
            continue

    logger.info(f"Total RSS articles collected: {len(articles)}")
    return articles
