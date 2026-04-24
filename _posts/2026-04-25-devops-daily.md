---
layout: post
title: "2026-04-25 DevOps/인프라 데일리 브리핑"
date: 2026-04-25 00:07:00 +0900
categories: [devops]
tags:
  - 2026 tools
  - AI SRE
  - AI-assisted
  - AWS
  - Architecture Diagram
  - CloudFormation
  - DPI
  - DevOps Tool
  - FIPS
  - GitLab
  - HTTPS
  - Infrastructure as Code
  - Kubernetes
  - Linux namespaces
  - SNI
  - TLS
  - Visualization
  - ai-agents
  - automation
  - autonomous agents
---

> 수집 시각: 2026-04-24 22:16 UTC | 총 10건

## 뉴스 & 릴리즈

### 1. [GitLab 19.0, FIPS 패키지에서 curl 제거](https://about.gitlab.com/blog/curl-removed-from-omnibus-gitlab-fips-packages-in-19-0/)
**출처**: GitLab Blog · **중요도**: 보통

**한국어 요약**: GitLab은 Omnibus-GitLab 19.0부터 FIPS 패키지에서 자체 구축 curl을 제거하고 Linux 배포판이 제공하는 curl을 사용하기로 결정했습니다. 이는 curl 8.18.0이 OpenSSL 1.x 컴파일을 더 이상 지원하지 않아 Amazon Linux 2와 AlmaLinux 8에서 호환성 문제가 발생했기 때문입니다. 변경 후 GitLab은 curl 보안 업데이트 책임을 더 이상 지지 않습니다.

**English Summary**: GitLab will remove the bundled curl from Omnibus-GitLab 19.0 FIPS packages, replacing it with the distribution-provided curl, similar to how it already handles OpenSSL. This change is driven by curl 8.18.0's deprecation of OpenSSL 1.x compilation support, affecting Amazon Linux 2 and AlmaLinux 8 customers. GitLab will no longer be responsible for shipping curl security updates starting with version 19.0.

**핵심 키워드**: GitLab, Omnibus-GitLab, FIPS, curl, OpenSSL, Amazon Linux 2, AlmaLinux 8

### 2. [Kubernetes v1.36: 사용자 네임스페이스 기능 정식 출시](https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/)
**출처**: Kubernetes Blog · **중요도**: 높음

**한국어 요약**: Kubernetes v1.36에서 사용자 네임스페이스(User Namespaces) 기능이 정식 출시(GA)되었습니다. 이는 Linux 전용 기능으로, 컨테이너 내 root 권한을 호스트의 root와 분리하여 보안을 강화합니다. hostUsers: false 설정으로 CAP_NET_ADMIN 같은 권한을 네임스페이스 범위로 제한할 수 있어, 호스트에 영향을 주지 않으면서도 권한있는 워크로드 실행이 가능해집니다.

**English Summary**: Kubernetes v1.36 officially released User Namespaces support for Linux workloads, a major security milestone after years of development. The feature isolates process identity by making root inside containers invisible to the host kernel, preventing privilege escalation attacks. When enabled with hostUsers: false, capabilities like CAP_NET_ADMIN become namespaced, enabling secure privileged workloads without full container privilege.

**핵심 키워드**: Kubernetes v1.36, User Namespaces, hostUsers, ID-mapped mounts, Linux kernel

## 커뮤니티

### 1. [CloudFormation 다이어그램 생성기로 AWS 템플릿 시각화](https://dev.to/pandey-raghvendra/cloudformation-diagram-generator-visualize-aws-templates-instantly-4038)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: InfraSketch가 CloudFormation 지원을 추가했다. 사용자가 CloudFormation YAML 또는 JSON 템플릿을 붙여넣으면 브라우저에서 즉시 아키텍처 다이어그램을 생성한다. 로그인 없이 모든 처리가 클라이언트에서 실행되며, CloudFormation의 !Ref, !GetAtt, !Sub 등의 단축 구문을 완벽히 지원한다.

**English Summary**: InfraSketch now supports CloudFormation templates, allowing users to paste YAML/JSON templates and instantly generate clean architecture diagrams in the browser. The tool handles CloudFormation's custom YAML intrinsic functions by registering custom types before parsing, eliminating manual visualization work.

**핵심 키워드**: InfraSketch, AWS CloudFormation, AWS, IaC

### 2. [계층 기반 접근법으로 21개 서비스 마이그레이션 자동화](https://dev.to/svasylenko/layers-made-it-universal-harnesses-made-it-run-2307)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: ECS에서 EKS로 21개 서비스를 마이그레이션하는 8분기 프로젝트에서 '하네스'라는 프롬프트 파이프라인을 개발했다. 각 계층은 스크립트 기반 결정론적 변경, AI 기반 발견 및 적응, 검증 단계로 구성되어 있으며, 이를 통해 동일한 변경을 다양한 저장소 구조에 동시에 적용할 수 있었다.

**English Summary**: A team developed a 'harness' prompt pipeline to automate the migration of 21 microservices from ECS to EKS. The harness chains deterministic scripts, AI-driven discovery, and validation across each layer, enabling identical changes to be executed across diverse snowflake repositories simultaneously while landing merge requests automatically.

**핵심 키워드**: ECS, EKS, prompt pipeline, harness, microservices, multi-service migration

### 3. [2026년 엔지니어링 팀을 위한 AI SRE 완벽 가이드](https://dev.to/siddharth_singh_409bd5267/ai-sre-the-complete-guide-for-engineering-teams-in-2026-51ba)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: AI SRE는 인적 지시 없이 자율적으로 알람 분류, 인시던트 조사, 근본 원인 분석, 사후분석을 수행하는 AI 에이전트다. 가트너는 2029년까지 엔터프라이즈의 70%가 에이전틱 AI를 IT 인프라 운영에 배포할 것으로 예측했다. 2026년에는 마이크로소프트의 Azure SRE Agent와 K8sGPT, HolmesGPT 등 오픈소스 솔루션들이 본격적으로 출현했다.

**English Summary**: An AI SRE is an autonomous AI agent that performs site reliability engineering tasks including alert triage, incident investigation, and root cause analysis without human step-by-step direction. Gartner projects 70% of enterprises will deploy agentic AI for IT infrastructure by 2029, up from under 5% in 2025. Commercial solutions like Microsoft's Azure SRE Agent and open-source alternatives such as K8sGPT gained traction in 2026.

**핵심 키워드**: Microsoft Azure SRE Agent, Komodor, Gartner, K8sGPT, HolmesGPT, Aurora

### 4. [다중 서비스 마이그레이션: 서비스별이 아닌 단계별 병렬 처리 전략](https://dev.to/svasylenko/flip-the-axis-a-layer-based-approach-to-multi-service-migrations-3a5d)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 21개의 ECS 서비스를 EKS로 마이그레이션해야 하는 상황에서 서비스별 직렬 처리 대신 단계별 병렬 처리 방식을 제안한다. 모든 서비스에 동일한 변경을 한 번에 적용하면 학습이 누적되고 불일치를 조기에 발견할 수 있으며 자동화가 가능해진다. 다만 아키텍처가 고유한 서비스는 별도로 직렬 처리해야 한다.

**English Summary**: This article proposes a layer-based approach to large-scale service migrations where teams parallelize by step rather than by service. By sweeping one type of change across all services before moving to the next phase, organizations can compound learning, catch inconsistencies early, and enable automation—while still handling architecturally unique services separately.

**핵심 키워드**: ECS, EKS, Kubernetes, AWS, service migration

### 5. [HTTPS 트래픽이 차단되는 이유와 DPI 우회 방식](https://dev.to/alanwest/why-your-https-traffic-still-gets-blocked-and-how-dpi-evasion-works-476l)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: HTTPS는 페이로드를 암호화하지만 TLS 핸드셰이크의 SNI(Server Name Indication) 필드는 평문으로 전송되어 네트워크 관찰자가 접속 대상 도메인을 확인할 수 있다. DPI(Deep Packet Inspection) 어플라이언스는 이 메타데이터를 검사하여 차단 목록과 매칭 후 연결을 종료한다. 개발자들은 DNS 쿼리 등 다양한 메타데이터가 DPI에 의해 추적될 수 있음을 이해해야 한다.

**English Summary**: Although HTTPS encrypts payload data, the SNI field in TLS handshakes is sent in plaintext, allowing network observers to identify the destination domain. DPI appliances exploit this by inspecting SNI metadata, matching it against blocklists, and dropping connections before encryption is established. Understanding these mechanisms helps developers troubleshoot connections blocked by restrictive corporate firewalls.

**핵심 키워드**: Deep Packet Inspection (DPI), SNI (Server Name Indication), TLS handshake, corporate firewall

### 6. [AI 에이전트의 숨겨진 데이터 손상 문제와 모니터링 한계](https://dev.to/nathanielc85523/40-cents-a-day-three-weeks-of-corrupted-writes-zero-alerts-fired-54i0)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 3주간 실행된 크론 작업이 데이터를 손상시켰지만 비용 대시보드에는 아무것도 나타나지 않았다. 문제는 현재의 모니터링 도구가 '비용'만 추적하고 '에이전트의 행동', '권한 여부', '올바른 동작 중단'을 감지하지 못한다는 것이다. OpenTelemetry LLM 의미론적 관례가 중첩된 에이전트 트리 구조를 제대로 모델링하지 못하는 스키마 갭이 근본 원인이다.

**English Summary**: A corrupted cron job ran undetected for three weeks, causing data damage while costing only 40 cents daily—invisible to cost dashboards. The root issue: monitoring tools only track spending, not whether agents are performing authorized actions correctly. OpenTelemetry's LLM semantic conventions lack native support for agent trees, sessions, and depth tracking needed to catch such issues.

**핵심 키워드**: OpenTelemetry, LLM semantic conventions, ClickHouse, agent tree, session grain

### 7. [Kubernetes vs Docker Swarm: 컨테이너 오케스트레이션 플랫폼 선택 가이드](https://dev.to/raghav_sharma_0c5d39f61a9/kubernetes-vs-docker-swarm-which-one-should-you-choose-302a)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 본 글은 컨테이너 관리를 위한 두 주요 오케스트레이션 도구인 Kubernetes와 Docker Swarm을 비교 분석한다. Kubernetes는 Google이 개발한 오픈소스 플랫폼으로 대규모 복잡한 애플리케이션 관리에 우수하며, 자동 배포, 자가 치유, 고급 네트워킹 등의 기능을 제공한다. 팀의 요구사항과 기술 수준에 따라 적절한 플랫폼을 선택해야 한다.

**English Summary**: This article compares Kubernetes and Docker Swarm, two major container orchestration platforms. Kubernetes, developed by Google, excels at managing large-scale, complex containerized applications with features like automated deployment, self-healing, and advanced networking. The choice between platforms depends on team requirements: Kubernetes suits enterprises needing high availability and flexibility, while Docker Swarm is preferred for simpler setups.

**핵심 키워드**: Kubernetes, Docker Swarm, Google, container management, microservices

### 8. [실제로 읽히는 저장소별 위키 구축하기](https://dev.to/vineethnkrishnan/building-a-per-repo-wiki-that-actually-gets-read-1kca)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발팀의 문서가 README, 내부 폴더, CI/CD 주석에 분산되어 있어 한 팀원이 지속적으로 질문하는 병목 현상이 발생했다. 이를 해결하기 위해 각 저장소에 wiki/ 폴더를 추가하고 PR 검토 후 자동 동기화하는 시스템을 도입했다. 핵심은 도구보다 '질문에 답한 후 문서화하기'라는 팀 문화 변화였다.

**English Summary**: A development team discovered their documentation was scattered across READMEs, internal folders, and CI/CD comments, causing one teammate to become a knowledge bottleneck. They implemented a per-repo wiki system with a wiki/ folder that auto-syncs to GitHub on merges, combined with a cultural shift of documenting answers immediately after providing them. The technical implementation was straightforward; changing team habits proved to be the real challenge.

**핵심 키워드**: GitHub Wiki, CI/CD automation, documentation strategy
