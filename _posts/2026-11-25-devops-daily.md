---
layout: post
title: "2026-11-25 DevOps/인프라 데일리 브리핑"
date: 2026-11-25 00:07:00 +0900
categories: [devops]
tags:
  - AWS
  - CI/CD
  - CIDR
  - CNI
  - Claude Code
  - DevOps
  - GitLab Dedicated
  - Go-live Guide
  - HCP
  - Infrastructure as Code
  - Kubernetes
  - OpenShift
  - Platform Operations
  - SSH
  - SaaS
  - Sharkly
  - Terraform
  - Ubuntu 24.04 LTS
  - VPC
  - VPS deployment
---

> 수집 시각: 2026-11-25 04:14 UTC | 총 10건

## 뉴스 & 릴리즈

### 1. [Terraform, Stacks용 tfpolicy 지원 및 SCIM 지원 추가](https://www.hashicorp.com/blog/terraform-introduces-tfpolicy-support-for-stacks-scim-support-and-more)
**출처**: HashiCorp Blog · **중요도**: 높음

**한국어 요약**: HashiCorp가 HCP Terraform과 Terraform Enterprise에 tfpolicy 지원, SCIM 지원, AI 준비 워크플로우 등을 추가했다. 이러한 업데이트는 인프라 오케스트레이션 강화, 거버넌스 개선, 팀의 안전하고 효율적인 확장을 목표로 한다.

**English Summary**: HashiCorp announces enhancements to HCP Terraform and Terraform Enterprise, including tfpolicy support for Stacks, SCIM support, and AI-ready workflows. These updates aim to improve infrastructure orchestration, governance, and enable teams to scale infrastructure securely and efficiently.

**핵심 키워드**: HashiCorp, HCP Terraform, Terraform Enterprise, Stacks, tfpolicy, SCIM

### 2. [GitLab Dedicated: 가동 시작 가이드](https://about.gitlab.com/blog/gitlab-dedicated-a-go-live-guide/)
**출처**: GitLab Blog · **중요도**: 보통

**한국어 요약**: GitLab Dedicated는 AWS 클라우드에 완전히 격리된 단일 테넌트 SaaS 솔루션으로, GitLab이 운영 및 유지보수를 담당합니다. 플랫폼 운영 책임이 GitLab과 고객 간에 분담되며, GitLab은 버전 관리, 보안 패치, 백업 등을 담당하고 고객은 파이프라인 설정, 웹훅 통합, 러너 구성 등을 관리합니다. Switchboard 관리 포털을 통해 고객은 필요한 설정을 수행할 수 있습니다.

**English Summary**: GitLab Dedicated is a fully isolated single-tenant SaaS solution deployed on AWS and managed by GitLab. The article outlines the division of responsibilities between GitLab (platform operations, security patching, backups) and customers (pipeline configuration, integrations, runner management), and introduces Switchboard as the administration portal for configuration management.

**핵심 키워드**: GitLab, GitLab Dedicated, Switchboard, AWS, Single-tenant SaaS

## 커뮤니티

### 1. [Windows 이미징 시스템 인수인계 시 필수 감사 체크리스트](https://dev.to/pxecommercialio/the-person-who-built-your-windows-imaging-rig-left-here-is-the-audit-545g)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Windows 배포 환경을 인수받았을 때 수행해야 할 감사 프로세스를 설명한 글입니다. 부팅 경로, 아키텍처 맵, 드라이버 저장소, 응답 파일 등 무인 설치에 필요한 4가지 핵심 요소를 문서화하고 추적해야 한다고 강조합니다. 이전 담당자의 암묵적 지식에 의존한 시스템을 체계적으로 파악하는 방법론을 제시합니다.

**English Summary**: A guide for auditing inherited Windows deployment infrastructure after personnel transitions. The article identifies four critical artifacts required for unattended machine installation: boot path configuration, architecture mapping, driver storage, and answer files. It emphasizes documenting these elements systematically to prevent knowledge loss and ensure system recoverability.

**핵심 키워드**: Windows imaging, DHCP, boot files, device drivers, RFC 2132, RFC 4578

### 2. [AWS Builder Center 배지 획득 여정: 지속적인 학습과 커뮤니티 참여](https://dev.to/vishal_patil_aws/another-milestone-unlocked-my-aws-builder-center-badges-journey-34f6)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 인도의 컴퓨터과학 대학원생이 AWS Builder Center에서 얻은 배지들을 소개하며 클라우드 학습 경험을 공유합니다. 작은 목표 설정, 커뮤니티 참여, 지속적인 학습과 공유를 통해 성장하는 과정을 강조합니다. AWS 클라우드 엔지니어로의 경력 개발에 도움이 되는 실질적인 조언을 제공합니다.

**English Summary**: A Computer Science graduate student shares his journey earning badges on AWS Builder Center, a community platform for cloud builders. He emphasizes the importance of consistent small efforts, community engagement, and sharing knowledge while learning AWS services, demonstrating how regular participation trumps occasional bursts of activity.

**핵심 키워드**: AWS Builder Center, Vishal, Maharashtra India, Cloud & DevOps Engineer

### 3. [SSH 개인키 형식 오류 해결 가이드 (2026)](https://dev.to/masitings/load-key-invalid-format-ssh-private-key-fix-2026-2ad5)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: SSH 개인키의 'invalid format' 오류는 키 자체의 문제가 아니라 파일 손상으로 인한 것이다. 줄바꿈 누락, Windows 줄바꿈, 텍스트 인코딩 변경, CI 시크릿 평탄화 등 여덟 가지 원인이 있으며, 각각에 대한 해결 방법이 한 개의 명령어로 해결 가능하다. 새 키를 생성하지 않고도 기존 파일을 복구할 수 있다.

**English Summary**: The 'Load key: invalid format' SSH error typically results from file corruption rather than a defective key. The article identifies eight reproducible causes including lost newlines, Windows line endings, text encoding changes, and flattened CI secrets, each with a one-command fix without regenerating the key.

**핵심 키워드**: OpenSSH 9.6, SSH private key, ed25519, CI/CD secrets

### 4. [클라우드 서버 백업 실패 사건: 6개월 운영 기록](https://dev.to/lilika/san-feng-yun-mian-fei-yun-fu-wu-qi-shi-ce-ci-wu-shan-hou-de-huan-jing-zhong-zhuang-shun-shou-ba-bei-fen-jiao-ben-bu-dui-liao-ban-nian-yun-wei-ji-lu--5gkn)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자가 Sanfeng Cloud 무료 서버에서 경험한 백업 스크립트 오류 사건을 다룬 글입니다. rm -rf 명령으로 실수로 파일을 삭제했을 때, 기존 백업은 데이터베이스를 포함하지 않고 같은 디스크에만 저장되어 있어 완전히 복구되지 않았습니다. 이후 백업 + 데이터베이스 덤프 + 별도 서버 전송으로 개선된 백업 전략으로 재작성했습니다.

**English Summary**: A DevOps practitioner documents a critical backup failure on Sanfeng Cloud after accidentally deleting production files with rm -rf. The existing backup script had critical flaws: it only backed up application files without databases and stored backups on the same disk, causing silent failures. The author rebuilt the backup strategy to include database exports and remote server transfers.

**핵심 키워드**: Sanfeng Cloud, Typecho, mysqldump, tar.gz, Nginx

### 5. [Sharkly 웹훅으로 에이전트 실행 자동화하기](https://dev.to/roobia/como-disparar-ejecuciones-de-agente-con-un-webhook-de-sharkly-2ep7)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Sharkly의 웹훅 자동화를 통해 HTTP POST 요청으로 에이전트 실행을 트리거할 수 있습니다. Cancel Anything 팀의 사례에서 야간 구독 취소 페이지 검증 실패 시 자동으로 버그 리포트를 생성하는 방식을 소개합니다. JSON 페이로드는 에이전트에 전달되어 작업 생성, 댓글 작성 등의 작업을 수행할 수 있습니다.

**English Summary**: This tutorial demonstrates how to trigger Sharkly agent executions via webhooks using HTTP POST requests. The example shows Cancel Anything team automating their nightly subscription cancellation page verification, automatically creating bug reports with agent diagnostics when failures occur.

**핵심 키워드**: Sharkly, Cancel Anything, webhook automation, agent execution

### 6. [AWS VPC 서브넷 계산기의 한계와 CIDR 수학 시각화](https://dev.to/_a19f513dbff3445581b0/why-traditional-subnet-calculators-break-on-aws-vpcs-and-how-to-visualize-32-bit-cidr-math-29nd)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: AWS VPC는 RFC 표준 이더넷과 달리 모든 서브넷에서 5개의 IP 주소를 예약하기 때문에 전통적인 서브넷 계산 공식이 작동하지 않습니다. /28 서브넷은 RFC 기준 14개가 아닌 11개의 사용 가능한 IP만 제공합니다. 이 글은 클라우드 환경과 온프레미스 네트워킹의 차이를 설명하고 빠른 계산 방법을 제시합니다.

**English Summary**: AWS VPCs reserve 5 IP addresses per subnet (vs. 2 in standard Ethernet), reducing usable IPs significantly—a /28 subnet provides only 11 usable IPs instead of the textbook 14. This gap causes real deployment failures. The article explains why traditional subnet calculators fail in cloud environments and introduces the 'Magic Number' method for quick CIDR calculations.

**핵심 키워드**: AWS VPC, RFC 4632, Azure VNet, Google Cloud VPC, /28 subnet, CIDR notation

### 7. [Claude Code를 VPS에 배포하는 방법: 원격 워크플로우 및 Ubuntu 가이드](https://dev.to/cash602cmd/how-to-deploy-claude-code-on-a-vps-4-remote-workflows-sizing-ubuntu-guide-2f24)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Anthropic의 Claude Code를 저비용 Linux VPS(월 $5)에서 실행하면 로컬 머신 종료 후에도 24/7 지속적인 AI 개발 환경을 유지할 수 있다. GPU 연산이 필요 없고 Anthropic 클라우드에서 LLM 추론이 모두 처리되므로 경제적이며, CLI+tmux, VS Code Remote-SSH 등 4가지 원격 아키텍처 패턴을 비교 분석한다.

**English Summary**: Claude Code can run efficiently on a cheap $5/month Ubuntu VPS since all LLM inference happens on Anthropic's cloud and only requires a lightweight CLI client locally. The article compares 4 remote deployment workflows (CLI+tmux, VS Code Remote-SSH, Official Remote Control, and CC Desk Tunnel) with hardware sizing recommendations for persistent, 24/7 AI development workbenches.

**핵심 키워드**: Anthropic, Claude Code, Ubuntu, VS Code Remote-SSH, tmux

### 8. [쿠버네티스와 OpenShift에서 Zero-Trust 팟 마이크로 세그멘테이션 구현](https://dev.to/hostingpodium/zero-trust-pod-micro-segmentation-at-scale-in-kubernetes-openshift-1139)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 전통적인 경계 방어가 컨테이너 환경에서 실패하므로, 모든 팟을 신뢰할 수 없는 엔드포인트로 취급하는 Zero-Trust 아키텍처 도입이 필수다. 쿠버네티스와 Red Hat OpenShift에서 기본값 거부 정책, 네임스페이스 격리, eBPF 데이터 경로를 활용한 세밀한 마이크로 세그멘테이션 구현 방법을 다룬다. 대규모 환경에서 iptables 기반 CNI의 성능 저하 문제를 eBPF를 통해 해결한다.

**English Summary**: The article explains how to implement zero-trust pod micro-segmentation in Kubernetes and OpenShift by treating every pod as an untrusted endpoint and enforcing default-deny policies with explicit traffic declarations. It addresses architectural imperatives for cluster security in multi-tenant environments and discusses how modern eBPF-based approaches overcome the performance limitations of traditional iptables-based network policies at scale.

**핵심 키워드**: Kubernetes, Red Hat OpenShift, eBPF, CNI, iptables, netfilter
