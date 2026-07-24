---
layout: post
title: "2026-07-25 DevOps/인프라 데일리 브리핑"
date: 2026-07-25 00:07:00 +0900
categories: [devops]
tags:
  - AI safety
  - API
  - CI/CD
  - CISO governance
  - ClickHouse
  - IP allowlisting
  - SMS testing
  - SharePoint
  - agentic AI
  - aks
  - azure
  - browser-testing
  - cloud infrastructure
  - cloud-infrastructure
  - container-orchestration
  - containerization
  - database optimization
  - devops
  - devops-tool
  - email verification
---

> 수집 시각: 2026-07-24 22:40 UTC | 총 10건

## 튜토리얼 & 아티클

### 1. [Supabase, Grafana Cloud 통합으로 원클릭 모니터링 실현](https://grafana.com/blog/grafana-cloud-supabase-one-click-integration/)
**출처**: Grafana Blog · **중요도**: 보통

**한국어 요약**: Supabase와 Grafana Labs가 파트너십을 통해 Supabase 대시보드에서 직접 Grafana Cloud를 활성화할 수 있는 통합을 출시했다. 사용자는 단 한 번의 클릭으로 쿼리 성능, 데이터베이스 상태 등 핵심 지표를 모니터링할 수 있으며, 미리 구성된 대시보드로 즉시 시스템 상태를 파악할 수 있다.

**English Summary**: Supabase and Grafana Labs launched a one-click integration enabling Supabase users to activate Grafana Cloud directly from their dashboard for production-grade observability. The out-of-the-box dashboard provides immediate visibility into Postgres metrics, query performance, and system health for applications built on Supabase.

**핵심 키워드**: Supabase, Grafana Labs, Grafana Cloud, Postgres, Matthew Linkous

### 2. [Grafana Cloud IP 허용 목록 새로운 설계 안내](https://grafana.com/blog/a-new-allowlists-design-for-grafana-cloud-ip-addresses-what-you-need-to-know/)
**출처**: Grafana Blog · **중요도**: 보통

**한국어 요약**: Grafana는 기존의 제품별 IP 주소 목록을 단일 구조화된 API로 통합하는 새로운 허용 목록 설계를 발표했습니다. 레거시 형식(JSON, TXT, DNS 레코드)은 2027년 1월 31일까지 유지되어 마이그레이션 기간을 제공합니다. IP 허용 목록을 사용하지 않거나 PrivateLink 같은 프라이빗 연결을 사용하는 사용자는 영향을 받지 않습니다.

**English Summary**: Grafana is consolidating its fragmented per-product IP address allowlists into a single, unified API endpoint. The legacy formats will remain functional until January 31, 2027, providing organizations time to migrate their firewall configurations and automations. Users relying on private connectivity options will experience no changes.

**핵심 키워드**: Grafana Cloud, Grafana Labs, allowlists API

## 뉴스 & 릴리즈

### 1. [에이전트 AI 보안: 추측이 아닌 체계적 보호 필요](https://www.docker.com/blog/agentic-ai-needs-guardrails-not-guesswork/)
**출처**: Docker Blog · **중요도**: 높음

**한국어 요약**: 엔터프라이즈 환경에서 AI 에이전트의 빠른 확산으로 CISO들이 생산성과 보안 사이의 균형을 맞춰야 하는 과제에 직면했다. Docker 블로그의 패널 토론에서 전문가들은 AI 에이전트를 안전하게 운영하기 위해 격리된 환경, 통제, 관찰이 필수적이라고 강조했다. 개발자들의 승인 없는 무분별한 AI 도구 사용을 제어하면서도 기술의 생산성 이점을 활용할 수 있는 거버넌스 체계의 필요성이 제기되었다.

**English Summary**: Enterprise security leaders face a critical challenge balancing AI agent productivity benefits with security risks, as developers increasingly adopt these tools without proper governance. A Docker panel discussion featuring CISO experts emphasizes that safely deploying agentic AI requires isolated environments, strict controls, and comprehensive observability to prevent vulnerabilities while maintaining developer velocity.

**핵심 키워드**: Docker, Warp, NanoCo, NanoClaw, Moriah Hara

## 커뮤니티

### 1. [Azure Kubernetes Service(AKS)에서 Kubernetes 애플리케이션 배포하기](https://dev.to/awokay/deploying-a-kubernetes-application-on-azure-kubernetes-service-aks-from-cluster-creation-to-live-3f97)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 글은 Azure Kubernetes Service(AKS)에서 Kubernetes 클러스터를 처음부터 생성하고 애플리케이션을 배포하는 단계별 가이드를 제공한다. 리소스 그룹 생성, AKS 클러스터 프로비저닝, 자격증명 설정, 노드 연결 확인, 애플리케이션 배포 등 5단계의 실무 절차를 PowerShell과 kubectl 명령어로 설명한다.

**English Summary**: This tutorial provides a step-by-step guide for deploying Kubernetes applications on Azure Kubernetes Service (AKS), covering resource group creation, cluster provisioning, credential configuration, node verification, and application deployment. The article uses practical PowerShell and kubectl commands to walk through each deployment stage from cluster setup to live application running.

**핵심 키워드**: Azure Kubernetes Service, Kubernetes, PowerShell, kubectl, VS Code

### 2. [브라우저 테스트의 진정한 난제는 브라우저 밖에 있다](https://dev.to/randomsquirrel802/the-hardest-browser-tests-live-outside-the-browser-afi)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 엔드-투-엔드 브라우저 테스트의 핵심 어려움은 클릭 명령이 아니라 이메일 인증, SMS 검증, 파일 업로드 등 외부 시스템과의 통합 조율에 있다. 이메일 지연, SMS 제한, 링크 만료, 병렬 테스트 간 충돌 등 분산 시스템의 장애 모드를 처리하는 것이 안정적인 테스트 슈트 구축의 장기적 비용을 결정한다.

**English Summary**: End-to-end browser testing's real challenge lies in orchestrating external systems like email verification and SMS codes, not in browser automation itself. Teams must account for distributed system failures including email delays, SMS throttling, link expiration, and timestamp mismatches across parallel tests.

**핵심 키워드**: Mailgun, IMAP, Twilio

### 3. [SharePoint 2016/2019 지원 종료 8일 후 최종 보안 패치 이후 중대 취약점 발견](https://dev.to/endoflifeai/the-next-sharepoint-98-arrived-in-eight-days-and-it-was-the-last-one-with-a-patch-3db0)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 2026년 7월 14일 SharePoint Server 2016과 2019가 확장 지원을 종료하고 마지막 보안 업데이트를 받았다. 8일 후인 7월 22일 CVSS 9.8 등급의 역직렬화 취약점(CVE-2026-50522)이 발견되어 공개 익스플로잇이 유포되고 실제 악용이 시작되었다. 중요한 점은 이 취약점이 7월 14일 업데이트에 포함된 마지막 패치로, 향후 모든 SharePoint 취약점은 2016/2019 버전에 대한 수정이 없다는 것이다.

**English Summary**: On July 14, 2026, SharePoint Server 2016 and 2019 reached end-of-extended-support and received their final security updates. Just 8 days later, a critical CVSS 9.8 deserialization vulnerability (CVE-2026-50522) with remote code execution was disclosed and actively exploited. This patch was the last one these versions will ever receive, meaning all future SharePoint vulnerabilities will go unfixed for 2016 and 2019 deployments.

**핵심 키워드**: SharePoint Server 2016, SharePoint Server 2019, CVE-2026-50522, CISA, Microsoft

### 4. [느려지는 테스트 스위트의 진짜 원인](https://dev.to/mellowthunder735/your-test-suite-isnt-slow-its-accumulating-decisions-5080)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 브라우저 테스트 스위트가 느려지는 것은 한 번의 급격한 실패가 아니라 작은 기술적 결정들이 누적된 결과다. 애니메이션 동작 차이, 기능 플래그, 병렬 처리 설정 등 여러 요소가 쌓이면서 신뢰도 부채(reliability debt)가 형성된다. 테스트가 CI 환경과 로컬 환경에서 다르게 동작하는 것은 환경이 동등하지 않기 때문이며, 이를 해결하려면 아키텍처 수준의 접근이 필요하다.

**English Summary**: Test suite slowdowns are caused by accumulated technical decisions rather than inherent flakiness. Common issues include environment differences between local and CI, animation behavior variations, and misaligned assertions that test implementation details instead of user outcomes. The test environment is part of the product design and must be treated as such.

**핵심 키워드**: browser-test-suites, CI-environment, reliability-debt, test-flakiness

### 5. [VPS 보안 감시 도구 vpsguard 개발기](https://dev.to/salamancacm/i-kept-seeing-weird-stuff-on-my-vps-so-i-built-a-tool-to-stop-guessing-50cn)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자가 VPS 인스턴스에서 설명할 수 없는 보안 문제를 감지한 후, 경량의 Linux 서버 감시 및 강화 도구인 vpsguard를 개발했다. Go 기반의 단일 바이너리로 SSH 설정, 방화벽, 의심스러운 계정, 암호화 키 관리 등 12가지 보안 검사를 수행하고 실시간으로 변화를 감시한다.

**English Summary**: A developer created vpsguard, a lightweight Go-based tool to audit, harden, and monitor Linux VPS instances after encountering unexplained security anomalies. The tool performs 12 security checks including SSH configuration, firewall settings, suspicious accounts, and unauthorized SSH key additions, with all remediations being idempotent and config backups automatically created.

**핵심 키워드**: vpsguard, Go, Linux, SSH, Ubuntu, AWS EC2 IMDSv1

### 6. [유휴 ClickHouse, 30초마다 1100만 행 병합 중](https://dev.to/otezvikentiy/my-idle-clickhouse-was-merging-11-million-rows-every-30-seconds-2d4i)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 저사양 VPS에서 실행 중인 ClickHouse 데이터베이스가 과도한 메모리와 디스크를 소비하고 있었다. 조사 결과 실제 애플리케이션 데이터는 543KB에 불과했지만, ClickHouse의 시스템 로그(trace_log, asynchronous_metric_log, text_log 등)가 TTL 설정이 없어 579MB까지 증가해 있었다. 이는 데이터베이스가 자신의 로그 관리에 막대한 I/O 자원을 소비하는 사례를 보여준다.

**English Summary**: A ClickHouse database on a resource-constrained VPS was consuming excessive memory and disk space despite minimal ingested data (543KB of actual telemetry). System logs with no TTL (trace_log, asynchronous_metric_log, text_log) had grown to 579MB, demonstrating how databases can spend most I/O resources managing their own internal logging instead of query processing.

**핵심 키워드**: ClickHouse, trace_log, asynchronous_metric_log, TTL configuration

### 7. [한화비전 카메라에서 깃허브 관리자 토큰 유출](https://dev.to/lu1tr0n/camaras-hanwha-filtraban-un-token-de-github-con-acceso-admin-4c65)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 보안 연구자가 한화비전 카메라의 펌웨어에서 약 30개 파일에 중복 저장된 깃허브 관리자 토큰을 발견했다. 이 토큰은 회사의 수백 개 프라이빗 저장소에 대한 관리자 권한을 가지고 있으며, 카메라 관리 패널의 자바스크립트 번들에 평문으로 포함되어 있었다. 패널에 접근 가능한 누구나 토큰을 추출할 수 있는 심각한 보안 취약점이다.

**English Summary**: A security researcher discovered a GitHub admin token embedded in Hanwha Vision camera firmware, duplicated across approximately 30 files. The token had administrative access to hundreds of private company repositories and was plaintext in the JavaScript bundle served by the camera's admin interface, making it accessible to anyone with panel access.

**핵심 키워드**: Hanwha Vision, GitHub, security researcher, firmware
