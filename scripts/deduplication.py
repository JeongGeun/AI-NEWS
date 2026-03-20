"""URL 해시 기반 중복 제거 모듈 — 토픽별 독립 파일 사용"""

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data"
MAX_HASHES = 2000


def _data_file(topic: str) -> Path:
    return DATA_DIR / f"seen_articles_{topic}.json"


def _url_hash(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()


def _load(topic: str) -> dict:
    path = _data_file(topic)
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"hashes": [], "last_updated": ""}


def _save(data: dict, topic: str) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(_data_file(topic), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def filter_new(articles: list[dict], topic: str = "global") -> list[dict]:
    """이미 처리된 기사 제거 후 새 기사만 반환, seen DB 업데이트.

    Args:
        articles: 기사 dict 목록
        topic: 토픽 slug (seen_articles_{topic}.json 파일 구분용)
    """
    data = _load(topic)
    seen: set[str] = set(data.get("hashes", []))

    new_articles = []
    new_hashes = []

    for article in articles:
        url = article.get("url", "")
        if not url:
            continue
        h = _url_hash(url)
        if h not in seen:
            new_articles.append(article)
            new_hashes.append(h)
            seen.add(h)

    if new_hashes:
        all_hashes = data.get("hashes", []) + new_hashes
        if len(all_hashes) > MAX_HASHES:
            all_hashes = all_hashes[-MAX_HASHES:]
        data["hashes"] = all_hashes
        data["last_updated"] = datetime.now(timezone.utc).isoformat()
        _save(data, topic)
        logger.info(f"[{topic}] Deduplication: {len(articles)} → {len(new_articles)} new articles")

    return new_articles
