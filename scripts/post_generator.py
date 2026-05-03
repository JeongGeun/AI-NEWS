"""Jekyll 마크다운 포스트 생성 모듈 — 토픽별 독립 포스트"""

import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

POSTS_DIR = Path(__file__).parent.parent / "_posts"

SIGNIFICANCE_LABELS = {
    "high": "높음",
    "medium": "보통",
    "low": "낮음",
}

DEFAULT_SUB_CATEGORY_LABELS = {
    "research": "연구 (Research)",
    "industry": "산업 동향 (Industry)",
    "news": "뉴스 (News)",
    "developer": "개발자 (Developer)",
    "tutorial": "튜토리얼 & 아티클",
    "community": "커뮤니티 (Community)",
    "newsletter": "뉴스레터 (Newsletter)",
}


_YAML_SPECIAL_START = set('@`|>&*!,[]{}#%')


def _quote_yaml_tag(tag: str) -> str:
    """YAML에서 문자열로 안전하게 파싱되도록 필요한 경우 따옴표로 감쌈."""
    tag = str(tag)
    # 숫자만으로 이루어진 태그 또는 YAML 특수문자로 시작하는 태그는 따옴표 처리
    if tag.lstrip('-').isdigit() or (tag and tag[0] in _YAML_SPECIAL_START):
        return f'"{tag}"'
    return tag


def _collect_tags(articles: list[dict]) -> list[str]:
    tags: set[str] = set()
    for a in articles:
        for tag in a.get("tags", []):
            if tag:
                tags.add(tag)
    return sorted(tags)[:20]


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


def generate_post(
    articles: list[dict],
    topic: dict,
    date: Optional[datetime] = None,
) -> Path:
    """토픽별 Jekyll 마크다운 포스트 생성, 파일 경로 반환.

    Args:
        articles: 기사 dict 목록 (요약 결과 포함)
        topic: topics.yml의 토픽 dict
        date: 포스트 날짜 (None이면 현재 KST)
    """
    if date is None:
        date = datetime.now(timezone(timedelta(hours=9)))  # KST

    slug = topic["slug"]
    date_str = date.strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}-daily.md"
    output_path = POSTS_DIR / filename

    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    # sub_category별 분류 (topics.yml의 sub_category_labels 기준)
    topic_labels = topic.get("sub_category_labels", {})
    sub_cat_labels = {**DEFAULT_SUB_CATEGORY_LABELS, **topic_labels}
    # topic이 순서를 정의하면 그 순서 우선, 나머지 DEFAULT로 보완
    if topic_labels:
        known_cats = list(topic_labels.keys()) + [
            k for k in DEFAULT_SUB_CATEGORY_LABELS if k not in topic_labels
        ]
    else:
        known_cats = list(sub_cat_labels.keys())

    by_sub_category: dict[str, list[dict]] = {cat: [] for cat in known_cats}
    by_sub_category["_other"] = []

    for article in articles:
        sub_cat = article.get("sub_category", "news")
        if sub_cat in by_sub_category:
            by_sub_category[sub_cat].append(article)
        else:
            by_sub_category["_other"].append(article)

    all_tags = _collect_tags(articles)
    tags_yaml = "\n  - ".join([""] + [_quote_yaml_tag(t) for t in all_tags]) if all_tags else ""

    jekyll_category = topic.get("jekyll_category", slug)

    lines = [
        "---",
        "layout: post",
        f'title: "{date_str} {topic["name"]} 데일리 브리핑"',
        f"date: {date.strftime('%Y-%m-%d')} 00:07:00 +0900",
        f"categories: [{jekyll_category}]",
        f"tags:{tags_yaml}",
        "---",
        "",
        f"> 수집 시각: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | "
        f"총 {len(articles)}건",
        "",
    ]

    # sub_category 섹션 순서대로 렌더링
    for cat_key in known_cats:
        cat_articles = by_sub_category.get(cat_key, [])
        if not cat_articles:
            continue
        label = sub_cat_labels.get(cat_key, cat_key)
        lines.append(f"## {label}")
        lines.append("")
        for idx, article in enumerate(cat_articles, 1):
            lines.append(_article_block(article, idx))

    # 분류 안 된 기사들
    other_articles = by_sub_category.get("_other", [])
    if other_articles:
        lines.append("## 기타")
        lines.append("")
        for idx, article in enumerate(other_articles, 1):
            lines.append(_article_block(article, idx))

    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    logger.info(f"Post generated: {output_path}")
    return output_path
