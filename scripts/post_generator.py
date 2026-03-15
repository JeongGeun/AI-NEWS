"""Jekyll 마크다운 포스트 생성 모듈"""

import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

POSTS_DIR = Path(__file__).parent.parent / "_posts"

CATEGORY_LABELS = {
    "research": "연구 (Research)",
    "industry": "산업 동향 (Industry)",
    "news": "뉴스 (News)",
    "community": "커뮤니티 (Community)",
    "newsletter": "뉴스레터 (Newsletter)",
}

SIGNIFICANCE_LABELS = {
    "high": "높음",
    "medium": "보통",
    "low": "낮음",
}


def _collect_tags(articles: list[dict]) -> list[str]:
    tags: set[str] = set()
    for a in articles:
        for tag in a.get("tags", []):
            if tag:
                tags.add(tag)
    return sorted(tags)[:20]  # 최대 20개


def _article_block(article: dict, idx: int) -> str:
    title = article.get("korean_title") or article.get("title", "제목 없음")
    url = article.get("url", "#")
    source = article.get("source", "")
    significance = SIGNIFICANCE_LABELS.get(article.get("significance", ""), "")
    korean_summary = article.get("korean_summary", "")
    english_summary = article.get("english_summary", "")
    key_entities = article.get("key_entities", [])

    lines = [f"### {idx}. [{title}]({url})"]
    meta_parts = []
    if source:
        meta_parts.append(f"**출처**: {source}")
    if significance:
        meta_parts.append(f"**중요도**: {significance}")
    if meta_parts:
        lines.append(" · ".join(meta_parts))
    lines.append("")
    if korean_summary:
        lines.append(f"**한국어 요약**: {korean_summary}")
        lines.append("")
    if english_summary:
        lines.append(f"**English Summary**: {english_summary}")
        lines.append("")
    if key_entities:
        lines.append(f"**핵심 키워드**: {', '.join(key_entities)}")
        lines.append("")
    return "\n".join(lines)


def generate_post(articles: list[dict], date: Optional[datetime] = None) -> Path:
    """기사 목록으로 Jekyll 마크다운 포스트 생성, 파일 경로 반환"""
    if date is None:
        date = datetime.now(timezone(timedelta(hours=9)))  # KST

    date_str = date.strftime("%Y-%m-%d")
    filename = f"{date_str}-ai-news-daily.md"
    output_path = POSTS_DIR / filename

    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    # 카테고리별 분류
    by_category: dict[str, list[dict]] = {
        "research": [], "industry": [], "news": [], "community": [], "newsletter": []
    }
    for article in articles:
        cat = article.get("category", "news")
        if cat not in by_category:
            cat = "news"
        by_category[cat].append(article)

    all_tags = _collect_tags(articles)
    tags_yaml = "\n  - ".join([""] + all_tags) if all_tags else ""

    # Front matter
    lines = [
        "---",
        "layout: post",
        f'title: "{date_str} AI 뉴스 데일리 브리핑"',
        f"date: {date.strftime('%Y-%m-%d')} 09:00:00 +0900",
        "categories: [daily-news]",
        f"tags:{tags_yaml}",
        "---",
        "",
        f"> 수집 시각: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | "
        f"총 {len(articles)}건",
        "",
    ]

    # 카테고리 섹션
    for cat_key in ["research", "industry", "news", "community", "newsletter"]:
        cat_articles = by_category[cat_key]
        if not cat_articles:
            continue
        label = CATEGORY_LABELS[cat_key]
        lines.append(f"## {label}")
        lines.append("")
        for idx, article in enumerate(cat_articles, 1):
            lines.append(_article_block(article, idx))

    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    logger.info(f"Post generated: {output_path}")
    return output_path
