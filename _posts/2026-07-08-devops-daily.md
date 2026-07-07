---
layout: post
title: "2026-07-08 DevOps/인프라 데일리 브리핑"
date: 2026-07-08 00:07:00 +0900
categories: [devops]
tags:
  - DevOps
  - DevOps-automation
  - Docker
  - Docker Compose
  - Grafana
  - Kafka
  - MLOps
  - Machine Learning
  - MariaDB
  - Matomo
  - Nginx
  - Nix
  - NixOS
  - Open Source
  - PaaS
  - PagedAttention
  - Privacy
  - Redpanda
  - SCIM
  - SSL/TLS
---

> 수집 시각: 2026-07-07 22:51 UTC | 총 9건

## 튜토리얼 & 아티클

### 1. [Grafana Cloud의 접근 제어 확장: SSO와 SCIM 활용](https://grafana.com/blog/how-to-scale-access-control-in-grafana-cloud/)
**출처**: Grafana Blog · **중요도**: 보통

**한국어 요약**: Grafana Cloud는 SSO(Single Sign-On)와 SCIM(System for Cross-domain Identity Management)을 통해 사용자 접근 제어를 효율적으로 확장할 수 있습니다. ID 제공자에서 사용자와 그룹이 추가, 제거, 업데이트될 때 이러한 변경사항이 Grafana Cloud에 자동으로 반영됩니다. 이는 단일 신원 소스를 제공하며 수동 조정이나 설정 편차 문제를 제거합니다.

**English Summary**: Grafana Cloud enables scalable access control by leveraging SSO for authentication and SCIM for automated user and group provisioning. Identity provider changes are automatically synchronized to Grafana Cloud, eliminating manual management and ensuring a single source of truth for user identity and permissions.

**핵심 키워드**: Grafana Cloud, SSO (Single Sign-On), SCIM (System for Cross-domain Identity Management), AcmeCloud

## 커뮤니티

### 1. [vLLM PagedAttention KV 캐시 손상 문제 해결 경험기](https://dev.to/enadoc2_temp_cc4da1a52236/title-4e0n)
**출처**: Dev.to DevOps · **중요도**: 높음

**한국어 요약**: 개발자가 vLLM의 PagedAttention을 사용하는 모델 서빙 중 KV 캐시 손상으로 인한 장애를 겪은 경험을 공유한다. 최고 RPS 14,720에서 발생한 이 문제는 배치 크기 32에서 KV 스토어 접근 시 예외를 발생시켰으며, 텐서 형태(배치 크기, 시퀀스 길이, 은닉 크기)의 불일치가 원인으로 보인다. 이는 대규모 트래픽 처리 시 LLM 서빙 인프라의 안정성 문제를 다룬다.

**English Summary**: A developer shares an on-call incident involving KV cache corruption in vLLM's PagedAttention during model serving at peak RPS of 14,720. The issue manifests as exceptions when accessing the KV store with batch size 32, causing tensor shape mismatches. The post documents debugging a critical production issue in LLM inference infrastructure.

**핵심 키워드**: vLLM, PagedAttention, KV Cache, KV Store, paged_attention.py, model_serving.py

### 2. [Matomo 오픈소스 애널리틱스 Docker로 배포하기](https://dev.to/vultr/deploying-matomo-analytics-an-open-source-google-analytics-alternative-3noa)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Matomo는 Google Analytics의 오픈소스 대체 솔루션으로, 사용자 데이터를 자신의 인프라에서 완전히 관리할 수 있는 프라이버시 중심 웹 분석 플랫폼입니다. 이 가이드는 Docker Compose, MariaDB, Nginx, Certbot을 활용하여 Matomo를 배포하는 단계별 방법을 설명하며, HTTPS 인증서가 적용된 완전한 설정을 제공합니다.

**English Summary**: This tutorial guides developers through deploying Matomo, an open-source privacy-focused web analytics platform, using Docker Compose with MariaDB, Nginx, and Certbot for SSL/TLS. The setup allows complete data ownership and control over visitor analytics while providing a Google Analytics alternative.

**핵심 키워드**: Matomo, Docker Compose, MariaDB, Nginx, Certbot, Google Analytics

### 3. [Ubuntu 24.04에서 Redpanda Kafka 호환 스트리밍 플랫폼 배포](https://dev.to/vultr/deploying-redpanda-kafka-compatible-streaming-platform-on-ubuntu-2404-4elh)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 본 가이드는 C++로 작성된 Kafka API 호환 스트리밍 플랫폼인 Redpanda를 Ubuntu 24.04에 설치하고, Let's Encrypt 인증서와 SASL/SCRAM 인증으로 보안을 강화하며, 커널을 프로덕션 환경에 맞게 튜닝하는 방법을 설명합니다. 프로듀서/컨슈머 테스트로 검증하고 Nginx 기본 인증 뒤에 Redpanda Console을 노출하여 보안이 강화되고 프로덕션 준비가 완료된 단일 노드 클러스터를 구성할 수 있습니다.

**English Summary**: This tutorial provides a comprehensive guide to deploying Redpanda, a Kafka-compatible streaming platform written in C++, on Ubuntu 24.04. It covers installation, security configuration with Let's Encrypt TLS and SASL/SCRAM authentication, kernel tuning for production, and deployment of Redpanda Console behind Nginx with basic authentication.

**핵심 키워드**: Redpanda, Ubuntu 24.04, Let's Encrypt, SASL/SCRAM, Nginx, Kafka API

### 4. [Nix를 활용한 LabCraft 학습 플랫폼 출시](https://dev.to/anandsuresh81/why-im-starting-labcraft-with-nix-2bg3)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 개발자가 인프라 및 시스템 도구 학습을 위한 실습형 플랫폼 LabCraft를 Nix/NixOS 강좌부터 시작하며 출시했다. Nix의 복잡한 문서와 오류 메시지로 인한 학습 곡선 문제를 해결하기 위해 실제 VM 환경에서 실습하고 오류를 직접 해결하는 방식으로 설계했다. 사용자들이 자주 막히는 부분(셸 설정, 실험 기능, 빌드 오류 등)을 중심으로 커리큘럼을 구성했다.

**English Summary**: A developer launched LabCraft, a hands-on learning platform for infrastructure tools, starting with a Nix/NixOS course. The platform addresses common learning barriers with Nix by providing real VM-based environments where learners can break, repair, and understand systems practically rather than through abstract tutorials. The course focuses on frequent pain points like shell setup, build errors, and conceptual misunderstandings.

**핵심 키워드**: LabCraft, Nix, NixOS, Dev.to

### 5. [Plausible Analytics 자체 호스팅 배포 가이드](https://dev.to/vultr/deploying-plausible-analytics-self-hosted-web-analytics-platform-48he)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Plausible Analytics는 개인정보를 수집하지 않는 프라이버시 중심의 오픈소스 웹 분석 도구로, Google Analytics의 대안입니다. 이 가이드는 Docker Compose를 사용하여 Plausible Community Edition을 Ubuntu 24.04에 배포하고 Nginx와 Let's Encrypt 인증서로 보안하는 과정을 설명합니다.

**English Summary**: This tutorial guides deploying Plausible Analytics, an open-source, privacy-first web analytics platform that tracks website traffic without cookies or personal data collection. The deployment uses Docker Compose, Nginx reverse proxy, and Let's Encrypt SSL certificates on Ubuntu 24.04.

**핵심 키워드**: Plausible Analytics, Docker Compose, Nginx, Let's Encrypt, Ubuntu 24.04, Google Analytics

### 6. [ClearML을 GCP Vertex AI의 오픈소스 대안으로 Ubuntu에 배포하기](https://dev.to/vultr/deploying-clearml-as-a-gcp-vertex-ai-alternative-on-ubuntu-n2f)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: 본 가이드는 Google Cloud의 Vertex AI를 대체할 수 있는 오픈소스 MLOps 플랫폼인 ClearML을 Docker Compose와 Traefik을 이용해 Ubuntu에 배포하는 방법을 설명합니다. ClearML은 자동 메트릭 추적, 실험 관리, 파이프라인 구성, 하이퍼파라미터 튜닝, 모델 배포 등 머신러닝 전체 생명주기를 자체 인프라에서 관리할 수 있는 장점이 있습니다.

**English Summary**: This tutorial demonstrates deploying ClearML, an open-source MLOps platform, as a self-hosted alternative to Google Vertex AI on Ubuntu using Docker Compose. ClearML provides automatic metric tracking, experiment management, pipeline orchestration, hyperparameter sweeps, and model serving capabilities while keeping data on user-controlled infrastructure.

**핵심 키워드**: ClearML, Google Vertex AI, Docker Compose, Traefik, Triton, Ubuntu

### 7. [VEX를 활용한 컨테이너 취약점 트리아주 자동화](https://dev.to/darkedges/from-vexctl-scripts-to-a-governed-vex-platform-building-vex-ui-with-nextjs-keyless-signing-and-1jkm)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Trivy 스캔 결과를 VEX(Vulnerability Exploitability eXchange) 형식으로 변환하여 실제 배포에 영향 없는 취약점을 자동으로 필터링하는 워크플로우를 소개한다. OpenVEX와 vexctl을 이용해 스캔 → VEX 생성 → 저장소 호스팅 → 재스캔 전 과정을 다루며, 실행 가능한 데모 리포지토리를 제공한다.

**English Summary**: This article demonstrates a complete VEX (Vulnerability Exploitability eXchange) workflow for automatically triaging container image vulnerabilities by converting Trivy scan results into machine-readable statements. It covers baseline scanning, OpenVEX generation, hosting a VEX repository, and re-scanning with suppression, providing practical implementation details and a runnable demo.

**핵심 키워드**: Trivy, VEX, OpenVEX, vexctl, container-scanning, vulnerability-exploitability

### 8. [Ubuntu 24.04에서 Dokploy 자체 호스팅 PaaS 배포하기](https://dev.to/vultr/deploying-dokploy-self-hosted-paas-for-docker-applications-on-ubuntu-2404-27eg)
**출처**: Dev.to DevOps · **중요도**: 보통

**한국어 요약**: Dokploy는 Heroku, Vercel, Netlify의 무료 오픈소스 대체제로, Git에서 앱을 배포하고 데이터베이스를 관리하며 Traefik을 통해 자동 HTTPS를 제공하는 자체 호스팅 PaaS입니다. 이 가이드는 Ubuntu 24.04에서 Dokploy를 설치하고 공개 Git 저장소에서 샘플 앱을 배포하는 방법을 설명합니다.

**English Summary**: Dokploy is an open-source, self-hosted PaaS platform offering a free alternative to Heroku, Vercel, and Netlify. It enables app deployment from Git, database management, and automatic HTTPS traffic routing via Traefik. This tutorial guides users through installing Dokploy on Ubuntu 24.04 and deploying sample applications.

**핵심 키워드**: Dokploy, Ubuntu 24.04, Docker, Traefik, Heroku, Vercel, Netlify
