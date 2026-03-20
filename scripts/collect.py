"""메인 오케스트레이터: RSS 수집 → 중복 제거 → 전문 추출 → 요약 → 포스트 생성"""

import logging
import os
import sys

import anthropic
from dotenv import load_dotenv

load_dotenv()

# 스크립트 디렉토리 기준 임포트
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


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # 1. RSS 수집
    logger.info("=== Step 1: RSS Fetch ===")
    articles = rss_fetcher.fetch_all()
    if not articles:
        logger.warning("No articles collected from RSS feeds")
        sys.exit(0)

    # 2. 중복 제거
    logger.info("=== Step 2: Deduplication ===")
    articles = deduplication.filter_new(articles)
    if not articles:
        logger.info("No new articles after deduplication")
        sys.exit(0)

    # 3. 전문 추출 (newspaper3k)
    logger.info("=== Step 3: Full Text Enrichment ===")
    articles = web_scraper.enrich_articles(articles)

    # 4. Claude Batch API 요약
    logger.info("=== Step 4: Summarization (Claude Haiku Batch API) ===")
    articles = claude_summarizer.summarize_articles(articles, client)

    # 5. Jekyll 포스트 생성
    logger.info("=== Step 5: Post Generation ===")
    output_path = post_generator.generate_post(articles)

    logger.info(f"=== Done: {output_path} ===")


if __name__ == "__main__":
    main()
