---
layout: post
title: "2026-07-23 DevOps/인프라 데일리 브리핑"
date: 2026-07-23 00:07:00 +0900
categories: [devops]
tags:
  - AI coding agents
  - AI governance
  - AWS
  - CI/CD
  - CISO
  - Consul
  - Container
  - DBA
  - Database Recovery
  - DevOps
  - DevOps security
  - Disaster Recovery
  - Docker
  - GitLab Duo
  - GuardDuty
  - Java migration
  - Kubernetes
  - Microsoft Sentinel
  - Oracle
  - RMAN
---

> 수집 시각: 2026-07-22 22:28 UTC | 총 11건

## 튜토리얼 & 아티클

### 1. [Grafana Cloud의 비용 귀속: 관찰성 및 테스트 워크플로우 전반의 지출 관리](https://grafana.com/blog/cost-attribution-in-grafana-cloud-manage-spend-across-observability-and-testing-workflows/)
**출처**: Grafana Blog · **중요도**: 보통

**한국어 요약**: Grafana Cloud가 비용 귀속 기능을 합성 모니터링과 k6 성능 테스트로 확대했다. 이제 조직은 팀, 서비스, 프로젝트별로 관찰성 및 테스트 지출을 추적하고 할당할 수 있으며, 내부 청구 모델(차지백, 쇼백)을 지원한다. 메트릭, 로그, 트레이스뿐만 아니라 테스트 비용까지 일관되게 귀속시킬 수 있다.

**English Summary**: Grafana Cloud extended cost attribution capabilities to Synthetic Monitoring and k6 performance testing, enabling organizations to allocate observability and testing spend across teams, projects, and services. This provides comprehensive visibility into testing costs and supports internal billing models like chargeback and showback, allowing cost traceability for metrics, logs, traces, and testing workflows.

**핵심 키워드**: Grafana Cloud, Grafana Cloud Synthetic Monitoring, Grafana Cloud k6

## 뉴스 & 릴리즈

### 1. [Consul의 다중 포트 서비스 지원으로 간소화된 서비스 관리](https://www.hashicorp.com/blog/one-service-many-doors-multi-port-services-in-consul)
**출처**: HashiCorp Blog · **중요도**: 보통

**한국어 요약**: HashiCorp의 Consul이 네이티브 다중 포트 지원 기능을 통해 애플리케이션을 팀의 이해 방식대로 모델링할 수 있게 되었습니다. 하나의 서비스 ID로 여러 개의 명명된 포트를 관리하여 카탈로그 복잡도를 감소시키고 운영 효율성을 높입니다.

**English Summary**: Consul's native multi-port support enables teams to model applications with one service identity and multiple named ports, reducing service catalog complexity. This feature simplifies how microservices are represented and managed in distributed systems.

**핵심 키워드**: HashiCorp, Consul

### 2. [에이전트 AI 보안, 추측이 아닌 가드레일 필요](https://www.docker.com/blog/agentic-ai-security-ciso-panel/)
**출처**: Docker Blog · **중요도**: 높음

**한국어 요약**: 엔터프라이즈 환경에서 에이전트 AI의 빠른 확산으로 인해 CISO들이 생산성과 보안 사이의 긴장 관계에 직면하고 있다. 개발자들이 승인 없이 보안 고려 없이 AI 에이전트를 사용하는 상황 속에서, 패널 토론에서는 격리된 환경에서 AI 에이전트를 안전하게 실행하고 모니터링할 필요성을 강조했다.

**English Summary**: Enterprise CISOs face mounting pressure to enable agentic AI while maintaining security. The panel discussion highlights the critical need for isolated environments to safely deploy AI agents without compromising oversight and control, balancing business demands for AI productivity with security governance requirements.

**핵심 키워드**: Warp, Zach Lloyd, NanoCo, Gavriel Cohen, Moriah Hara, Docker

### 3. [AI 에이전트 보안: 정책 조언이 아닌 런타임 강제](https://www.docker.com/blog/runtime-enforcement-not-runtime-advice/)
**출처**: Docker Blog · **중요도**: 높음

**한국어 요약**: Docker 블로그는 자율 AI 에이전트의 보안 문제를 다루며, 기존 정책만으로는 부족하고 런타임 단계에서의 강제적 제어가 필수라고 주장합니다. AI 시스템이 리포지토리와 CI/CD 파이프라인 외부에서 작업을 수행할 때, 개발자들은 예측 가능한 거버넌스를 원하며 이는 세 가지 경계 영역에서 해결되어야 한다고 설명합니다.

**English Summary**: The article argues that traditional security policies alone are insufficient for governing autonomous AI agents, emphasizing the need for runtime enforcement rather than policy suggestions. As agents gain access to files, terminals, APIs, and external tools outside traditional checkpoints, developers require predictable governance across three boundary areas rather than restrictive policies.

**핵심 키워드**: Docker, autonomous agents, AI systems, runtime enforcement, governance

### 4. [Cursor와 GitLab으로 Java 8을 Java 21로 현대화하기](https://about.gitlab.com/blog/modernize-java-with-cursor-and-gitlab/)
**출처**: GitLab Blog · **중요도**: 높음

**한국어 요약**: GitLab 블로그에서는 AI 코딩 에이전트 Cursor와 GitLab의 Duo Agent Platform을 활용하여 Java 8에서 Java 21로의 마이그레이션을 안전하게 수행하는 방법을 제시합니다. Cursor는 개별 작업에 집중된 수정을 빠르게 처리하며, GitLab은 이슈 계층과 CI/CD, 코드 리뷰, 보안 스캔으로 전체 소프트웨어 개발 생명주기를 관리하여 안전성을 보장합니다.

**English Summary**: GitLab demonstrates how to use Cursor AI coding agent with GitLab's Duo Agent Platform for safely modernizing Java 8 to Java 21. Cursor handles focused code fixes efficiently, while GitLab manages the broader software lifecycle through issue hierarchies, CI/CD, code review, and security scanning to ensure safe production changes.

**핵심 키워드**: Cursor, GitLab, Java 21, Duo Agent Platform, MCP server

## 커뮤니티

### 1. [허깅페이스 AI 모델 허브, 악성 데이터셋으로 보안 침해](https://dev.to/lainagent_ai/a-dataset-breached-the-worlds-largest-ai-model-hub-363b)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 2026년 7월 16일 허깅페이스는 악성 데이터셋을 통한 보안 침해 사건을 공개했다. 공격자는 머신이 읽도록 의도된 파일을 악용해 코드 실행 경로 2개를 남용했고, 처리 워커에 접근한 후 노드 레벨 권한을 확보했다. 이후 클라우드 자격증명을 탈취하고 내부 클러스터 전역으로 자동 에이전트 프레임워크를 확산시켰으며, 17,000건 이상의 공격자 활동 흔적이 기록되었다.

**English Summary**: Hugging Face disclosed a major security breach on July 16, 2026, where a malicious dataset exploited code-execution vulnerabilities in their data-processing infrastructure, leading to node-level access and lateral movement across internal clusters. The attacker harvested cloud credentials and deployed an autonomous agent framework, with over 17,000 recorded attack events.

**핵심 키워드**: Hugging Face, load_dataset, data-processing infrastructure, autonomous agent framework

### 2. [에뮬레이터, 시뮬레이터, 실제 기기의 테스트 비교](https://dev.to/graceholloway_/emulators-simulators-and-real-devices-compared-32h5)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 모바일 앱 개발 시 에뮬레이터, 시뮬레이터, 실제 기기는 각각 다른 목적을 수행한다. 에뮬레이터는 빠른 피드백으로 초기 버그를 저비용으로 잡을 수 있지만, 시뮬레이터는 칩 동작이나 배터리 상태 같은 하드웨어 의존적 버그를 감지하고, 실제 기기는 출시 전 신뢰성을 확보한다. 팀이 이들을 올바르게 구분해서 사용하면 개발 효율성과 품질을 모두 높일 수 있다.

**English Summary**: Emulators, simulators, and real devices serve different testing purposes in mobile app development. Emulators enable fast feedback for quick bug detection during development, simulators model hardware-specific behavior for deeper issues, and real devices ensure release confidence. Teams must choose the right tool for their testing goals rather than treating them as interchangeable.

**핵심 키워드**: Android emulator, mobile app testing, DevOps

### 3. [Ubuntu 26.04에서 Docker 올바르게 설치하기](https://dev.to/peculiarengineer/install-docker-on-ubuntu-2604-the-right-way-with-the-docker-group-truth-1knd)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Ubuntu 26.04에 Docker를 설치할 때 배포판 기본 패키지 대신 Docker의 공식 apt 저장소를 사용하는 것이 권장된다. 공식 저장소를 통해 최신 버전의 Docker CE, Docker Compose, Buildx 플러그인 등을 설치할 수 있다. 단, docker 그룹에 사용자를 추가할 때 root 권한이 부여되는 보안 영향을 반드시 이해해야 한다.

**English Summary**: This tutorial recommends using Docker's official apt repository instead of Ubuntu's default docker.io package for Ubuntu 26.04 installations. The official method provides the latest Docker versions with Compose and Buildx plugins, but requires careful consideration of security implications when adding users to the docker group, which grants root-equivalent privileges.

**핵심 키워드**: Docker, Ubuntu 26.04, apt repository, docker-ce, docker-compose-plugin

### 4. [AWS GuardDuty를 Microsoft Sentinel과 통합하는 오픈소스 프로젝트](https://dev.to/femitek_8ef22c/looking-for-testers-and-contributors-aws-guardduty-to-microsoft-sentinel-integration-37h3)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자가 AWS GuardDuty의 보안 탐지 결과를 Microsoft Sentinel으로 구조화하여 수집할 수 있도록 돕는 오픈소스 프로젝트를 공개했습니다. 관리형 및 실시간 수집 옵션, KQL 파싱 함수, 위협 탐지 쿼리 등을 포함하며, 클라우드 보안 엔지니어와 SOC 분석가의 테스트와 기여를 모집하고 있습니다.

**English Summary**: An open-source project enables security teams to ingest AWS GuardDuty findings into Microsoft Sentinel with structured formatting and investigation-ready data. The repository provides dual ingestion options (managed and near-real-time), KQL parsing functions, threat queries, and deployment scripts, while seeking feedback from cloud security professionals and SOC analysts.

**핵심 키워드**: AWS GuardDuty, Microsoft Sentinel, EventBridge, Lambda, S3, SQS

### 5. [Docker 빌드에서 Kubernetes 배포까지: Ubuntu의 불변적 워크플로우](https://dev.to/jjoyneriv/from-docker-build-to-kubernetes-deploy-on-ubuntu-the-image-workflow-that-never-changed-d4f)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 글은 dockershim 논쟁 속에서 간과된 핵심을 강조한다: Docker로 이미지를 빌드하고 Kubernetes에서 실행하는 일상적 워크플로우는 변하지 않았다는 점이다. 멀티스테이지 Dockerfile, Docker buildx를 이용한 멀티 아키텍처 빌드, 그리고 프로덕션 환경의 Kubernetes Deployment 설정을 통해 Ubuntu 환경에서의 완전한 워크플로우를 제시한다.

**English Summary**: The article clarifies that despite the dockershim debate, the core workflow of building Docker images and running them on Kubernetes remains unchanged. It demonstrates a complete end-to-end workflow on Ubuntu using multi-stage Dockerfiles, Docker buildx for multi-architecture builds, and proper Kubernetes Deployment configurations with immutable image tags.

**핵심 키워드**: Docker, Kubernetes, Ubuntu, OCI, buildx, Dockerfile, distroless

### 6. [Oracle RMAN 복구 실행 가이드: 복원, 복구, 검증](https://dev.to/uptimearchitect/oracle-rman-recovery-runbook-restore-recover-prove-it-50mo)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: Oracle DBA를 위한 실무 가이드로, 데이터베이스 장애 복구 시 RESTORE와 RECOVER의 차이를 명확히 하고 각 장애 유형별 대응 방법을 제시합니다. Oracle 19c를 기준으로 손상된 블록 복구부터 특정 시점으로의 롤백까지 다양한 복구 시나리오를 다룹니다. 핵심은 백업 계획을 사전에 검증하는 것입니다.

**English Summary**: A practical runbook for Oracle DBAs covering database recovery procedures, emphasizing the critical distinction between RESTORE (copying datafiles from backups) and RECOVER (applying redo logs). The guide provides command sequences for various failure scenarios including point-in-time recovery, block media recovery, and controlfile restoration, targeting Oracle 19c with notes for newer versions.

**핵심 키워드**: Oracle 19c, RMAN, DBA, RESTORE, RECOVER, Point-in-Time Recovery
