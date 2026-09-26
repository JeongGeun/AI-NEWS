---
layout: post
title: "2026-09-26 DevOps/인프라 데일리 브리핑"
date: 2026-09-26 00:07:00 +0900
categories: [devops]
tags:
  - CI/CD
  - DNS
  - DNS management
  - DevOps
  - Docker
  - GDPR compliance
  - PostgreSQL
  - RDAP
  - RFC 9083
  - TTL optimization
  - WHOIS
  - ai-agents
  - artifactory
  - authentication bypass
  - backend engineering
  - best-practices
  - connection pooling
  - container
  - control plane selection
  - database optimization
---

> 수집 시각: 2026-09-26 00:13 UTC | 총 7건

## 커뮤니티

### 1. [JFrog Artifactory CVE-2026-82329: 기본 조인 키를 통한 인증 우회 취약점](https://dev.to/jeffreyciend/jfrog-artifactory-cve-2026-82329-the-default-join-key-as-an-authentication-bypass-2ipc)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: JFrog Artifactory에서 기본값으로 설정된 빈 조인 키를 악용한 인증 우회 취약점(CVE-2026-82329)이 발견되었습니다. 클러스터된 배포 환경에서 공유 비밀로 사용되는 조인 키가 비어있거나 기본값으로 설정되면 공격자가 관리자 토큰을 위조할 수 있어 자격증명 없이 저장소에 접근할 수 있습니다. CISA가 공개 취약점 목록에 추가했으며 7.161.20 이하 버전이 영향을 받습니다.

**English Summary**: JFrog Artifactory CVE-2026-82329 is an authentication bypass vulnerability caused by a default empty join key in clustered deployments. Attackers can forge administrative tokens without credentials, gaining access to private packages, repositories, and stored credentials. Exploitation activity was observed on September 1, 2026, affecting versions below 7.161.20.

**핵심 키워드**: JFrog Artifactory, CVE-2026-82329, CISA, watchTowr, join key

### 2. [PostgreSQL 연결 풀러 비교: PgBouncer vs Supavisor vs RDS Proxy](https://dev.to/libme/pgbouncer-vs-supavisor-vs-rds-proxy-which-postgres-pooler-survives-transaction-mode-1l52)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: PostgreSQL의 '너무 많은 클라이언트' 오류를 해결하기 위한 세 가지 주요 연결 풀러를 비교 분석한다. 각 풀러는 수백 개의 앱 연결을 수십 개의 백엔드 연결로 다중화하지만, 트랜잭션 모드에서 Prepared Statement와 세션 변수를 손상시킨다. PgBouncer는 최고의 제어권, Supavisor는 합리적인 선택, RDS Proxy는 IAM 인증과 장애 조치가 중요할 때 최적이다.

**English Summary**: The article compares three Postgres connection poolers (PgBouncer, Supavisor, RDS Proxy) for handling the 'too many clients' error. While all three multiplex hundreds of app connections onto fewer backend connections, they sacrifice session features like prepared statements and LISTEN/NOTIFY. Each pooler suits different use cases based on operational requirements and environment.

**핵심 키워드**: PgBouncer, Supavisor, RDS Proxy, PostgreSQL, Supabase

### 3. [기본 커밋이 동일한 실패를 재현할 때만 플레이크 프리즈 승인](https://dev.to/datacpp_8185/accept-a-flake-freeze-only-when-base-replays-the-same-miss-1kmm)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 본 문서는 테스트 플레이크 프리즈(flake freeze) 승인의 조건을 정의합니다. 패치 에이전트에서 플레이크 프리즈는 기본 커밋이 동일한 시드에서 동일한 속성을 놓칠 때만 유효합니다. 속성 해시, 픽스처 에포크, 재시도 횟수 등 4가지 핵심 사실이 일치해야 하며, 하나라도 다르면 패치가 도입한 회귀로 간주됩니다.

**English Summary**: This article proposes criteria for accepting flake freezes in agent patches. A flake freeze is valid only when the unmodified base commit fails the same property on the same seed, with matching property-source digest and fixture epoch. Four key facts must align: base_misses, base_attempts, property_sha256, and fixture_epoch; any deviation indicates the patch introduced a regression.

**핵심 키워드**: flake freeze, base commit, property check, fixture epoch, agent patch

### 4. [SDE 면접을 위한 Docker 완벽 가이드](https://dev.to/shogun_the_grt/docker-for-sde-interviews-the-guide-i-wish-id-had-205h)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 이 글은 백엔드 면접에서 자주 출제되는 Docker에 대해 심층적으로 설명합니다. 컨테이너가 경량 가상머신이 아닌 리눅스 커널의 격리된 프로세스라는 핵심 개념부터 시작하여, Dockerfile 작성, 이미지 레이어, 네트워킹, 스토리지, Compose, 디버깅 전략 등을 다룹니다. 면접관이 좋아하는 시나리오 질문에 대비하기 위한 실무적인 플레이북을 제공합니다.

**English Summary**: A comprehensive guide for SDE interviews covering Docker fundamentals, including how containers work under the hood using Linux kernel namespaces rather than being lightweight VMs. The article covers Dockerfile best practices, images, layers, networking, storage, Docker Compose, CLI commands, security basics, and debugging strategies for common interview scenarios.

**핵심 키워드**: Docker, containers, Linux namespaces, Dockerfile, PID namespace, DevOps

### 5. [마켓플레이스 검증을 위한 TTL 단계적 변경 전략](https://dev.to/wilfredknight8447/marketplace-verification-with-scheduled-pre-change-ttl-lowering-and-restore-9d1)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 마켓플레이스의 소유권 확인을 위해 DNS TTL을 효율적으로 관리하는 방법을 제시한다. 변경 1일 전 TTL 단축, 변경 시점에 검증 레코드 수정, 이후 원래 TTL 복구의 3단계 프로세스를 권장한다. 다양한 DNS 제어 플레인(Infra, Route 53, Cloudflare, Google Cloud DNS, DNSimple)의 특성을 비교하며 팀의 인프라 환경에 맞는 선택을 강조한다.

**English Summary**: This article recommends a three-step DNS TTL management strategy for marketplace domain verification: lower TTL one day before cutover, change the verification record at cutover, and restore the original TTL afterward. The author compares various DNS control planes (Infrai, AWS Route 53, Cloudflare, Google Cloud DNS, DNSimple) and advises teams to choose based on how reliably the control plane can preserve this three-step intent rather than pure DNS write speed.

**핵심 키워드**: Infrai, Amazon Route 53, Cloudflare DNS, Google Cloud DNS, DNSimple

### 6. [Golden Trace: AI 에이전트 회귀 테스트의 잃어버린 핵심](https://dev.to/anciwasim/golden-trace-the-eval-anchor-most-teams-skip-1501)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 대부분의 팀은 실패한 에이전트 실행만 기록하고 성공한 경로를 저장하지 않아 나중의 변경으로 품질이 저하된다. 'Golden Trace'는 성공한 전체 실행(입력, 계획, 툴 호출, 중간 상태, 결과)을 회귀 테스트의 기준점으로 고정하는 방식으로, 프롬프트나 모델 변경 후에도 원래의 성공 경로가 유지되는지 확인하는 제어 메커니즘이다.

**English Summary**: Teams typically log failed agent runs but fail to freeze successful ones as baselines, causing performance degradation after prompt updates or model changes that go undetected in demos. 'Golden Trace' proposes storing a complete successful end-to-end agent run (inputs, plans, tool calls, intermediate states, outcomes) as a sacred regression anchor to verify that future changes don't break the proven happy path.

**핵심 키워드**: Golden Trace, agent runs, regression anchor, invoice exception agent, evaluation

### 7. [WHOIS에서 RDAP로: 도메인 조회 프로토콜의 진화](https://dev.to/glitchbound/whois-is-gone-rdap-replaced-it-and-a-404-does-not-mean-what-you-think-4cim)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 기존의 평문 기반 WHOIS 프로토콜은 RFC 9083 표준의 RDAP로 완전히 대체되었습니다. RDAP는 JSON 형식으로 응답하며 모든 gTLD 레지스트리에서 필수 운영됩니다. GDPR 이후 개인정보는 제공되지 않지만, 레지스트라, 등록일, 만료일, DNSSEC 상태 등 운영 정보는 여전히 조회 가능합니다.

**English Summary**: WHOIS, the legacy plaintext domain lookup protocol on port 43, has been replaced by RDAP (RFC 9083), which returns JSON and is now required by all gTLD registries. Post-GDPR, RDAP no longer returns registrant personal data, but provides valuable operational information including registrar, registration/expiry dates, status codes, and DNSSEC details.

**핵심 키워드**: RDAP, WHOIS, gTLD registries, RFC 9083, GDPR
