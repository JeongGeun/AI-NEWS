"""본문 전문 추출 모듈 (newspaper3k)

스크래핑이 아닌 RSS에서 수집된 기사의 전문을 추출하는 역할만 담당.
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from newspaper import Article
    NEWSPAPER_AVAILABLE = True
except ImportError:
    NEWSPAPER_AVAILABLE = False
    logger.warning("newspaper3k not available; full text enrichment disabled")


def enrich_full_text(article: dict) -> dict:
    """RSS 기사의 URL에서 본문 전문을 추출해 article dict를 보강"""
    if not NEWSPAPER_AVAILABLE:
        return article

    url = article.get("url", "")
    if not url:
        return article

    try:
        news_article = Article(url, language="en")
        news_article.download()
        news_article.parse()

        full_text = news_article.text
        if full_text and len(full_text) > len(article.get("summary", "")):
            # 최대 2000자 제한 (토큰 비용 절감)
            article["full_text"] = full_text[:2000]
        else:
            article["full_text"] = article.get("summary", "")

    except Exception as e:
        logger.debug(f"Failed to extract full text from {url}: {e}")
        article["full_text"] = article.get("summary", "")

    return article


def enrich_articles(articles: list[dict], max_workers: int = 5) -> list[dict]:
    """병렬로 기사 전문 추출"""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    if not NEWSPAPER_AVAILABLE:
        for a in articles:
            a["full_text"] = a.get("summary", "")
        return articles

    enriched = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(enrich_full_text, a): a for a in articles}
        for future in as_completed(futures):
            try:
                enriched.append(future.result())
            except Exception as e:
                original = futures[future]
                logger.error(f"Enrich failed for {original.get('url', '')}: {e}")
                original["full_text"] = original.get("summary", "")
                enriched.append(original)

    return enriched
