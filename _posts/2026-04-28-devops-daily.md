---
layout: post
title: "2026-04-28 DevOps/인프라 데일리 브리핑"
date: 2026-04-28 00:07:00 +0900
categories: [devops]
tags:
  - .NET
  - AI integration
  - AWS
  - AWS tools
  - DevOps
  - DevOps tooling
  - Docker
  - GitLab
  - Kubernetes
  - MCP protocol
  - Podman
  - api-design
  - application security
  - batch-processing
  - best-practices
  - capacity-planning
  - cloud-infrastructure
  - code modernization
  - command-line
  - container-orchestration
---

> 수집 시각: 2026-04-27 22:19 UTC | 총 10건

## 뉴스 & 릴리즈

### 1. [glab CLI로 AI 에이전트에 GitLab 직접 접근 권한 부여하기](https://about.gitlab.com/blog/give-your-ai-agent-direct-structured-gitlab-access-with-glab-cli/)
**출처**: GitLab Blog · **중요도**: 높음

**한국어 요약**: GitLab은 glab CLI를 통해 AI 에이전트가 GitLab 프로젝트에 직접 접근할 수 있도록 하는 방법을 소개했습니다. 이를 통해 AI 에이전트는 이슈, 머지 리퀘스트, 파이프라인을 직접 읽고 작업할 수 있어 개발자가 컨텍스트를 수동으로 복사-붙여넣기할 필요가 없습니다. MCP를 통한 통합으로 AI 에이전트의 성능을 향상시키고 개발 워크플로우를 가속화할 수 있습니다.

**English Summary**: GitLab introduced a tutorial on enabling AI agents to access GitLab projects directly via the glab CLI, eliminating manual context switching and hallucination issues. By leveraging the Model Context Protocol (MCP), AI agents like Claude and Cursor can reliably read issues, review merge requests, and execute pipelines without requiring manual data relay, resulting in faster and more capable development workflows.

**핵심 키워드**: GitLab, glab CLI, Claude, Cursor, GitLab Duo, MCP (Model Context Protocol)

### 2. [Kubernetes v1.36: 일시 중단된 작업의 변경 가능한 Pod 리소스 (베타)](https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/)
**출처**: Kubernetes Blog · **중요도**: 높음

**한국어 요약**: Kubernetes v1.36에서 일시 중단된 Job의 Pod 템플릿에서 컨테이너 리소스 요청 및 제한을 수정할 수 있는 기능이 베타 단계로 승격되었습니다. 이 기능을 통해 큐 컨트롤러와 클러스터 관리자는 Job이 실행되기 전이나 재개되기 전에 CPU, 메모리, GPU, 확장 리소스 사양을 조정할 수 있습니다. 이를 통해 머신러닝 및 배치 작업의 최적 리소스 할당이 가능해지며, 기존의 Job 삭제 및 재생성 방식의 메타데이터 손실 문제를 해결합니다.

**English Summary**: Kubernetes v1.36 promotes mutable pod resources for suspended Jobs to beta, enabling queue controllers and cluster administrators to adjust CPU, memory, GPU, and extended resource specifications without deleting and recreating Jobs. This feature solves the problem of immutable resource requirements by allowing dynamic resource allocation based on current cluster capacity and hardware availability. It is particularly beneficial for batch and machine learning workloads where optimal resource allocation depends on runtime conditions.

**핵심 키워드**: Kubernetes, Kueue, Pod Resources, Job Suspension, GPU Resource Allocation

## 튜토리얼 & 아티클

### 1. [AWS Transform Custom: 엔터프라이즈급 코드 현대화 자동화 솔루션](https://aws.amazon.com/blogs/devops/aws-transform-custom-enterprise-code-modernization-with-the-learn-scale-improve-flywheel/)
**출처**: AWS DevOps Blog · **중요도**: 높음

**한국어 요약**: AWS Transform custom은 대규모 엔터프라이즈 환경에서 수십 개 이상의 저장소를 효율적으로 현대화할 수 있도록 설계된 도구입니다. 한 고객은 이 솔루션을 통해 현대화 기간을 7-12주에서 2.5주로 단축하고, 업무 시간을 10-20배 감소시켰습니다. 단순 코드 변환을 넘어 팀 조율, 지식 공유, 품질 유지까지 전체 포트폴리오 차원의 통합 솔루션을 제공합니다.

**English Summary**: AWS Transform custom addresses enterprise-scale code modernization challenges by automating bulk transformations across multiple repositories while coordinating teams and maintaining consistency. A customer case study demonstrates a 3-5x reduction in modernization timelines (from 7-12 weeks to 2.5 weeks) and 10-20x reduction in effort hours. The solution combines intelligent learning and scaled execution to solve coordination problems inherent in large-scale digital transformations.

**핵심 키워드**: AWS, AWS Transform custom, enterprise modernization, code transformation

## 커뮤니티

### 1. [경량형 로그 모니터링 플랫폼 Logarys 소개](https://dev.to/sebk69/introducing-logarys-a-lightweight-scalable-log-monitoring-platform-leg)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자를 위해 설계된 경량 로그 수집 및 쿼리 플랫폼 Logarys가 공개되었다. NATS JetStream과 MongoDB를 기반으로 한 아키텍처로 빠른 수집, 모듈식 설계, 간단한 배포를 제공한다. 복잡한 로깅 스택의 한계를 극복하고 확장성 있는 관찰성 솔루션을 목표로 한다.

**English Summary**: Logarys, a lightweight log ingestion and querying platform, was introduced as an alternative to complex observability stacks. Built with NATS JetStream and MongoDB, it offers fast ingestion, modular architecture, and simplified deployment via Docker or Kubernetes. The platform emphasizes horizontal scalability, backpressure handling, and flexible ingestion pipelines.

**핵심 키워드**: Logarys, NATS JetStream, MongoDB, Docker, Kubernetes

### 2. [Podman vs Docker: 기술이 아닌 마이그레이션 비용의 문제](https://dev.to/yetmike/podman-lost-to-docker-i-stopped-fighting-it-21hi)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Docker는 71.1%의 채택률로 Podman(11.1%)을 압도하고 있으며, 이는 기술적 우월성 문제가 아닌 생태계 규모의 차이다. Podman의 루트리스 기본 설정, Quadlet 통합 등 기술적 장점은 존재하지만, 기존 Docker 환경에서의 마이그레이션 비용(소켓 경로 차이, CI/CD 파이프라인 업데이트, 개발자 교육 등)이 실질적 장애물이다. 새로운 프로젝트에서는 Podman이 적합하지만, 기존 Docker 인프라 전환은 신중하게 검토해야 한다.

**English Summary**: Docker dominates container technology with 71.1% adoption versus Podman's 11.1%, a gap driven by ecosystem size rather than technical merit. While Podman offers genuine architectural advantages (rootless-by-default, systemd integration, no per-user licensing), migrating existing Docker setups faces hidden costs: socket compatibility issues, CI/CD pipeline updates, and developer retraining. The decision should be context-dependent: Podman suits greenfield projects on RHEL, but established Docker deployments require careful cost-benefit analysis.

**핵심 키워드**: Docker, Podman, Red Hat, CNCF, Docker Hub, Podman Desktop, Stack Overflow 2025 Survey

### 3. [AWS 비용 20-45% 절감하는 체계적 감사 방법](https://dev.to/kloudaudit/how-to-cut-your-aws-bill-by-20-45-without-touching-your-architecture-3b9j)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 클라우드 비용 증가 문제를 해결하기 위한 1시간 내 감사 방법을 제시한다. 좀비 인스턴스 제거, 예약 인스턴스 활용, 스토리지 계층화, 개발 환경 자동 종료, Spot 인스턴스 활용 등 5가지 단계를 통해 아키텍처 변경 없이 비용을 대폭 절감할 수 있다.

**English Summary**: A systematic audit approach to reduce AWS bills by 20-45% without architectural changes. The guide covers five key optimization strategies: eliminating underutilized instances (15-25% savings), switching to Reserved Instances for stable workloads (30-45% savings), implementing storage lifecycle policies, scheduling database shutdowns during off-hours (65% reduction), and using Spot instances for interruptible workloads (60-80% cheaper).

**핵심 키워드**: AWS, EC2, S3, RDS, Reserved Instances, Spot Instances, Compute Savings Plans

### 4. [.NET 개발자 채용이 앱 보안 강화에 필수인 이유](https://dev.to/hoor_ali_428d0ccd853d063e/top-reasons-why-firms-rely-on-net-developers-for-strengthening-apps-security-44oa)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 기업들이 안전하고 확장 가능한 소프트웨어 개발을 위해 .NET 개발자 채용을 늘리고 있다. 마이크로소프트가 개발한 .NET 플랫폼은 내구성, 신뢰성, 유연성을 갖춘 것으로 평가받으며, PC, 엔터프라이즈 앱, 웹, 클라우드 등 다양한 환경을 지원한다. 원격 .NET 개발자 채용을 통해 기업들은 지역 제한 없이 글로벌 인재에 접근할 수 있다.

**English Summary**: Companies increasingly hire .NET developers to build secure and scalable applications. Microsoft's .NET platform offers durability, reliability, and flexibility across PCs, enterprise apps, web, and cloud environments. Remote .NET developer hiring enables businesses to access global talent without geographic limitations.

**핵심 키워드**: .NET Framework, Microsoft, remote developers, enterprise applications

### 5. [Ubuntu 25.10에서 'who' 명령어 작동 불능 - UTMP 단계적 폐기](https://dev.to/jaideepg/utmp-being-phased-out-why-who-returns-empty-output-on-modern-ubuntu-1chj)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Ubuntu 25.10에서 'who' 명령어가 빈 출력을 반환하는 문제가 발생했습니다. 원인은 1970년대부터 사용된 UTMP 메커니즘을 Ubuntu가 단계적으로 폐기하면서 발생한 것으로, /var/run/utmp 파일 누락 또는 AppArmor의 권한 제한이 주요 원인입니다. 다른 명령어인 'w'나 'loginctl'은 정상 작동합니다.

**English Summary**: Ubuntu 25.10 users are experiencing issues with the 'who' command returning empty output despite exit code 0. The root cause is Ubuntu's phasing out of the UTMP mechanism used since the 1970s, with missing /var/run/utmp file or AppArmor permission denial being the culprits. Alternative commands like 'w' and 'loginctl' continue to work normally.

**핵심 키워드**: Ubuntu 25.10, who command, UTMP, Launchpad Bug #2130814, AppArmor

### 6. [30분 시스템 디자인 인터뷰에서 Rate Limiting 설계하기](https://dev.to/gabrielanhaia/rate-limiting-in-a-30-minute-system-design-interview-2lgg)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 시스템 디자인 인터뷰에서 공개 API의 Rate Limiting을 30분 내에 설계하는 실전 전략을 다룬다. 먼저 요구사항을 명확히 파악하고(인증 방식, 제한 규칙, RPS 등), 적절한 알고리즘을 선택하며, 구현 세부사항과 확장성을 논의하는 단계별 접근 방식을 제시한다. Back-of-the-envelope 계산으로 Redis 같은 적절한 기술을 선택하는 방법을 보여준다.

**English Summary**: A practical guide for designing rate limiting in a 30-minute system design interview. The article provides a step-by-step approach: clarify requirements (authentication type, limits per minute/hour, peak RPS), select appropriate algorithms, perform capacity calculations, and discuss implementation details. It emphasizes asking clarifying questions first and using back-of-the-envelope math to guide technology choices like Redis.

**핵심 키워드**: Rate Limiting, System Design Interview, Redis, API, Back-of-the-envelope Calculation

### 7. [PostgreSQL JSON 컬럼을 스키마로 마이그레이션하기](https://dev.to/gabrielanhaia/migrating-from-a-json-column-to-a-proper-schema-in-postgres-4o9e)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: PostgreSQL에서 JSONB 컬럼에 저장된 데이터를 적절한 타입의 컬럼으로 마이그레이션하는 방법을 설명합니다. 확장-축소(expand-and-contract) 패턴을 사용하여 다운타임 없이 단계적으로 마이그레이션하며, 인덱싱 문제와 락 문제를 해결합니다. 기존 JSON 구조의 문제점(느린 쿼리, 타입 오류, 인덱싱 불가)을 해결하는 실무 가이드입니다.

**English Summary**: This article describes a PostgreSQL migration pattern for moving data from JSONB columns into properly typed columns with zero downtime. Using the expand-and-contract pattern, it addresses production issues like 800ms sequential scans, improper data types in JSON, and indexing challenges by gradually shifting traffic to the new schema while keeping the old one intact.

**핵심 키워드**: PostgreSQL, JSONB, expand-and-contract pattern, ALTER TABLE, sequential scans
