"""Claude Haiku Batch API로 기사 한국어 요약"""

import anthropic
import json
import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)

MODEL = "claude-haiku-4-5"
BATCH_POLL_INTERVAL = 60  # seconds
BATCH_TIMEOUT = 25 * 60   # 25분

SYSTEM_PROMPT = """You are an AI news analyst specializing in Korean tech media.
Summarize each article concisely and accurately.
Always respond with valid JSON only — no markdown fences, no extra text."""

USER_PROMPT_TEMPLATE = """Summarize this AI/tech article in both Korean and English.

Title: {title}
Source: {source}
Content: {content}

Respond with this exact JSON structure:
{{
  "korean_title": "한국어 제목 (원제 의역, 50자 이내)",
  "korean_summary": "한국어 요약 (핵심 내용 3-4문장, 200자 이내)",
  "english_summary": "English summary (2-3 sentences, key findings only)",
  "category": "research | industry | news",
  "tags": ["tag1", "tag2", "tag3"],
  "significance": "high | medium | low",
  "key_entities": ["entity1", "entity2"]
}}"""


def _build_request(article: dict, custom_id: str) -> dict:
    content = article.get("full_text") or article.get("summary", "")
    prompt = USER_PROMPT_TEMPLATE.format(
        title=article.get("title", ""),
        source=article.get("source", ""),
        content=content[:1500],
    )
    return {
        "custom_id": custom_id,
        "params": {
            "model": MODEL,
            "max_tokens": 600,
            "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": prompt}],
        },
    }


def _parse_response(text: str) -> Optional[dict]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # JSON 블록 추출 시도
        import re
        match = re.search(r"\{[\s\S]+\}", text)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
    return None


def summarize_articles(articles: list[dict], client: anthropic.Anthropic) -> list[dict]:
    """Batch API로 전체 기사 요약, 결과를 article dict에 병합하여 반환"""
    if not articles:
        return []

    # Batch 요청 생성
    requests = [_build_request(a, f"article_{i}") for i, a in enumerate(articles)]

    logger.info(f"Creating batch with {len(requests)} requests...")
    batch = client.messages.batches.create(requests=requests)
    batch_id = batch.id
    logger.info(f"Batch created: {batch_id}")

    # 완료 대기
    elapsed = 0
    while elapsed < BATCH_TIMEOUT:
        time.sleep(BATCH_POLL_INTERVAL)
        elapsed += BATCH_POLL_INTERVAL

        batch = client.messages.batches.retrieve(batch_id)
        status = batch.processing_status
        counts = batch.request_counts
        logger.info(
            f"  Batch status: {status} | "
            f"succeeded={counts.succeeded} errored={counts.errored} "
            f"processing={counts.processing} ({elapsed}s elapsed)"
        )

        if status == "ended":
            break
    else:
        logger.error("Batch timed out")
        return articles  # 요약 없이 원본 반환

    # 결과 수집
    results_map: dict[str, dict] = {}
    for result in client.messages.batches.results(batch_id):
        custom_id = result.custom_id
        if result.result.type == "succeeded":
            text = result.result.message.content[0].text
            parsed = _parse_response(text)
            if parsed:
                results_map[custom_id] = parsed
            else:
                logger.warning(f"Failed to parse JSON for {custom_id}: {text[:200]}")
        else:
            logger.warning(f"Request {custom_id} failed: {result.result.type}")

    # article dict에 요약 병합
    summarized = []
    for i, article in enumerate(articles):
        custom_id = f"article_{i}"
        summary_data = results_map.get(custom_id, {})
        summarized.append({**article, **summary_data})

    logger.info(
        f"Summarization complete: {len(results_map)}/{len(articles)} succeeded"
    )
    return summarized
