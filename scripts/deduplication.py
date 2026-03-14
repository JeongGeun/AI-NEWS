"""URL 해시 기반 중복 제거 모듈"""

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_FILE = Path(__file__).parent.parent / "data" / "seen_articles.json"
MAX_HASHES = 2000


def _url_hash(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()


def _load() -> dict:
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"hashes": [], "last_updated": ""}


def _save(data: dict) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def filter_new(articles: list[dict]) -> list[dict]:
    """이미 처리된 기사 제거 후 새 기사만 반환, seen DB 업데이트"""
    data = _load()
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
        # Rolling window: 최대 MAX_HASHES 유지
        if len(all_hashes) > MAX_HASHES:
            all_hashes = all_hashes[-MAX_HASHES:]
        data["hashes"] = all_hashes
        data["last_updated"] = datetime.now(timezone.utc).isoformat()
        _save(data)
        logger.info(f"Deduplication: {len(articles)} → {len(new_articles)} new articles")

    return new_articles
