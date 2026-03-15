# AI 뉴스 데일리 브리핑

매일 오전 9시(KST) AI 관련 뉴스를 자동 수집하고, Claude AI가 한국어로 요약하여 Jekyll 블로그로 발행하는 파이프라인입니다.

## 데모

> 배포 후 URL: `https://jeonggeun.github.io/AI-NEWS`

---

## 파이프라인 개요

```
GitHub Actions cron (00:00 UTC = 09:00 KST)
  → RSS 수집 (16개 소스)
  → 중복 제거 (URL SHA-256 해시)
  → 본문 전문 추출 (newspaper3k)
  → 한국어 요약 (Claude Haiku · Batch API)
  → Jekyll 마크다운 포스트 생성
  → GitHub Pages 배포
```

---

## 수집 소스

| 소스 | 카테고리 | 일일 최대 |
|------|---------|---------|
| arXiv cs.AI / cs.LG / cs.CL | 연구 | 각 10개 (키워드 필터) |
| HuggingFace Blog | 산업 | 5개 |
| Google DeepMind Blog | 산업 | 5개 |
| Google AI Blog | 산업 | 5개 |
| VentureBeat AI | 뉴스 | 8개 |
| TechCrunch AI | 뉴스 | 8개 |
| MIT Technology Review | 뉴스 | 5개 |
| The Verge AI | 뉴스 | 5개 |
| The Gradient | 연구 | 3개 |
| GeekNews | 커뮤니티 | 10개 (키워드 필터) |
| Hacker News | 커뮤니티 | 8개 (AI 키워드 필터, 10점 이상) |
| Reddit r/MachineLearning | 커뮤니티 | 5개 (키워드 필터) |
| Reddit r/LocalLLaMA | 커뮤니티 | 5개 |
| GitHub Blog (AI) | 개발자 | 5개 |
| Stack Overflow Blog | 개발자 | 5개 (키워드 필터) |
| Simon Willison's Blog | 개발자 | 5개 |
| LangChain Blog | 개발자 | 5개 |
| Dev.to | 개발자 | 5개 (키워드 필터) |
| Import AI (Substack) | 뉴스레터 | 3개 |
| The Batch (deeplearning.ai) | 뉴스레터 | 3개 |

arXiv는 제목/abstract에 아래 키워드 중 하나 이상 포함된 논문만 수집합니다:
`LLM`, `large language model`, `agent`, `reasoning`, `multimodal`, `RLHF`, `fine-tuning`, `RAG`, `diffusion model`, `vision-language`, `transformer`, `foundation model`, `instruction tuning`, `alignment`

개발자 카테고리 중 Stack Overflow Blog, Dev.to는 아래 키워드 중 하나 이상 포함된 글만 수집합니다:
`copilot`, `cursor`, `devin`, `code generation`, `coding assistant`, `ai coding`, `ide`, `vscode`, `llm api`, `langchain`, `llamaindex`, `vector database`, `embeddings`, `rag pipeline`, `mlops`, `llmops`, `ai engineering`, `prompt engineering`, `inference`, `model deployment`, `github copilot`, `developer tools`, `sdk`, 외 다수

---

## 디렉토리 구조

```
AI-NEWS/
├── .github/workflows/
│   └── daily-news.yml       # cron 스케줄 + Jekyll 빌드 + 배포
├── scripts/
│   ├── collect.py           # 오케스트레이터 (메인 진입점)
│   ├── rss_fetcher.py       # RSS 파싱 (feedparser)
│   ├── web_scraper.py       # 본문 전문 추출 (newspaper3k)
│   ├── deduplication.py     # URL 해시 기반 중복 제거
│   ├── claude_summarizer.py # Batch API 한국어 요약
│   └── post_generator.py    # Jekyll 마크다운 생성
├── data/
│   └── seen_articles.json   # 중복 제거용 URL 해시 저장소
├── _posts/                  # 자동 생성 일일 포스트
├── _tabs/
│   └── about.md
├── _config.yml              # Jekyll (Chirpy 테마)
├── Gemfile
├── index.html
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

실행 후 `_posts/YYYY-MM-DD-ai-news-daily.md` 파일이 생성됩니다.

### 3. Jekyll 로컬 확인

```bash
bundle exec jekyll serve
# → http://localhost:4000
```

---

## GitHub Actions 배포 설정

### Step 1. Secret 등록

GitHub repo → **Settings → Secrets and variables → Actions** → New repository secret

| Name | Value |
|------|-------|
| `ANTHROPIC_API_KEY` | Anthropic API 키 |

`GITHUB_TOKEN`은 Actions에서 자동 제공되므로 별도 설정 불필요합니다.

### Step 2. 첫 워크플로 수동 실행

**Actions 탭 → "Daily AI News Collection & Publish" → Run workflow**

실행 완료 시 `gh-pages` 브랜치가 자동 생성됩니다.

### Step 3. GitHub Pages 활성화

**Settings → Pages → Branch: `gh-pages` → Save**

이후 매일 00:00 UTC(오전 9시 KST)에 자동 실행됩니다.

---

## 비용

| 항목 | 내용 |
|------|------|
| 모델 | `claude-haiku-4-5` |
| 방식 | Message Batches API (50% 할인) |
| 예상 비용 | ~50개 기사/일 기준 **약 $0.01/일 ($3.65/년)** |

---

## 기술 스택

- **수집**: Python 3.12 + feedparser + newspaper3k
- **요약**: [Anthropic Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)
- **블로그**: Jekyll + [Chirpy 테마](https://github.com/cotes2046/jekyll-theme-chirpy)
- **CI/CD**: GitHub Actions + [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)
