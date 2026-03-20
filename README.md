# 테크 뉴스 데일리

AI, 프론트엔드, 백엔드, DevOps/인프라 분야의 기술 뉴스를 매일 자동 수집하고, Claude AI가 한국어로 요약·분류하여 Jekyll 블로그로 발행하는 파이프라인입니다.

## 데모

> **`https://jeonggeun.github.io/AI-NEWS`**

---

## 파이프라인 개요

```
GitHub Actions cron (21:09 UTC = 06:09 KST 다음날)
  → config/topics.yml 로드 (AI / 프론트엔드 / 백엔드 / DevOps)
  → 토픽별 순차 실행:
      → RSS 수집 (토픽별 소스에서 fetch_topic())
      → 중복 제거 (토픽별 URL SHA-256 해시)
      → 본문 전문 추출 (newspaper3k)
      → Claude Haiku Batch API: 한국어 요약 + 토픽 관련성 분류 (topic_labels)
      → 관련성 필터링 후 Jekyll 마크다운 포스트 생성
  → GitHub Pages 배포
```

---

## 토픽 & 수집 소스

토픽 설정은 **`config/topics.yml`** 에서 관리합니다. 코드 변경 없이 YAML만 수정해 토픽을 추가할 수 있습니다.

### 🤖 AI 뉴스 (22개 소스)

| 소스 | 서브카테고리 | 일일 최대 | 사전 필터 |
|------|------------|---------|---------|
| arXiv cs.AI / cs.LG / cs.CL | 연구 | 각 10개 | 키워드 (arxiv) |
| HuggingFace Blog | 산업 | 5개 | — |
| Google DeepMind / Google AI Blog | 산업 | 5개 | — |
| VentureBeat AI / TechCrunch AI | 뉴스 | 8개 | — |
| MIT Technology Review / The Verge AI | 뉴스 | 5개 | — |
| The Gradient | 연구 | 3개 | — |
| GeekNews | 커뮤니티 | 10개 | 키워드 (community) |
| Hacker News | 커뮤니티 | 8개 | URL 쿼리 필터 |
| Reddit r/MachineLearning | 커뮤니티 | 5개 | 키워드 (community) |
| Reddit r/LocalLLaMA | 커뮤니티 | 5개 | — |
| GitHub Blog (AI) / Simon Willison / LangChain Blog | 개발자 | 5개 | — |
| Stack Overflow Blog / Dev.to | 개발자 | 5개 | 키워드 (developer) |
| Import AI / The Batch | 뉴스레터 | 3개 | — |

### 💻 프론트엔드 (8개 소스)

CSS-Tricks, Smashing Magazine, web.dev, React Blog, Vue.js Blog, Angular Blog, Dev.to (JavaScript, WebDev)

### 🖥 백엔드 (7개 소스)

Go Blog, Rust Blog, Spring Blog, Martin Fowler, InfoQ, Dev.to (Backend, API)

### ⚙️ DevOps/인프라 (8개 소스)

Kubernetes Blog, Docker Blog, Grafana Blog, HashiCorp Blog, AWS DevOps Blog, GitLab Blog, GitHub Blog, Dev.to (DevOps)

---

## LLM 기반 관련성 분류

기사 수집 후 Claude Haiku가 **요약과 분류를 1회 배치 API 호출로 동시에** 처리합니다.

```json
{
  "korean_title": "...",
  "korean_summary": "...",
  "english_summary": "...",
  "category": "research | industry | news | developer | tutorial | community",
  "tags": ["tag1", "tag2"],
  "significance": "high | medium | low",
  "key_entities": ["entity1"],
  "topic_labels": ["ai", "devops"]
}
```

`topic_labels`에 현재 토픽 slug가 포함된 기사만 최종 포스트에 수록됩니다. 별도의 분류 API 호출 없이 추가 비용 없이 관련성 판단이 이루어집니다.

---

## 디렉토리 구조

```
AI-NEWS/
├── .github/workflows/
│   ├── daily-news.yml       # cron 스케줄 + 뉴스 수집 파이프라인
│   └── deploy.yml           # Jekyll 빌드 + GitHub Pages 배포
├── config/
│   └── topics.yml           # 토픽 정의 (slug, RSS 소스, LLM 설명)
├── scripts/
│   ├── collect.py           # 오케스트레이터 — 토픽 루프
│   ├── rss_fetcher.py       # RSS 파싱 (feedparser) — fetch_topic()
│   ├── web_scraper.py       # 본문 전문 추출 (newspaper3k)
│   ├── deduplication.py     # 토픽별 URL 해시 중복 제거
│   ├── claude_summarizer.py # Batch API 요약 + topic_labels 분류
│   └── post_generator.py    # 토픽별 Jekyll 마크다운 생성
├── data/
│   ├── seen_articles_ai.json       # 토픽별 중복 제거 DB
│   ├── seen_articles_frontend.json
│   ├── seen_articles_backend.json
│   └── seen_articles_devops.json
├── _posts/                  # 자동 생성 일일 포스트 (YYYY-MM-DD-{slug}-daily.md)
├── _tabs/
│   ├── ai.md                # AI 뉴스 탭 (layout: category)
│   ├── frontend.md          # 프론트엔드 탭
│   ├── backend.md           # 백엔드 탭
│   ├── devops.md            # DevOps/인프라 탭
│   └── about.md
├── _includes/
│   └── search-loader.html   # Chirpy 검색 오버라이드 (LLM / 키워드 분기)
├── assets/js/
│   ├── llm-search.js        # 자연어 검색 클라이언트
│   └── data/
│       └── llm-search-index.json  # 경량 검색 인덱스 (Jekyll 빌드 시 생성)
├── vercel/
│   ├── api/search.js        # Vercel Serverless Function (LLM 검색 API)
│   ├── vercel.json
│   └── package.json
├── _config.yml              # Jekyll (Chirpy 테마)
├── index.html               # 토픽 카드 랜딩 페이지
└── requirements.txt
```

---

## 시작하기

### 1. 의존성 설치

```bash
# Python
pip install -r requirements.txt

# Ruby / Jekyll
bundle install
```

### 2. 로컬 실행 (파이프라인 테스트)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/collect.py
```

실행 후 `_posts/YYYY-MM-DD-{slug}-daily.md` 파일이 토픽별로 생성됩니다.

### 3. 토픽 추가

`config/topics.yml`에 새 토픽 블록을 추가하면 코드 변경 없이 파이프라인에 반영됩니다:

```yaml
- slug: "security"
  name: "보안"
  tab_order: 5
  tab_icon: "fas fa-shield-alt"
  jekyll_category: "security"
  llm_description: "Cybersecurity, vulnerabilities, zero-day exploits, security tools..."
  rss_sources:
    - url: "https://krebsonsecurity.com/feed/"
      source: "Krebs on Security"
      sub_category: "news"
      max_items: 5
```

그 다음 `_tabs/security.md` 탭 파일만 추가하면 됩니다.

### 4. Jekyll 로컬 확인

```bash
bundle exec jekyll serve
# → http://localhost:4000/AI-NEWS/
```

---

## GitHub Actions 배포 설정

### Step 1. Secret 등록

GitHub repo → **Settings → Secrets and variables → Actions** → New repository secret

| Name | Value |
|------|-------|
| `ANTHROPIC_API_KEY` | Anthropic API 키 |

### Step 2. 첫 워크플로 수동 실행

**Actions 탭 → "Daily Tech News Collection & Publish" → Run workflow**

### Step 3. GitHub Pages 활성화

**Settings → Pages → Branch: `gh-pages` → Save**

이후 매일 21:09 UTC(익일 06:09 KST)에 자동 실행됩니다.

---

## LLM 자연어 검색 (Vercel Function)

블로그 검색창에서 키워드가 아닌 자연어로 기사를 검색할 수 있습니다.

```
"React 18 성능 개선 관련 최신 글 보여줘"
"Kubernetes 보안 취약점 관련 기사"
```

### 동작 방식

```
사용자 입력 → 브라우저 JS
  → Vercel Function (ANTHROPIC_API_KEY 보관)
  → llm-search-index.json (경량 검색 인덱스) fetch
  → Claude Haiku로 관련 기사 상위 5개 선정 + 이유 설명
  → 결과 카드 렌더링
```

### Vercel 배포

```bash
npm install -g vercel
cd vercel
vercel login
vercel secret put ANTHROPIC_API_KEY
vercel --prod
```

배포 후 `_config.yml`에서 주석 해제:

```yaml
llm_search_worker_url: "https://YOUR_PROJECT.vercel.app/api/search"
```

현재 배포 URL: `https://vercel-one-opal.vercel.app/api/search`

---

## 비용

| 항목 | 내용 |
|------|------|
| 모델 | `claude-haiku-4-5` (Message Batches API, 50% 할인) |
| 수집 비용 | ~166개 기사/일 (4개 토픽) · **약 $0.20/일** |
| 검색 비용 | ~$0.0005/검색 · 100회/일 기준 **$0.05/월** |
| 인프라 | GitHub Actions (무료) + GitHub Pages (무료) + Vercel (무료 티어) |

---

## 기술 스택

- **수집**: Python 3.12 + feedparser + newspaper3k + pyyaml
- **분류·요약**: [Anthropic Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/message-batches) (Claude Haiku)
- **검색**: Vercel Serverless Function + Claude Haiku
- **블로그**: Jekyll + [Chirpy 테마](https://github.com/cotes2046/jekyll-theme-chirpy)
- **CI/CD**: GitHub Actions + [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)
