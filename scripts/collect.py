"""메인 오케스트레이터: 토픽별 RSS 수집 → 중복 제거 → 전문 추출 → 요약+분류 → 포스트 생성"""

import logging
import os
import sys
from pathlib import Path

import anthropic
import yaml
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))

import rss_fetcher
import web_scraper
import deduplication
import claude_summarizer
import post_generator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("collect")

CONFIG_PATH = Path(__file__).parent.parent / "config" / "topics.yml"


def load_topics_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_topic_pipeline(
    topic: dict,
    client: anthropic.Anthropic,
    all_topics: list[dict],
) -> None:
    """단일 토픽에 대한 전체 파이프라인 실행"""
    slug = topic["slug"]
    logger.info(f"=== Topic: {topic['name']} ({slug}) ===")

    # 1. RSS 수집
    logger.info(f"[{slug}] Step 1: RSS Fetch")
    articles = rss_fetcher.fetch_topic(topic)
    if not articles:
        logger.warning(f"[{slug}] No articles collected from RSS feeds")
        return

    # 2. 중복 제거
    logger.info(f"[{slug}] Step 2: Deduplication")
    articles = deduplication.filter_new(articles, topic=slug)
    if not articles:
        logger.info(f"[{slug}] No new articles after deduplication")
        return

    # 3. 전문 추출 (newspaper3k)
    logger.info(f"[{slug}] Step 3: Full Text Enrichment")
    articles = web_scraper.enrich_articles(articles)

    # 4. Claude Batch API 요약 + 토픽 분류
    logger.info(f"[{slug}] Step 4: Summarization + Topic Classification")
    articles = claude_summarizer.summarize_articles(articles, client, all_topics)

    # 5. 토픽 관련성 필터 (topic_labels 기반)
    # - topic_labels 키 없음 → 파싱 실패, 포함 (안전 폴백)
    # - topic_labels = [] → Claude가 "무관" 판단, 제외
    # - topic_labels에 현재 slug 포함 → 포함
    relevant = [
        a for a in articles
        if "topic_labels" not in a or slug in a.get("topic_labels", [])
    ]
    logger.info(
        f"[{slug}] Topic filter: {len(articles)} → {len(relevant)} relevant articles"
    )

    if not relevant:
        logger.info(f"[{slug}] No relevant articles after topic filtering")
        return

    # 6. Jekyll 포스트 생성
    logger.info(f"[{slug}] Step 5: Post Generation")
    output_path = post_generator.generate_post(relevant, topic)
    logger.info(f"[{slug}] Done: {output_path}")


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    config = load_topics_config()
    all_topics = config["topics"]
    client = anthropic.Anthropic(api_key=api_key)

    for topic in all_topics:
        try:
            run_topic_pipeline(topic, client, all_topics)
        except Exception as e:
            logger.error(f"Pipeline failed for topic '{topic['slug']}': {e}", exc_info=True)
            continue  # 한 토픽 실패해도 다음 토픽 계속 진행


if __name__ == "__main__":
    main()
