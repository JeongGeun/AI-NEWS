---
layout: post
title: "2026-11-15 DevOps/인프라 데일리 브리핑"
date: 2026-11-15 00:07:00 +0900
categories: [devops]
tags:
  - AWS
  - CI/CD
  - CISA guidelines
  - DevOps
  - DevOps platform
  - External Secrets Operator
  - FAA
  - Infrastructure
  - Infrastructure as Code
  - Kubernetes
  - Product Launch
  - SBOM
  - SaaS security
  - SecretStore
  - Terraform
  - air traffic control
  - automation
  - backoff retry
  - compliance
  - compliance tool
---

> 수집 시각: 2026-11-15 01:08 UTC | 총 8건

## 커뮤니티

### 1. [소프트웨어 부품명세서(SBOM) 요청 도구 무료 공개](https://dev.to/circuitsfit/free-tool-sbom-request-pack-8k2)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 소프트웨어 부품명세서(SBOM)는 소프트웨어의 구성 요소, 공급자, 버전 및 의존성을 나열한 목록입니다. CISA, NSA, FBI가 2026년 최소 요소 지침을 발표했으며, 모든 소프트웨어와 AI, SaaS 등 특정 유형에 적용됩니다. circuits.fit에서 제공하는 무료 브라우저 도구를 사용해 공급업체의 SBOM을 요청하고 확인할 수 있습니다.

**English Summary**: A free browser-based tool on circuits.fit helps buyers request and track Software Bill of Materials (SBOM) from vendors. CISA, NSA, and FBI released updated SBOM minimum elements in 2026 that now apply to all software including SaaS and AI products, enabling faster vulnerability impact assessment compared to traditional questionnaire processes.

**핵심 키워드**: CISA, NSA, FBI, circuits.fit, NTIA, SBOM

### 2. [SecretStore 지연 시 ExternalSecret의 백오프 재시도 동작](https://dev.to/whenitruns/when-an-externalsecret-runs-on-backoff-behind-a-late-secretstore-jmf)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: External Secrets Operator v2.11.0에서 SecretStore가 준비되지 않았을 때 ExternalSecret의 첫 번째 동기화 동작을 분석한 보고서입니다. refreshInterval 설정과 무관하게 1, 4, 8, 16초 간격으로 최대 7분까지 지수 백오프 방식으로 재시도되며, 다음 재시도 시점에 동기화된다는 것을 확인했습니다.

**English Summary**: This report examines how External Secrets Operator v2.11.0 handles the first sync of an ExternalSecret when its SecretStore is not ready. The operator retries with exponential backoff (1, 4, 8, 16... seconds) up to 7 minutes, independent of the refreshInterval setting, syncing at the next retry attempt.

**핵심 키워드**: External Secrets Operator v2.11.0, ExternalSecret, SecretStore, exponential backoff

### 3. [소프트웨어 벤더에게 SBOM 요청하기](https://dev.to/circuitsfit/ask-a-vendor-for-an-sbom-3lhc)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: CISA의 2026년 최소 요소 기준이 SaaS 및 AI 소프트웨어에 적용된다. 소프트웨어 갱신 계약 담당자와 보안 검토 담당자를 위해 SBOM 요청 시 필수 필드, 형식, 생성 날짜를 명확히 요청해야 한다. PDF 슬라이드가 아닌 기계 판독 가능한 형식의 완전한 문서를 요구해야 한다.

**English Summary**: CISA's 2026 minimum elements for Software Bill of Materials (SBOM) now apply to all software including SaaS and AI products. When requesting an SBOM from vendors, procurement teams should specify required fields (component hash algorithm, license, generation tool, context), machine-readable format (CycloneDX or SPDX), generation date, and update frequency policies. A PDF slide or outdated document does not constitute a compliant SBOM.

**핵심 키워드**: CISA, SBOM (Software Bill of Materials), CycloneDX, SPDX, NTIA baseline

### 4. [사이트 운영자를 위한 무료 보안 점검 15가지 도구 모음](https://dev.to/toolsphare/a-free-website-and-security-check-up-kit-15-tools-for-site-owners-and-it-teams-271b)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자와 IT팀을 위한 무료 웹사이트 점검 도구 15개를 소개하는 글입니다. SSL 인증서 만료, DNS 설정 오류, 이메일 스팸 필터링 문제 등 소규모 비즈니스와 개발자들이 자주 놓치는 사항들을 방지하기 위해 브라우저에서 바로 사용할 수 있는 무료 도구들을 제공합니다. 도메인/DNS, HTTPS/HTTP 동작 확인, 보안 점검 등 카테고리별로 정리된 실용적인 점검 도구 모음입니다.

**English Summary**: This article presents a free website check-up kit of 15 browser-based tools for site owners and IT teams to prevent common failures like SSL certificate expiration, DNS propagation issues, and email deliverability problems. The tools are organized by category including domain/DNS lookup, SSL certificate checking, and HTTP behavior verification, requiring no signup or paid subscriptions.

**핵심 키워드**: ToolSphare, Muhammad Wasim, WHOIS lookup, DNS Record Lookup, SSL Certificate Checker

### 5. [AWS에서 Terraform을 이용한 Infrastructure as Code 구현](https://dev.to/kestronai/infrastructure-as-code-with-terraform-on-aws-33gm)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: Infrastructure as Code(IaC)는 클라우드 리소스를 콘솔 클릭 대신 텍스트 파일로 정의하는 방식이며, Terraform은 가장 널리 사용되는 도구입니다. IaC를 통해 모든 변경사항이 Git으로 추적되고, 환경을 처음부터 재구성할 수 있습니다. 원격 상태 관리, 환경별 분리된 상태, 재사용 가능한 모듈, CI/CD 파이프라인 구성이 핵심입니다.

**English Summary**: Infrastructure as Code (IaC) enables defining cloud resources in text files rather than manual console clicks, with Terraform being the industry standard tool. This approach provides benefits like version control tracking, repeatability across environments, and disaster recovery capabilities. Best practices include remote state management, environment separation, modular code design, and CI/CD pipeline integration.

**핵심 키워드**: Terraform, AWS, Git, Infrastructure as Code, CI/CD

### 6. [래치키 6월 업데이트: 자가치유 CI 기본 활성화](https://dev.to/kalemi/latchkey-june-update-self-healing-ci-is-on-by-default-nm9)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: CI/CD 플랫폼 래치키가 자가치유(Self-Healing) 기능을 모든 조직에 기본으로 활성화했습니다. 이 기능은 환경 오류를 자동으로 진단·복구하고, Claude 에이전트를 통해 미분류 오류를 조사하며, 영구적 해결책을 풀 리퀘스트로 제안합니다. 대시보드에서 추세와 상세 보고서를 확인할 수 있으며, 한 번의 토글로 비활성화 가능합니다.

**English Summary**: Latchkey has enabled self-healing CI by default for all organizations, automatically diagnosing and repairing environment failures while routing unfamiliar issues to a Claude AI agent. The platform provides healing dashboards, pull requests for permanent fixes, and maintains a single toggle to disable the feature if needed.

**핵심 키워드**: Latchkey, Claude, self-healing CI, pull requests

### 7. [미국 항공기 대량 운항 중단 사건, 라우터 결함이 원인](https://dev.to/noahcontrolplane/every-theory-for-why-americas-planes-stopped-on-friday-the-13th-ranked-from-confirmed-to-ufos-4o09)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 2024년 11월 13일 미국 FAA가 전국 3,500여 대의 항공기 운항을 중단시킨 사건의 원인이 규명되었다. L3Harris 계약업체가 구리선을 광섬유로 교체하던 중 라우터가 오류를 일으켜 항공교통 제어 네트워크에 초당 1,000회 연결 시도를 보낸 것이 원인이었다. 이는 9/11 이후 두 번째 규모의 전국적 운항 중단 사건으로 기록되었다.

**English Summary**: On November 13, 2024, the FAA grounded all departing flights nationwide, affecting approximately 3,500 aircraft in a 5-hour ground stop. The official investigation confirmed that a contractor replacing copper wiring with fiber optics inadvertently deployed a malfunctioning router that flooded the air traffic control network with connection attempts, causing the system failure.

**핵심 키워드**: FAA, L3Harris, air traffic control network, router failure, Sean Duffy

### 8. [래치키 러너 정식 출시, CI/CD 인프라 자동화 솔루션](https://dev.to/kalemi/latchkey-may-update-latchkey-runners-are-live-4gl2)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자 플랫폼 래치키가 자동화된 CI/CD 러너 서비스를 정식 출시했다. 2~16 vCPU 규모의 4가지 인스턴스 옵션과 월 $5부터 시작하는 구독 플랜을 제공하며, 기존 GitHub 워크플로우와의 호환성을 유지한다. 저장소 스캔 기반 커스텀 러너 이미지 생성 기능으로 의존성 관리를 자동화할 수 있다.

**English Summary**: Latchkey launched its Runners service with four machine sizes (2-16 vCPU), GitHub-compatible base images, and subscription plans starting at $5/month with included runner minutes. The service features transparent caching, custom runner generation via repository scanning, and per-minute pricing for usage beyond included minutes.

**핵심 키워드**: Latchkey, Latchkey Runners, GitHub, Ubuntu 24.04
