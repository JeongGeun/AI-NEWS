---
layout: post
title: "2026-05-14 DevOps/인프라 데일리 브리핑"
date: 2026-05-14 00:07:00 +0900
categories: [devops]
tags:
  - AI Agents
  - AI deployment
  - AI-assisted development
  - CVE
  - CVSS
  - Deployment
  - DevOps
  - DevSecOps
  - Docker
  - Hermes Agent
  - Kubernetes
  - NIST
  - NVD
  - Nginx
  - OpenClaw
  - Podman
  - RabbitMQ
  - Self-hosted
  - Ubuntu
  - VPS
---

> 수집 시각: 2026-05-13 22:40 UTC | 총 14건

## 뉴스 & 릴리즈

### 1. [NIST, 국가 취약점 데이터베이스 범위 축소... 컨테이너 보안 재검토 필요](https://www.docker.com/blog/nist-narrows-the-nvd-what-container-security-programs-should-reassess/)
**출처**: Docker Blog · **중요도**: 높음

**한국어 요약**: NIST가 4월 15일 국가 취약점 데이터베이스(NVD)의 우선순위 강화 모델을 발표했다. 대부분의 CVE는 여전히 공개되지만, CVSS 점수, CPE 매핑, CWE 분류는 정부 사용 소프트웨어와 알려진 악용 취약점 등 일부 카테고리에만 제공된다. 컨테이너 스캔 및 규정 준수 프로그램은 NVD 데이터 구조 변화에 대응해야 한다.

**English Summary**: NIST announced on April 15 a prioritized enrichment model for the National Vulnerability Database, where fewer CVEs will receive CVSS scores, CPE mappings, and CWE classifications compared to historical coverage. Only CVEs affecting critical software, federal government systems, and known exploited vulnerabilities will receive full enrichment, while others move to "Not Scheduled" status. Organizations using NVD-dependent scanning workflows need to reassess their vulnerability management strategies.

**핵심 키워드**: NIST, National Vulnerability Database, CISA, Docker, CVE

### 2. [AI 시대 소프트웨어 개발 보안: GitLab의 DevSecOps 솔루션](https://about.gitlab.com/blog/harden-pipeline-perimeter-for-ai-assisted-coding/)
**출처**: GitLab Blog · **중요도**: 높음

**한국어 요약**: AI 보조 개발로 인한 보안 위협이 증가하고 있으며, 기존 보안 모델이 따라가지 못하고 있다. GitLab Ultimate는 See(가시성), Enforce(정책 시행), Fix(취약점 수정)의 세 가지 차원을 통합하여 DevSecOps 제어 플랫폼으로 기능한다. 그룹 보안 대시보드는 SAST, SCA, 시크릿 탐지 등 다양한 보안 스캔 결과를 한 곳에서 통합 관리할 수 있다.

**English Summary**: AI-assisted development tools are shipping code faster than security processes can govern, creating vulnerability gaps. GitLab Ultimate addresses this by integrating security into the core SDLC through three key capabilities: See (unified visibility), Enforce (policy enforcement), and Fix (automated remediation). The platform consolidates findings from multiple security scanners (SAST, SCA, container scanning, DAST, etc.) into a single Group Security Dashboard for comprehensive risk management.

**핵심 키워드**: GitLab, GitLab Ultimate, Group Security Dashboard, SAST, SCA, DAST

### 3. [GitLab, 정책 기반 취약점 심각도 자동 조정 기능 출시](https://about.gitlab.com/blog/severity-override-vulnerability-management-policy/)
**출처**: GitLab Blog · **중요도**: 높음

**한국어 요약**: GitLab은 CVSS 점수 기반의 일반적인 취약점 심각도 평가의 한계를 극복하기 위해 정책 기반 심각도 오버라이드 기능을 선보였다. 이 기능은 CVE ID, CWE ID, 파일 경로 등의 조건에 따라 취약점 심각도를 자동으로 조정하여 조직의 실제 위험 모델에 맞는 보고서를 생성한다. Set Severity, Increase Severity, Decrease Severity 등 세 가지 오버라이드 작업을 통해 수동 분류 작업을 자동화하고 확장성을 높일 수 있다.

**English Summary**: GitLab introduced vulnerability management severity override policies that automatically adjust CVSS severity levels based on custom conditions defined by enterprises. The feature allows organizations to override generic vulnerability ratings with context-aware severity assignments using CVE ID, CWE ID, file path matching and three override operations (Set, Increase, Decrease), enabling scalable vulnerability triage that reflects actual business risk rather than theoretical vulnerability characteristics.

**핵심 키워드**: GitLab, CVSS, CVE, CWE, Security Policy Bot

### 4. [GitLab 패치 릴리스: 18.11.3, 18.10.6, 18.9.7 보안 업데이트](https://docs.gitlab.com/releases/patches/patch-release-gitlab-18-11-3-released/)
**출처**: GitLab Blog · **중요도**: 높음

**한국어 요약**: GitLab은 2026년 5월 13일 커뮤니티 에디션과 엔터프라이즈 에디션의 패치 버전 18.11.3, 18.10.6, 18.9.7을 릴리스했다. 주요 버그 및 보안 수정 사항을 포함하고 있으며, 자체 관리 GitLab 설치 환경의 즉시 업그레이드를 강력히 권장한다. GitLab.com은 이미 패치 버전이 적용되었으며, GitLab Dedicated 고객은 별도 조치가 필요하지 않다.

**English Summary**: GitLab released patch versions 18.11.3, 18.10.6, and 18.9.7 on May 13, 2026, containing critical bug and security fixes. All self-managed GitLab installations are strongly urged to upgrade immediately, while GitLab.com and Dedicated customers are already protected or require no action.

**핵심 키워드**: GitLab, GitLab Community Edition, GitLab Enterprise Edition, GitLab.com, GitLab Dedicated

### 5. [쿠버네티스 v1.36: PSI 메트릭 정식 지원 시작](https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/)
**출처**: Kubernetes Blog · **중요도**: 높음

**한국어 요약**: 쿠버네티스 v1.36에서 Linux 커널의 PSI(Pressure Stall Information) 메트릭이 정식 지원(GA)되었다. PSI는 CPU 활용률 같은 전통적 지표와 달리 작업 지연과 손실 시간을 백분율로 제공하여 리소스 포화도를 더 정확히 파악할 수 있다. SIG Node의 광범위한 성능 검증을 통해 프로덕션 환경에서의 안정성이 입증되었다.

**English Summary**: Kubernetes v1.36 graduates PSI (Pressure Stall Information) metrics to General Availability, providing stable node, pod, and container-level resource contention monitoring. Unlike traditional utilization metrics, PSI tracks stalled tasks and time loss across CPU, memory, and I/O with moving averages, offering superior visibility into resource saturation before outages occur.

**핵심 키워드**: Kubernetes v1.36, PSI (Pressure Stall Information), SIG Node, Linux kernel

### 6. [쿠버네티스 v1.36: 워크로드 인식형 스케줄링 고도화](https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/)
**출처**: Kubernetes Blog · **중요도**: 높음

**한국어 요약**: 쿠버네티스 v1.36은 워크로드 API와 PodGroup API를 분리하여 스케줄링 아키텍처를 개선했습니다. 새로운 PodGroup 스케줄링 사이클, 토폴로지 인식형 스케줄링, 워크로드 인식형 선점, 그리고 Dynamic Resource Allocation(DRA) 지원이 추가되었습니다. 이러한 변화는 AI/ML 및 배치 워크로드의 복잡한 스케줄링 요구사항을 효과적으로 처리합니다.

**English Summary**: Kubernetes v1.36 advances workload-aware scheduling by separating the Workload API (static template) from the new PodGroup API (runtime state), introducing a new PodGroup scheduling cycle for atomic workload processing. New features include topology-aware scheduling, workload-aware preemption, ResourceClaim support for Dynamic Resource Allocation, and initial Job controller integration with the new API architecture.

**핵심 키워드**: Kubernetes, Workload API, PodGroup API, kube-scheduler, Job controller, DRA

## 커뮤니티

### 1. [실시간 AI 워크플로우 확장: 1천만 이벤트 처리 후 재설계 전략](https://dev.to/smartguy666/what-broke-after-10m-realtime-events-and-how-we-re-architected-for-realtime-ai-workflows-3024)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 대규모 동시 사용자 환경에서 실시간 이벤트 기반 AI 에이전트 오케스트레이션 시스템이 직면한 확장성 문제를 분석합니다. WebSocket 연결 폭증, 메시지 순서 보장 실패, 상태 관리 복잡성 증가 등의 문제가 발생했으며, 인프라 오버헤드가 실제 병목임을 발견했습니다. 멀티테넌트 SaaS 환경에서 신뢰할 수 있는 실시간 백엔드 아키텍처 재설계 경험을 공유합니다.

**English Summary**: The article describes scaling challenges when a realtime event-driven backend for AI workflows grew from thousands to tens of thousands of concurrent users. Key issues included WebSocket connection storms, message ordering inconsistencies, in-memory state loss, and infrastructure complexity becoming the primary bottleneck. The team explores various architectural approaches to support multi-agent orchestration and long-running inference sessions in production.

**핵심 키워드**: WebSocket cluster, message broker, AI agents, multi-tenant SaaS, inference sessions

### 2. [Docker VPS 배포: Nginx를 활용한 무중단 서비스 전략](https://dev.to/merbayerp/docker-deploy-on-vps-nginx-strategies-for-zero-downtime-dpl)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: VPS 환경에서 Docker 컨테이너를 배포할 때 서비스 중단을 방지하기 위해 Nginx 리버스 프록시를 활용하는 방법을 설명한다. 기존 버전을 유지하면서 새 버전을 백그라운드에서 실행한 후 Nginx의 upstream 블록과 proxy_pass를 이용해 트래픽을 지능적으로 라우팅하는 기법을 소개한다.

**English Summary**: This article explains how to implement zero-downtime deployment strategies for Dockerized applications on a VPS using Nginx as a reverse proxy. By running new application versions in parallel while keeping the current version live, Nginx intelligently routes traffic between backend servers using upstream blocks and proxy_pass configuration to ensure seamless service transitions.

**핵심 키워드**: Nginx, Docker, VPS, upstream blocks, proxy_pass

### 3. [엔지니어가 자격증 취득 시 범하는 5가지 실수](https://dev.to/truecert/5-mistakes-engineers-make-when-getting-certified-3boo)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자들이 자격증 취득 시 반복하는 실수를 분석한 글입니다. 코스 구매 전 평가 시험 먼저 진행하기, 산업에서 실제 요구하는 자격증 선택하기 등 효율적인 자격증 취득 전략을 제시합니다. 불필요한 시간과 비용 낭비를 줄이는 실용적 조언을 담고 있습니다.

**English Summary**: This article outlines five common mistakes engineers make when pursuing certifications and provides practical solutions. Key recommendations include taking an assessment before enrolling in courses to identify knowledge gaps, and researching actual job requirements before choosing which certification to pursue, rather than relying on general credentials.

**핵심 키워드**: AWS, GCP, Terraform, certification industry

### 4. [Ubuntu 24.04에서 Ubuntu 26.04 LTS로 업그레이드하기](https://dev.to/vultr/upgrading-ubuntu-2404-to-ubuntu-2604-1cf4)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Ubuntu 24.04 LTS에서 Ubuntu 26.04 LTS로 in-place 업그레이드하는 실전 가이드입니다. do-release-upgrade 도구를 사용하여 Linux 7.0 커널과 업데이트된 보안 기본값을 적용할 수 있으며, SSH 포트 관리, 설정 파일 충돌 해결, 불필요한 패키지 제거 등의 주요 단계를 다룹니다.

**English Summary**: A step-by-step guide for upgrading Ubuntu 24.04 LTS to Ubuntu 26.04 LTS in-place using the do-release-upgrade tool. The article covers preparation steps, opening auxiliary SSH port 1022 to prevent lockouts, handling configuration conflicts, and confirming the upgraded system with the new Linux 7.0 kernel.

**핵심 키워드**: Ubuntu 24.04 LTS, Ubuntu 26.04 LTS, Linux 7.0 kernel, do-release-upgrade, SSH daemon

### 5. [Ubuntu 26.04에서 RabbitMQ 설치 및 보안 구성 가이드](https://dev.to/vultr/installing-rabbitmq-on-ubuntu-2604-c67)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 가이드는 Ubuntu 26.04에서 오픈소스 메시지 브로커인 RabbitMQ를 설치하고 관리하는 방법을 설명합니다. Erlang 런타임 설치, RabbitMQ 서버 구성, 관리 플러그인 활성화, 그리고 Nginx와 Let's Encrypt를 사용하여 웹 대시보드를 HTTPS로 보안하는 단계를 포함합니다. 완료 후 분산 애플리케이션 간의 메시지 큐 기반 통신이 가능한 안전한 RabbitMQ 환경을 갖추게 됩니다.

**English Summary**: A comprehensive guide for installing RabbitMQ on Ubuntu 26.04, covering installation of Erlang and RabbitMQ server, service management, and securing the management dashboard with Nginx and Let's Encrypt SSL certificates. The tutorial enables distributed applications to communicate asynchronously through message queues.

**핵심 키워드**: RabbitMQ, Ubuntu 26.04, Erlang, Nginx, Let's Encrypt

### 6. [Ubuntu 26.04에서 Podman 설치 및 컨테이너 운영 가이드](https://dev.to/vultr/installing-podman-on-ubuntu-2604-193n)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 이 가이드는 Ubuntu 26.04에서 Docker 호환 데몬리스 컨테이너 엔진인 Podman을 설치하고 관리하는 방법을 설명합니다. APT 저장소에서 Podman을 설치한 후 Podman 소켓을 활성화하고 Nginx 컨테이너를 배포하는 단계를 다룹니다. Podman은 백그라운드 데몬 없이 각 컨테이너를 독립적인 프로세스로 실행하여 단일 장애점을 제거합니다.

**English Summary**: A comprehensive guide for installing and managing Podman, a daemonless container engine compatible with Docker CLI, on Ubuntu 26.04. The article covers installation steps, enabling Podman socket for API access, and deploying containerized applications like Nginx. Podman's architecture runs each container as an independent process without a background daemon, improving reliability and compatibility with OCI container formats.

**핵심 키워드**: Podman, Ubuntu 26.04, Docker, OCI, Nginx, systemctl

### 7. [Ubuntu 26.04에서 Hermes Agent 배포하기](https://dev.to/vultr/deploying-hermes-agent-on-ubuntu-2604-4128)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Nous Research의 오픈소스 AI 에이전트 프레임워크인 Hermes Agent를 Ubuntu 26.04에 Docker Compose로 배포하는 방법을 다룬다. Telegram, Discord, Slack, WhatsApp 등과 통합되며 OpenAI 호환 LLM 제공자를 지원한다. Traefik을 통한 자동 HTTPS 설정과 LLM 백엔드 구성으로 보안된 웹 대시보드를 갖춘 자체 호스팅 AI 에이전트를 구축할 수 있다.

**English Summary**: A practical guide to deploying Hermes Agent, an open-source self-hosted AI agent framework by Nous Research, on Ubuntu 26.04 using Docker Compose and Traefik. The framework supports multiple messaging platforms and OpenAI-compatible LLM providers, providing a secured web dashboard with verified LLM connectivity for continuous AI agent operations.

**핵심 키워드**: Hermes Agent, Nous Research, Docker Compose, Traefik, Vultr Serverless Inference

### 8. [Ubuntu 26.04에서 OpenClaw 자율 AI 에이전트 플랫폼 배포하기](https://dev.to/vultr/deploying-openclaw-on-ubuntu-2604-303e)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: OpenClaw는 WhatsApp, Telegram, Slack, Discord를 지원하는 자체 호스팅 자율 AI 에이전트 플랫폼입니다. 이 가이드는 Docker를 활용하여 Ubuntu 26.04에 OpenClaw를 배포하고, Caddy를 통해 HTTPS로 제어 UI를 안전하게 노출하는 방법을 설명합니다. OpenAI 호환 모델 제공자를 지원하며 세션 간 지속적인 메모리를 유지합니다.

**English Summary**: This tutorial guides deploying OpenClaw, a self-hosted autonomous AI agent platform supporting WhatsApp, Telegram, Slack, and Discord, on Ubuntu 26.04 using Docker. The platform maintains persistent memory across sessions and works with any OpenAI-compatible model provider, with secure HTTPS access via Caddy reverse proxy.

**핵심 키워드**: OpenClaw, Docker, Ubuntu 26.04, Caddy, WhatsApp, Telegram, Slack, Discord, OpenAI
