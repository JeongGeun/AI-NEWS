# CLAUDE.md — AI-NEWS 프로젝트 컨텍스트

## 프로젝트 개요

매일 기술 뉴스(AI, 프론트엔드, 백엔드, DevOps/인프라)를 자동 수집하고, Claude Haiku로 한국어 요약 및 토픽 분류 후 Jekyll 블로그로 발행하는 파이프라인.

- **블로그**: `https://jeonggeun.github.io/AI-NEWS`
- **LLM 검색 API**: `https://vercel-one-opal.vercel.app/api/search`

---

## 핵심 설계 원칙

- **`config/topics.yml`이 유일한 진실의 원천** — 새 토픽 추가 시 이 파일만 수정, Python 코드 변경 불필요
- **LLM 분류를 요약과 통합** — 요약 + `topic_labels` 분류를 1회 Batch API 호출로 처리 (추가 비용 없음)
- **토픽별 독립 파일** — dedup DB (`seen_articles_{slug}.json`), 포스트 (`YYYY-MM-DD-{slug}-daily.md`)

---

## 디렉토리 구조

```
config/topics.yml          ← 토픽 정의 (수정 시 파이프라인 자동 반영)
scripts/
  collect.py               ← 오케스트레이터 (topics.yml 로드 → 토픽별 파이프라인 실행)
  rss_fetcher.py           ← fetch_topic(topic: dict) → list[dict]
  deduplication.py         ← filter_new(articles, topic="ai") → 토픽별 seen_articles_{slug}.json
  claude_summarizer.py     ← summarize_articles(articles, client, topic_definitions) → topic_labels 포함
  post_generator.py        ← generate_post(articles, topic: dict) → _posts/YYYY-MM-DD-{slug}-daily.md
  web_scraper.py           ← enrich_articles(articles) — 변경 없음
data/
  seen_articles_{slug}.json ← 토픽별 URL 해시 DB (최대 2000개 rolling window)
_posts/
  YYYY-MM-DD-ai-daily.md   ← categories: [ai]
  YYYY-MM-DD-frontend-daily.md
  ...
_tabs/
  ai.md / frontend.md / backend.md / devops.md  ← layout: category, category: {slug}
  about.md
_includes/
  search-loader.html        ← Chirpy 검색 오버라이드 (site.llm_search_worker_url 유무로 분기)
assets/js/
  llm-search.js             ← 클라이언트 LLM 검색 UI (800ms 디바운스, AbortController)
  data/llm-search-index.json ← Liquid 템플릿 → Jekyll 빌드 시 생성 (최근 300개 포스트 경량 인덱스)
vercel/
  api/search.js             ← Vercel Serverless Function (Claude Haiku 검색)
  vercel.json / package.json
index.html                  ← 토픽 카드 랜딩 페이지 (layout: page)
```

---

## 파이프라인 흐름

```python
# collect.py 핵심 흐름
config = yaml.safe_load("config/topics.yml")
for topic in config["topics"]:
    articles = rss_fetcher.fetch_topic(topic)           # RSS 수집
    articles = deduplication.filter_new(articles, topic["slug"])  # 중복 제거
    articles = web_scraper.enrich_articles(articles)    # 본문 추출
    articles = claude_summarizer.summarize_articles(articles, client, all_topics)  # 요약+분류
    relevant = [a for a in articles
                if "topic_labels" not in a             # 파싱 실패 → 포함 (안전 폴백)
                or topic["slug"] in a["topic_labels"]] # 관련성 있는 기사만
    post_generator.generate_post(relevant, topic)
```

---

## Claude API 응답 스키마

`claude_summarizer.py`가 기사마다 요청하는 JSON 응답:

```json
{
  "korean_title": "한국어 제목 (50자 이내)",
  "korean_summary": "한국어 요약 (200자 이내)",
  "english_summary": "English summary (2-3 sentences)",
  "category": "research | industry | news | developer | tutorial | community",
  "tags": ["tag1", "tag2", "tag3"],
  "significance": "high | medium | low",
  "key_entities": ["entity1", "entity2"],
  "topic_labels": ["ai", "devops"]
}
```

`topic_labels`는 현재 처리 중인 토픽 slug와 매칭되어 관련성 필터링에 사용됩니다.

---

## 토픽 추가 방법

1. `config/topics.yml`에 새 토픽 블록 추가
2. `_tabs/{slug}.md` 생성:
   ```yaml
   ---
   layout: category
   title: "탭 표시명"
   category: {slug}
   icon: fas fa-icon-name
   order: N
   ---
   ```
3. `index.html`에 카드 블록 추가 (선택)
4. 커밋 → GitHub Actions가 자동으로 새 토픽 포스트 생성 시작

Python 코드 수정 불필요.

---

## 환경변수

| 변수 | 위치 | 설명 |
|------|------|------|
| `ANTHROPIC_API_KEY` | GitHub Secrets / `.env` / Vercel env | 뉴스 요약 + 검색 |
| `SITE_URL` | Vercel env | GitHub Pages URL (기본값: `https://jeonggeun.github.io/AI-NEWS`) |

---

## Jekyll 설정 주요 포인트

- **테마**: `jekyll-theme-chirpy` v7.0
- **탭**: `_tabs/` 파일이 `layout: category`를 사용해 해당 카테고리 포스트를 카드 형태로 표시
- **Home**: `index.html` — `layout: page`, 4개 토픽 카드 랜딩 페이지
- **LLM 검색**: `_config.yml`의 `llm_search_worker_url` 설정 시 활성화, 미설정 시 SimpleJekyllSearch 폴백
- **exclude**: `scripts/`, `data/`, `config/`, `vercel/`은 Jekyll 빌드에서 제외

---

## GitHub Actions

| 워크플로 | 트리거 | 역할 |
|---------|--------|------|
| `daily-news.yml` | cron 21:09 UTC / 수동 | Python 파이프라인 실행, `_posts/` + `data/` 커밋 |
| `deploy.yml` | `daily-news.yml` 완료 / main push | Jekyll 빌드 → `gh-pages` 배포 |

timeout: 90분 (4개 토픽 × Batch API 대기 시간)

---

## 로컬 개발

```bash
# Python 파이프라인 테스트
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/collect.py

# Jekyll 로컬 서버
bundle install
bundle exec jekyll serve --livereload
# → http://localhost:4000/AI-NEWS/

# Vercel Function 로컬 테스트
cd vercel
vercel dev
# → http://localhost:3000/api/search?q=React+hooks
```

---

## 비용 참고

- 수집·요약: ~166개 기사/일 × ~700 output tokens = **약 $0.20/일**
- LLM 검색: ~$0.0005/검색 (Claude Haiku Batch API 미사용, 일반 API)
- 인프라: GitHub Actions + GitHub Pages + Vercel 모두 **무료 티어**
