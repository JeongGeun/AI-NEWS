---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---

# 테크 뉴스 데일리 브리핑

이 블로그는 매일 오전 AI, 프론트엔드, 백엔드, DevOps/인프라 분야의 기술 뉴스를 자동으로 수집하여 한국어로 요약합니다.

## 토픽별 수집 소스

### 🤖 AI 뉴스
- **연구**: arXiv (cs.AI, cs.LG, cs.CL), The Gradient
- **산업**: HuggingFace Blog, Google DeepMind Blog, Google AI Blog
- **뉴스**: VentureBeat AI, TechCrunch AI, MIT Technology Review, The Verge AI
- **개발자**: GitHub Blog, Simon Willison, LangChain Blog, Stack Overflow Blog, Dev.to
- **커뮤니티**: GeekNews, Hacker News, Reddit r/MachineLearning, Reddit r/LocalLLaMA
- **뉴스레터**: Import AI, The Batch (deeplearning.ai)

### 💻 프론트엔드
- CSS-Tricks, Smashing Magazine, web.dev
- React Blog, Vue.js Blog, Angular Blog
- Dev.to (JavaScript, WebDev)

### 🖥 백엔드
- Go Blog, Rust Blog, Spring Blog
- Martin Fowler, InfoQ
- Dev.to (Backend, API)

### ⚙️ DevOps/인프라
- Kubernetes Blog, Docker Blog, Grafana Blog
- HashiCorp Blog, AWS DevOps Blog, GitLab Blog, GitHub Blog
- Dev.to (DevOps)

## 기술 스택

- **수집**: Python + feedparser + newspaper3k
- **분류·요약**: Claude Haiku (Anthropic Message Batches API) — LLM 기반 토픽 관련성 분류
- **검색**: Claude Haiku + Vercel Serverless Function (자연어 LLM 검색)
- **발행**: Jekyll (Chirpy 테마) + GitHub Actions + GitHub Pages
