"""RSS 피드가 없거나 (403 등으로) 차단된 소스를 위한 HTML 직접 파싱 모듈.

각 함수는 (title, link, summary, published) 튜플 목록을 반환하며,
rss_fetcher.fetch_topic()에서 feedparser 엔트리와 동일하게 처리된다.
"""

import logging
import re
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
_HEADERS = {"User-Agent": _BROWSER_UA}
_TIMEOUT = 10


def scrape_geeknews() -> list[tuple]:
    """GeekNews 홈페이지 직접 파싱 (RSS 엔드포인트 /rss 는 WAF가 403으로 차단함)"""
    try:
        resp = requests.get("https://news.hada.io/", headers=_HEADERS, timeout=_TIMEOUT)
        resp.raise_for_status()
    except Exception as e:
        logger.error(f"  Error scraping GeekNews: {e}")
        return []

    soup = BeautifulSoup(resp.text, "lxml")
    entries = []
    for row in soup.select("div.topic_row"):
        title_tag = row.select_one("div.topictitle a h2")
        link_tag = row.select_one("div.topictitle a")
        desc_tag = row.select_one("div.topicdesc a")
        time_tag = row.select_one("time")
        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag.get("href", "")
        summary = desc_tag.get_text(strip=True) if desc_tag else ""
        published = None
        if time_tag and time_tag.get("datetime"):
            try:
                published = datetime.fromisoformat(time_tag["datetime"]).astimezone(timezone.utc)
            except ValueError:
                pass

        entries.append((title, link, summary, published))

    return entries


def scrape_langchain_blog() -> list[tuple]:
    """LangChain 블로그 RSS(blog.langchain.dev/rss/)가 죽어 목록 페이지를 직접 파싱"""
    try:
        resp = requests.get("https://www.langchain.com/blog", headers=_HEADERS, timeout=_TIMEOUT)
        resp.raise_for_status()
    except Exception as e:
        logger.error(f"  Error scraping LangChain Blog: {e}")
        return []

    soup = BeautifulSoup(resp.text, "lxml")
    entries = []
    seen_links = set()
    for item in soup.select("div.blog-item"):
        title_tag = item.select_one("h2")
        link_tag = item.select_one("a.blog-link-absolute")
        date_tag = item.select_one(".date-color")
        if not title_tag or not link_tag:
            continue

        href = link_tag.get("href", "")
        if not href or href in seen_links:
            continue
        seen_links.add(href)

        title = title_tag.get_text(strip=True)
        link = f"https://www.langchain.com{href}" if href.startswith("/") else href
        published = None
        if date_tag:
            try:
                published = datetime.strptime(
                    date_tag.get_text(strip=True), "%B %d, %Y"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                pass

        entries.append((title, link, "", published))

    return entries


def scrape_anthropic_news() -> list[tuple]:
    """Anthropic은 공식 RSS를 제공하지 않아 /news 목록 페이지를 직접 파싱"""
    try:
        resp = requests.get("https://www.anthropic.com/news", headers=_HEADERS, timeout=_TIMEOUT)
        resp.raise_for_status()
    except Exception as e:
        logger.error(f"  Error scraping Anthropic Blog: {e}")
        return []

    soup = BeautifulSoup(resp.text, "lxml")
    entries = []
    seen_links = set()
    for item in soup.select("a[href^='/news/']"):
        href = item.get("href", "")
        if href == "/news/" or not href or href in seen_links:
            continue

        # 피처드 카드는 클래스명이 "featuredTitle"처럼 대문자를 포함하므로 대소문자 무시 매칭
        title_tag = item.find(class_=re.compile("title", re.IGNORECASE))
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        if not title:
            continue
        seen_links.add(href)

        link = f"https://www.anthropic.com{href}"
        p_tag = item.find("p")
        summary = p_tag.get_text(strip=True) if p_tag else ""
        time_tag = item.find("time")
        published = None
        if time_tag:
            try:
                published = datetime.strptime(
                    time_tag.get_text(strip=True), "%b %d, %Y"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                pass

        entries.append((title, link, summary, published))

    return entries


SCRAPERS = {
    "geeknews": scrape_geeknews,
    "langchain_blog": scrape_langchain_blog,
    "anthropic_news": scrape_anthropic_news,
}
