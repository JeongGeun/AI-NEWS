---
layout: post
title: "2026-11-24 DevOps/인프라 데일리 브리핑"
date: 2026-11-24 00:07:00 +0900
categories: [devops]
tags:
  - Asterisk
  - B2B-intelligence
  - Caddy
  - DevOps
  - Git, npm, Python, Docker
  - HTTPS
  - Kubernetes
  - LinkedIn
  - Linux
  - Python
  - SPDY
  - SSL/TLS certificates
  - WebSocket
  - Zscaler, Cloudflare, Netskope
  - air-gapped environment
  - automation
  - b2b-sales
  - call recording
  - capabilities
  - configuration
---

> 수집 시각: 2026-11-24 05:25 UTC | 총 9건

## 뉴스 & 릴리즈

### 1. [쿠버네티스 v1.38 미리보기: 주요 변경사항 및 지원 중단 예정](https://kubernetes.io/blog/2026/11/23/kubernetes-v1-38-sneak-peek/)
**출처**: Kubernetes Blog · **중요도**: 보통

**한국어 요약**: 쿠버네티스 v1.38 릴리스를 앞두고 프로젝트 팀은 주요 변경사항을 공개했다. kubectl의 WebSocket 옵트아웃 환경변수가 제거되며, kuberc 자격증명 플러그인 허용목록 항목에서 'name' 필드가 삭제된다. 사용자는 사전에 스크립트와 CI 환경을 업데이트하여 호환성을 유지해야 한다.

**English Summary**: Kubernetes v1.38 release introduces deprecations and removals, including the removal of WebSocket opt-out environment variables (KUBECTL_REMOTE_COMMAND_WEBSOCKETS and KUBECTL_PORT_FORWARD_WEBSOCKETS) and changes to kuberc credential plugin allowlist entries. These changes reflect the project's transition from SPDY to WebSockets as the default protocol.

**핵심 키워드**: Kubernetes v1.38, kubectl, WebSockets, SPDY, KEP-4006, kuberc

## 커뮤니티

### 1. [OpenZeppelin Defender 종료 후 모니터링 마이그레이션 체크리스트](https://dev.to/kris_b_554ee86e9d618c204a/moving-off-openzeppelin-defender-a-checklist-for-your-monitors-2mhi)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: OpenZeppelin이 2026년 7월 1일 Defender 호스팅 서비스를 중단했다. 스마트 계약 모니터링을 위해 자체 서버에서 오픈소스 Monitor와 Relayer를 운영하거나 호스팅 서비스로 전환할 수 있다. 기존 모니터 설정을 수집하고 요구사항에 맞는 솔루션을 선택하여 마이그레이션을 완료해야 한다.

**English Summary**: OpenZeppelin retired its hosted Defender service on July 1, 2026, requiring teams to migrate their smart contract monitors. Teams can either self-host the open-source Monitor and Relayer or switch to alternative hosted services based on their monitoring needs and infrastructure requirements.

**핵심 키워드**: OpenZeppelin, Defender, Monitor, Relayer

### 2. [폐쇄형 네트워크 서비스 데스크를 위한 티켓 관리 솔루션 선택](https://dev.to/aurejaalkan/choosing-ticket-management-for-an-air-gapped-service-desk-59di)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 본 가이드는 외부 네트워크 연결 없이 완전히 오프라인에서 운영되는 폐쇄형 서비스 데스크를 위한 티켓 관리 도구 5가지를 비교합니다. ONES.com, GLPI, Zammad 등 각 도구의 배포 방식, AI 에이전트 지원 여부, 오프라인 운영 가능성을 세 가지 실용적 기준으로 평가하여 조직의 네트워크 제약 조건에 맞는 최적의 솔루션 선택을 돕습니다.

**English Summary**: This guide compares five ticket management tools designed for air-gapped service desks that operate without external network connectivity. The comparison evaluates solutions based on offline capability, ticket workflow processes, and integration with asset/inventory management, helping teams select the right tool based on their specific network constraints and operational needs.

**핵심 키워드**: ONES.com, GLPI, Zammad, air-gapped service desk, ticket management

### 3. [Asterisk 통화 녹음 저장소 관리: 보안과 보존](https://dev.to/muhammadalimughal/asterisk-call-recording-storage-retention-encryption-1f1m)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Asterisk PBX 시스템의 통화 녹음 저장 문제를 해결하기 위한 실무 가이드입니다. MixMonitor로 로컬 디스크에 녹음한 후 압축, 암호화, 클라우드 스토리지 업로드 및 자동 삭제 정책을 적용하는 아키텍처를 제시합니다. 보안, 용량 관리, 규정 준수를 종합적으로 고려한 설계 방식을 다룹니다.

**English Summary**: A practical guide for managing Asterisk call recording storage securely and efficiently. The article recommends recording with MixMonitor locally, then post-processing files through compression, encryption, cloud upload, and enforcing retention policies with lifecycle rules and signed URLs for playback.

**핵심 키워드**: Asterisk, FreePBX, MixMonitor, Loop Origin, PBX, object storage

### 4. [회사 Mac에서 Zscaler 등 보안 게이트웨이의 SSL 인증서 오류 해결법](https://dev.to/swgbar/fix-unable-to-get-local-issuer-certificate-x509-ssl-errors-on-mac-behind-zscaler-netskope--36gl)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 회사 관리형 MacBook에서 Git, npm, Python, Docker 등 개발 도구들이 SSL 인증서 오류를 발생시키는 문제를 다룬다. 기업의 Secure Web Gateway(Zscaler, Cloudflare, Netskope 등)가 macOS 시스템 키체인에 루트 CA를 주입하지만 개발 런타임은 별도의 CA 번들을 사용하기 때문이다. 오류 원인 파악 및 해결 방법을 단계별로 설명한다.

**English Summary**: This tutorial addresses SSL certificate errors that occur on company-managed MacBooks when using developer tools like Git, npm, Python, and Docker. The issue arises because corporate Secure Web Gateways (Zscaler, Cloudflare, Netskope, etc.) inject root CAs into macOS System Keychain, while developer runtimes use isolated CA bundles. The article provides step-by-step identification and troubleshooting methods, including a free corporate SWG decoder tool.

**핵심 키워드**: Zscaler, Cloudflare Gateway, Netskope, Cisco Umbrella, Palo Alto Prisma Access, Fortinet, macOS System Keychain

### 5. [Python과 n8n으로 B2B 리드 자동화 구축하기](https://dev.to/deepak_sheoran_4754c2e34c/how-to-automate-b2b-lead-domain-intelligence-suite-in-2026-with-python-n8n-2692)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 튜토리얼은 Python과 n8n을 활용하여 B2B 리드 도메인 인텔리전스 스위트의 데이터 추출, 파싱, 모니터링을 자동화하는 방법을 설명합니다. 수동 데이터 처리의 비효율성을 해결하고 클라우드 마이크로서비스를 통해 자동화된 비즈니스 파이프라인을 구축하는 과정을 다룹니다.

**English Summary**: This tutorial demonstrates how to automate B2B lead domain intelligence data extraction, parsing, and monitoring using Python and n8n. It addresses the inefficiencies of manual data processing and provides guidance on building deterministic cloud microservices for automated business pipelines.

**핵심 키워드**: Python, n8n, B2B Lead Intelligence, data extraction, cloud microservices

### 6. [Python과 n8n으로 LinkedIn 기업 정보 수집 자동화하기](https://dev.to/deepak_sheoran_4754c2e34c/how-to-automate-linkedin-public-company-profiler-in-2026-with-python-n8n-24dm)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 튜토리얼은 Python과 n8n을 활용하여 LinkedIn 공개 기업 정보, 채용 공고, 이메일 추출 등 다양한 B2B 리드 수집 작업을 자동화하는 방법을 소개합니다. 클라우드 마이크로서비스를 이용한 데이터 추출 자동화로 수동 작업의 오류와 비용을 줄일 수 있습니다.

**English Summary**: This tutorial demonstrates how to automate LinkedIn data extraction, B2B lead intelligence, and contact information gathering using Python and n8n. It covers setting up cloud microservices for automated data processing, eliminating manual extraction errors and reducing operational costs.

**핵심 키워드**: n8n, Python, LinkedIn, B2B lead generation, web scraping, data extraction

### 7. [Caddy 웹 서버로 쇼핑몰 사이트 운영하기](https://dev.to/practicaldevblog/caddy-web-server-tutorial-serve-a-shop-site-in-minutes-16)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Go로 작성된 Caddy 웹 서버는 짧은 설정 파일(Caddyfile)로 정적 파일 제공과 백엔드 리버스 프록시를 동시에 처리할 수 있다. NGINX 대비 간단한 설정으로 같은 작업을 수행하며, HTTPS 인증서를 자동으로 관리한다. 카라치 직물점 사례를 통해 localhost 환경에서 실제 작동을 검증한다.

**English Summary**: Caddy is a Go-based web server that simplifies hosting static sites and proxying backend APIs through a minimal configuration file (Caddyfile), offering simpler syntax than NGINX. The tutorial demonstrates running a Karachi fabric shop's website and orders API on localhost, highlighting Caddy's config validation and automatic HTTPS management capabilities.

**핵심 키워드**: Caddy, NGINX, Caddyfile, Go, HTTPS

### 8. [Linux 권한 기능(Capabilities)으로 Root 권한 최소화하기](https://dev.to/lyraalishaikh/stop-running-as-root-for-one-port-practical-linux-capabilities-5)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 웹 서비스가 포트 80에 바인딩하기 위해 Root 권한으로 실행되는 관행을 개선하는 방법을 설명합니다. Linux Capabilities 메커니즘을 사용하면 Root의 모든 권한 대신 필요한 최소한의 권한(CAP_NET_BIND_SERVICE 등)만 프로세스에 부여할 수 있습니다. 파일에는 설정되었지만 프로세스의 effective set에 도달하지 못하는 간극을 해소하는 방법을 다룹니다.

**English Summary**: This tutorial explains how to use Linux Capabilities to run web services with minimal privileges instead of full root access. Rather than granting all kernel privileges to bind port 80, administrators can assign specific capabilities like CAP_NET_BIND_SERVICE. The article addresses the common gap between setting file capabilities and ensuring they reach the process's effective privilege set.

**핵심 키워드**: Linux Capabilities, CAP_NET_BIND_SERVICE, setcap, getcap, privilege bits, kernel 6.12
