---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

# AI 뉴스 데일리 브리핑

이 블로그는 매일 오전 9시(KST) AI 관련 뉴스를 자동으로 수집하여 한국어로 요약합니다.

## 수집 소스

- **연구**: arXiv (cs.AI, cs.LG, cs.CL), The Gradient
- **산업**: HuggingFace Blog, Google DeepMind Blog, Google AI Blog
- **뉴스**: VentureBeat AI, TechCrunch AI, MIT Technology Review, The Verge AI

## 기술 스택

- **수집**: Python + feedparser + newspaper3k
- **요약**: Claude Haiku (Anthropic Message Batches API)
- **발행**: Jekyll (Chirpy 테마) + GitHub Actions + GitHub Pages
