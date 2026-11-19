---
layout: post
title: "2026-11-19 백엔드 데일리 브리핑"
date: 2026-11-19 00:07:00 +0900
categories: [backend]
tags:
  - A/B testing
  - AI API
  - AI video generation
  - API security
  - Apache Celeborn
  - Apache Spark
  - BOLA
  - BOLA vulnerability
  - CVE-2026-115560
  - Cassandra
  - EBS
  - EKS
  - FastAPI
  - IDOR
  - JSON parsing
  - Kubernetes
  - ML infrastructure
  - N+1 queries
  - Next.js
  - PHP
---

> 수집 시각: 2026-11-19 02:36 UTC | 총 16건

## 튜토리얼 & 아티클

### 1. [데이터 계약: 현대적 데이터 관리의 필수요소](https://martinfowler.com/articles/data-contracts.html)
**출처**: Martin Fowler · **중요도**: 높음

**한국어 요약**: 에이전트 AI 시대에 기업의 데이터 기반 의사결정을 위해서는 신뢰할 수 있는 데이터 계약이 필수적이다. 본 글은 다양한 소스의 데이터를 통합할 때 발생하는 데이터 품질, 구조 안정성, 규정 준수 등의 문제를 해결하기 위해 데이터 엔지니어와 데이터 소유자 간의 명확한 계약이 필요함을 강조한다.

**English Summary**: Data contracts are becoming essential in modern data-driven organizations to establish trust and clarity when integrating data from multiple sources. The article outlines key questions data engineers must address regarding data completeness, quality, freshness, structural stability, and compliance when working with datasets across large enterprises.

**핵심 키워드**: Martin Fowler, data contracts, data engineers, insurance company

### 2. [Booking.com의 AI 진화: 20년간의 ML 플랫폼 발전사](https://www.infoq.com/presentations/bookingcom-ml-data-platform-evolution/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 높음

**한국어 요약**: Booking.com의 엔지니어가 QCon 20주년을 맞아 회사의 머신러닝 플랫폼 진화 과정을 공개했습니다. 데이터 관리, ML 엔지니어링, 도메인 인텔리전스 등 3개 계층으로 나눠 2005년부터 현재까지의 기술 진화를 추적하며, 특히 A/B 테스트 도입과 대규모 모델 서빙 등 주요 이정표를 소개합니다.

**English Summary**: Booking.com presented its 20-year evolution of machine learning platforms that power billions of travel decisions. The presentation covers three layers: data management (database evolution and cloud migration), ML engineering (model serving at scale and feature engineering), and domain intelligence (ML platform portfolio overview). The company highlights early milestones like running their first A/B experiment in 2005.

**핵심 키워드**: Booking.com, Jabez Eliezer Manuel, InfoQ, QCon

### 3. [LinkedIn, Apache Celeborn으로 Spark 셔플 실패 750건에서 20건으로 단축](https://www.infoq.com/news/2026/11/linkedin-celeborn-remote-shuffle/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 높음

**한국어 요약**: LinkedIn이 Apache Celeborn을 도입하여 Spark와 Flink 워크로드의 중간 데이터 저장소를 계산 인프라에서 분리했다. 이를 통해 일일 셔플 페치 실패를 750건에서 20건으로 감소시켰으며, 계산 비용을 10% 절감하고 애플리케이션 런타임을 14% 개선했다.

**English Summary**: LinkedIn deployed Apache Celeborn as a dedicated remote shuffle platform, reducing daily shuffle fetch failures from 750 to 20 and decreasing compute costs by 10% while improving application runtimes by 14%. The solution separates intermediate data storage from compute clusters, addressing shuffle workload challenges across LinkedIn's 300,000+ daily Spark jobs.

**핵심 키워드**: LinkedIn, Apache Celeborn, Apache Spark, Apache Flink, Magnet

### 4. [Yelp, EBS 볼륨 재연결로 Cassandra를 EKS로 마이그레이션](https://www.infoq.com/news/2026/11/kubernetes-cassandra-eks/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 높음

**한국어 요약**: Yelp는 자체 관리 Kubernetes 클러스터에서 Amazon EKS로 Cassandra 플릿을 마이그레이션했습니다. EBS 볼륨을 새로운 Pod에 직접 재연결하는 'Rolling PV Transplant' 방식을 사용하여 약 90개의 프로덕션 클러스터를 다운타임 없이 이동했습니다. 가장 큰 클러스터는 약 12시간이 소요되었으며 데이터 손실이나 고객 영향이 없었습니다.

**English Summary**: Yelp successfully migrated its Cassandra fleet from self-managed Kubernetes to Amazon EKS across 90 production clusters using a novel 'Rolling PV Transplant' approach that re-points EBS volumes to new pods, avoiding data streaming costs and achieving zero downtime. The migration leverages the fact that EBS volumes are zone-bound and PersistentVolumes are volume ID pointers, enabling efficient StatefulSet migration without doubling compute capacity.

**핵심 키워드**: Yelp, Amazon EKS, Cassandra, Kubernetes, EBS, PersistentVolume

## 커뮤니티

### 1. [미국 SMS 발송 규정: 22개 주의 비즈니스 문자 송수신 시간 가이드](https://dev.to/nova_solutions/building-an-sms-feature-for-us-businesses-22-states-have-their-own-texting-law-here-are-the-1o71)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: 미국에서 비즈니스용 SMS 기능을 개발할 때 연방 규정뿐 아니라 22개 주의 개별 법률을 준수해야 한다. 연방 규정은 오전 8시~오후 9시(수신자 기준) 송수신만 허용하며, 주별로 추가 제한, 서면 동의 요구, 옵트아웃 리스트 등이 상이하다. 개발자는 각 주의 구체적인 송수신 시간 제한을 코드에 반영해야 한다.

**English Summary**: Developers building SMS features for US businesses must comply with 22 state-level texting laws in addition to federal regulations. Federal rules restrict commercial texts to 8 a.m.–9 p.m. (recipient's local time), but individual states have additional requirements including sending hour limits, consent requirements, and do-not-call lists. The article provides specific sending hour restrictions by state for sales messages.

**핵심 키워드**: 22 US states, Federal regulations (47 C.F.R. § 64.1200), SMS compliance, sending hours, Virginia, Connecticut, Pennsylvania, New York

### 2. [PHP 11월 19일 긴급 보안 업데이트 공지](https://dev.to/hacksgr/critical-php-security-update-coming-november-19th-2i4g)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: PHP 보안팀이 2026년 11월 19일 모든 지원 버전에 대한 긴급 보안 업데이트를 예고했다. CVE-2026-115560을 포함한 여러 취약점을 해결하며, 대부분의 심각한 문제는 비표준 설정에서만 악용 가능하다. 임시 조치로 세션 업로드 진행 기능 비활성화를 권장하며, 관리자는 버전 확인 후 공식 패치 설치가 필수다.

**English Summary**: PHP security team announced critical updates for all supported versions on November 19, 2026, addressing multiple vulnerabilities including CVE-2026-115560 related to session upload progress. Most serious issues only affect non-default configurations, so not all applications are necessarily at risk. System administrators should verify their runtime version and install official patches as temporary workaround of disabling upload progress feature is insufficient.

**핵심 키워드**: PHP Security Team, CVE-2026-115560, session upload progress, PHP 8.6.0

### 3. [FastAPI + Async SQLAlchemy 2.0: N+1 쿼리와 블로킹 제거](https://dev.to/autolabsystem/fastapi-async-sqlalchemy-20-eliminating-n1-queries-and-blocking-event-loops-36o)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: Async FastAPI 애플리케이션에서 성능을 최적화하는 방법을 다룬다. SQLAlchemy 2.0의 비동기 세션에서 명시적인 selectinload() 또는 joinedload() 사용으로 N+1 쿼리 문제를 해결하고, 라우터-서비스-저장소 계층 분리와 표준화된 에러 처리(RFC 7807)를 통해 프로덕션 수준의 아키텍처를 구축한다.

**English Summary**: This tutorial addresses performance optimization in async FastAPI applications by preventing N+1 queries using explicit selectinload() and joinedload() in SQLAlchemy 2.0's async sessions. It emphasizes architectural best practices including separation of concerns (routers, services, repositories) and standardized error responses (RFC 7807 problem details) to prevent blocking event loops and maintain scalability.

**핵심 키워드**: FastAPI, SQLAlchemy 2.0, Uvicorn, async/await, MissingGreenlet

### 4. [AI API의 잘못된 JSON 응답 처리 방법](https://dev.to/_fde76ff2d01974642930b/how-to-fix-invalid-json-from-an-ai-api-2j0b)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: AI API로부터 받는 JSON 응답의 여러 오류 사례(불완전한 응답, 타입 불일치, 스키마 검증 실패)를 구분하여 처리하는 방법을 설명한다. 각 오류에 별도의 에러 코드를 할당하고, API 완료 상태를 확인한 후 완전한 텍스트를 파싱해야 한다는 점을 강조한다. 이를 통해 재시도로 인한 반복적인 문제를 방지할 수 있다.

**English Summary**: This article provides guidance on handling invalid JSON responses from AI APIs by distinguishing between different failure modes (incomplete responses, type mismatches, schema validation failures). It recommends assigning separate error codes to each failure type and checking API completion status before parsing to prevent masking parser errors with generic failures.

**핵심 키워드**: AI API, JSON validation, error codes, schema validation, Claude

### 5. [프로그래밍 SEO와 Supabase로 4시간에 1,200개 랜딩페이지 구축](https://dev.to/oxymoreservices/how-we-built-1200-seo-landing-pages-for-a-local-plumber-in-4-hours-programmatic-seo-supabase-3ci5)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: 개발자가 프로그래밍 SEO 기법과 Supabase를 활용하여 로스앤젤레스 배관업체를 위해 4시간 11분 만에 1,200개의 SEO 랜딩페이지를 자동 생성했다. 12개 서비스 × 100개 지역 조합으로 구성된 동적 페이지는 60일 후 1,089개가 인덱싱되었으며, 183개의 검색어에서 1페이지 순위를 달성했다.

**English Summary**: A developer successfully built 1,200 programmatic SEO landing pages for a Los Angeles plumbing business in 4 hours 11 minutes using Supabase and Next.js. The system dynamically generates pages combining 12 services × 100 neighborhoods, achieving indexing of 1,089 pages and first-page rankings for 183 keywords within 60 days.

**핵심 키워드**: Supabase, Next.js, Los Angeles plumbing client, programmatic SEO engine

### 6. [US/EU 지연 작업을 위한 웹훅 레이트 제한 큐 설계](https://dev.to/godfreysterling1574/webhook-rate-limiting-queue-design-for-useu-delayed-jobs-retry-and-dlq-4i2b)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: 웹훅 전송 시스템에서 큐는 단순한 전송 수단이며, 중복 방지, 테넌트 레이트 제한, 전송 증명은 애플리케이션 레벨에서 관리해야 한다. 불변 이벤트 ID를 부여하고 애플리케이션 원장에서 멱등성과 조정을 담당하여 프로세스 손실 시에도 이벤트 추적성을 보장해야 한다.

**English Summary**: In webhook delivery systems, durable queues handle transport while application ledgers must manage idempotency and reconciliation. The design pattern requires authenticating inbound webhooks, assigning immutable event IDs, durably recording minimal envelopes, and using the event ID as a uniqueness key to prevent duplicate business effects across US and EU deployments.

**핵심 키워드**: webhook delivery, queue design, event ID, dead-letter queue, rate limiting, US/EU deployments

### 7. [AI 실행 거버넌스: 멱등성 키가 보호하는 것과 보호하지 않는 것](https://dev.to/rain6fish/ai-execution-governance-part-13-the-key-protects-the-call-not-the-money-124a)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: 엔터프라이즈 시스템에서 AI 에이전트의 실제 작업(결제, 레코드 생성 등)을 관리하는 런타임에서 멱등성 키의 역할을 분석한다. 중단된 거래에서 예약이 해제되면 다른 키로 중복 결제가 가능할 수 있다는 사용자 질문을 통해, 세 가지 범위에서 '중복 결제 금지'를 구현하는 방식을 설명한다.

**English Summary**: This article examines idempotency keys in an AI runtime system that executes real actions in enterprise systems. It explores what idempotency keys actually protect against duplicate payments and explains the three scopes for implementing 'don't pay twice' logic: single call, conversation-level, and system-level protections.

**핵심 키워드**: idempotency key, AI agents, enterprise systems, payment timeout, request deduplication

### 8. [AI 비디오 생성은 마법이 아닌 분산 시스템](https://dev.to/germey/your-ai-video-pipeline-is-a-distributed-system-not-a-magic-button-512i)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: AI 비디오 생성 도구는 단순한 프롬프트 입력 후 출력을 받는 것처럼 보이지만, 실제 제품 환경에서는 사용자 중단, 렌더링 지연, 중복 웹훅, 버전 관리 등 많은 복잡한 문제가 발생한다. 비디오 생성보다 중요한 것은 대기, 실패, 수정, 인간의 판단을 견딜 수 있는 견고한 시스템을 구축하는 것이며, AI 비디오 도구를 동기식 미디어 엔드포인트가 아닌 분산 빌드 시스템으로 이해해야 한다.

**English Summary**: AI video generation appears simple in demos but requires complex infrastructure in production to handle user interruptions, failures, webhooks, and revisions. The key insight is treating AI video tools as distributed build systems rather than synchronous endpoints, where prompts imply multiple interdependent components like scripts, timing, music, and rendering that must be managed as durable tasks rather than blocking requests.

**핵심 키워드**: AI video tools, distributed systems, HTTP requests, durable task identifiers, production pipeline

### 9. [베트남 공항 시스템으로 배우는 트래픽 스파이크 엔지니어링](https://dev.to/saintzzz/building-travel-tooling-taught-me-what-tet-does-to-vietnams-airports-li3)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: 개발자가 베트남 설날(Tet) 기간 공항 혼잡도를 분석하면서 얻은 엔지니어링 교훈을 소개한다. 국내 항공편은 300%, 국제편은 60% 급증하며, 항공사 운항 일정에 따라 승객이 집중되는 특성을 가진 버스티 시스템으로 모델링할 수 있다. 평균 부하보다 피크 시간대 동시성을 중심으로 설계해야 한다는 시스템 확장 원리를 적용할 수 있다.

**English Summary**: A developer shares engineering lessons learned from analyzing Vietnam's airport congestion during Tet (lunar new year), where domestic passenger volumes spike 300% and international traffic rises 60%. The article models airports as bursty queueing systems where peak concurrency and downstream capacity matter more than average load, drawing parallels to scaling web services during traffic spikes.

**핵심 키워드**: Vietnam airports, Tet holiday, traffic spike modeling, queueing systems

### 10. [API 보안: WAF 규칙과 애플리케이션 인증의 올바른 조합](https://dev.to/_eb0609572b9efcf27472066/waf-rules-alone-vs-application-authorization-how-to-protect-an-api-from-broken-object-level-14n2)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: 본 문서는 WAF(Web Application Firewall) 규칙만으로는 부족하며 애플리케이션 레벨의 인증 및 인가가 함께 필요함을 설명합니다. 비정상적인 객체 레벨 접근 차단, SSRF 방지, 봇 트래픽 탐지, 경로 순회 및 XXE 공격 대응 등 다양한 보안 위협에 대한 WAF 배치 및 구성 전략을 다룹니다.

**English Summary**: This comprehensive guide discusses API security strategies focusing on combining WAF rules with application-level authorization controls. It covers various deployment scenarios including SSRF detection, bot traffic filtering, injection attack prevention, and proper WAF placement in network architecture to effectively protect internet-facing applications.

**핵심 키워드**: Web Application Firewall, Object Level Authorization, API protection, Security deployment

### 11. [API의 BOLA와 IDOR: 크로스스토어 주문 접근 테스트](https://dev.to/nusantarasecure/bola-dan-idor-pada-api-menguji-akses-pesanan-antar-toko-659)
**출처**: Dev.to API · **중요도**: 높음

**한국어 요약**: 본 문서는 API 보안 취약점인 BOLA(Broken Object Level Authorization)와 IDOR(Insecure Direct Object References)를 설명하고, 멀티스토어 주문 시스템에서 인증된 사용자가 다른 스토어의 주문에 접근하는 취약점을 테스트하는 방법론을 제시한다. OWASP API 보안 가이드를 기반으로 인증과 인가의 차이를 구분하고, 실제 테스트 환경에서의 체계적인 취약점 검증 절차를 소개한다.

**English Summary**: This article explains API security vulnerabilities BOLA (Broken Object Level Authorization) and IDOR (Insecure Direct Object References), demonstrating how authenticated users can access orders from other stores without proper authorization checks. It provides a methodology for testing authorization flaws in multi-store ordering systems based on OWASP guidelines, distinguishing between authentication and authorization concepts.

**핵심 키워드**: BOLA, IDOR, OWASP API1:2023, API authorization, multi-store ordering

### 12. [SafeLine을 활용한 API 인증 우회 공격 방어 가이드](https://dev.to/lialiago/how-to-protect-an-api-from-broken-object-level-authorization-with-safeline-adj)
**출처**: Dev.to API · **중요도**: 높음

**한국어 요약**: API의 Broken Object Level Authorization (BOLA) 취약점은 유효한 사용자 토큰으로도 특정 객체 접근 권한을 검증하지 않아 발생합니다. 공격자는 URL의 객체 ID를 변조하거나 자동화된 추측을 통해 무단 접근, 수정, 삭제를 수행할 수 있습니다. SafeLine은 리버스 프록시로 작동하는 자체 호스팅 WAF(웹 애플리케이션 방화벽)로서 HTTP 트래픽을 필터링하고 모니터링하여 인가 결정을 지원합니다.

**English Summary**: The article explains Broken Object Level Authorization (BOLA), an API vulnerability where valid authentication succeeds but authorization checks fail for specific objects. Attackers can manipulate object IDs in requests to gain unauthorized access. SafeLine, a self-hosted Web Application Firewall operating as a reverse proxy, can help protect APIs by filtering and monitoring HTTP traffic to enforce authorization policies.

**핵심 키워드**: SafeLine, BOLA, WAF, API security, reverse proxy, authorization
