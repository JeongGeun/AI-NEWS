---
layout: post
title: "2026-07-19 백엔드 데일리 브리핑"
date: 2026-07-19 00:07:00 +0900
categories: [backend]
tags:
  - API
  - API alternative
  - Apify
  - Directions
  - Google Maps
  - Google Play
  - JSON
  - Kafka
  - Kubernetes
  - Odin platform
  - OpenSearch
  - PostgreSQL
  - Redis
  - Route Planning
  - SQL
  - Spring Boot
  - agentic AI
  - asynchronous
  - backend architecture
  - backend-engineering
---

> 수집 시각: 2026-07-18 22:12 UTC | 총 13건

## 튜토리얼 & 아티클

### 1. [클라우드 네이티브 인프라, 신뢰할 수 있는 에이전틱 AI의 기초로 부상](https://www.infoq.com/news/2026/07/cncf-trustworthy-agentic-ai/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 높음

**한국어 요약**: CNCF의 새로운 기술 분석에 따르면, 에이전틱 AI의 미래는 완전히 새로운 인프라가 아닌 기존의 성숙한 클라우드 네이티브 생태계 위에 구축될 것으로 예상된다. Kubernetes, OpenTelemetry, Dapr, SPIFFE, Falco, Kafka, GitOps 등의 기술들이 AI 에이전트에 필요한 오케스트레이션, 가시성, 보안, 복원력, 거버넌스 등을 제공한다. 에이전틱 시스템은 본질적으로 추가적인 추론 능력을 가진 분산 시스템이며, 클라우드 네이티브 생태계가 지난 10년간 해결해온 문제들이 자율 AI 시스템의 과제와 일치한다.

**English Summary**: The CNCF argues that autonomous AI systems should be built on mature cloud-native infrastructure rather than entirely new architectures. Kubernetes, OpenTelemetry, Dapr, SPIFFE, Falco, Kafka, and GitOps collectively provide orchestration, observability, identity management, security, and governance capabilities that autonomous agents require. Agentic systems are fundamentally distributed systems with reasoning capabilities, and cloud-native technologies already address their operational challenges.

**핵심 키워드**: CNCF, Kubernetes, OpenTelemetry, Dapr, SPIFFE, Falco, Kafka, GitOps

### 2. [우버의 존 장애 복원력 OpenSearch 클러스터 구축 방법](https://www.infoq.com/news/2026/07/uber-opensearch-zone-failure/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 보통

**한국어 요약**: 우버는 OpenSearch의 샤드 할당 기능과 자체 격리 그룹 시스템을 결합하여 존 장애 시에도 쿼리와 데이터 수집 기능을 유지하는 방식을 개발했습니다. 물리적 존 간 노드 수 불균형 문제를 해결하기 위해 격리 그룹을 논리 계층으로 도입하여, 각 그룹이 동일한 노드 수를 보장받도록 했습니다. 이 설계는 전체 존 장애와 추가 노드 1개 장애를 동시에 견딜 수 있습니다.

**English Summary**: Uber developed a zone-failure-resilient OpenSearch architecture using isolation groups as a logical layer between physical failure domains and OpenSearch's shard allocation logic. By ensuring equal node distribution across isolation groups regardless of underlying physical zones, the system maintains cluster stability during complete zone outages while preventing data loss and unassigned shards.

**핵심 키워드**: Uber, OpenSearch, Odin, isolation groups

### 3. [버전 관리 SQL 데이터베이스 Dolt 2.0 출시, 자동 저장소 정리 및 압축 기능 추가](https://www.infoq.com/news/2026/07/dolt-version-control/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)
**출처**: InfoQ · **중요도**: 높음

**한국어 요약**: DoltHub이 Git 스타일 버전 관리 기능을 갖춘 MySQL 호환 SQL 데이터베이스 Dolt의 2.0 버전을 출시했다. 주요 업데이트는 자동 가비지 컬렉션, 아카이브 압축(30-50% 저장소 감소), 벡터 데이터 타입 베타 지원, 성능 개선 등이다. Prolly Trees 기반의 행 수준 버전 관리와 효율적인 구조 공유로 빠른 diff와 merge를 지원한다.

**English Summary**: DoltHub released Dolt 2.0, a version-controlled SQL database with Git-like capabilities. The major update includes automatic garbage collection, archive compression reducing storage by 30-50%, vector data support in beta, and performance improvements claiming faster speeds than MySQL on sysbench benchmarks.

**핵심 키워드**: DoltHub, Dolt 2.0, Tim Sehn, MySQL, Prolly Trees

## 커뮤니티

### 1. [매트릭스처럼 쿼리 최적화하기: PostgreSQL 인덱싱 전략](https://dev.to/timevolt/indexing-like-a-neo-dodging-slow-queries-in-the-matrix-357k)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: PostgreSQL 레이트 리미터 서비스에서 수백만 행의 느린 쿼리 문제를 해결한 사례 연구. user_id와 created_at 두 열을 활용한 복합 인덱스 설계로 풀 테이블 스캔을 범위 스캔으로 전환하여 성능을 대폭 개선. 인덱스는 마법이 아닌 정밀한 도구임을 강조하며 올바른 인덱싱 전략의 중요성을 설명.

**English Summary**: A developer shares their experience optimizing a PostgreSQL rate-limiter service experiencing slow queries on a multi-million row table. By understanding how indexes work and implementing a compound index on user_id and created_at columns, they transformed slow full table scans into fast range lookups. The article emphasizes that indexes are precise tools requiring proper design rather than blanket solutions.

**핵심 키워드**: PostgreSQL, compound index, rate-limiter service, query optimization

### 2. [프로그래밍에서 하루가 86,400초가 아닌 이유](https://dev.to/doogal/why-a-day-isnt-86400-seconds-in-programming-10ma)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: 소프트웨어 개발에서 하루를 정확히 86,400초로 가정하면 심각한 버그가 발생한다. 시간은 수학적 개념이 아니라 정치적 구성물로, 일광절약시간, 정부의 시간대 변경, 복잡한 윤년 규칙 등으로 인해 개발자는 시간 계산을 하드코딩하지 말고 검증된 시간 라이브러리를 사용해야 한다.

**English Summary**: Hardcoding a day as exactly 86,400 seconds is a dangerous assumption in software engineering that breaks during daylight savings time and other government-mandated time changes. Time is a political construct rather than a mathematical constant, making it essential for developers to use well-maintained time libraries instead of fixed time calculations.

**핵심 키워드**: Daylight Savings Time, cron jobs, time zone shifts, leap years

### 3. [Redis가 정확히 16,384개의 슬롯을 사용하는 이유](https://dev.to/daksh-gargas/why-redis-splits-into-exactly-16384-slots-a-deep-dive-into-distributed-systems-design-4bgh)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: Redis 클러스터가 모든 구성에서 정확히 16,384개의 해시 슬롯을 사용하는 기술적 설계 이유를 심층 분석한 글입니다. Redis 창시자 Salvatore Sanfilippo의 설계 결정 배경을 단일 인스턴스부터 분산 시스템까지의 진화 과정을 통해 설명합니다. 메모리 구조, 네트워크 물리학, 수학적 근거를 포함한 분산 시스템 설계의 실제 사례를 제시합니다.

**English Summary**: This article explores why Redis Cluster uses exactly 16,384 hash slots across all deployments, regardless of cluster size. The author analyzes Redis creator Salvatore Sanfilippo's design decision by tracing the technical evolution from single-instance to distributed systems, examining memory structures, network physics, and mathematical foundations behind this specific number choice.

**핵심 키워드**: Redis, Salvatore Sanfilippo, 16,384 slots, hash slots, cluster architecture

### 4. [벡터 데이터베이스가 백만 개 벡터를 효율적으로 검색하는 방법](https://dev.to/dilip_v_p/how-vector-databases-search-a-million-vectors-without-checking-a-million-2ee1)
**출처**: Dev.to Backend · **중요도**: 높음

**한국어 요약**: 벡터 데이터베이스는 단어나 문장을 고차원 공간의 점으로 변환하여 의미론적 유사성 검색을 가능하게 한다. 코사인 유사도를 통해 벡터 간 거리를 측정하며, 전체 벡터를 순회하는 브루트포스 방식 대신 효율적인 인덱싱 기법을 사용하여 백만 개 이상의 벡터에서도 빠른 검색을 수행한다.

**English Summary**: Vector databases convert words and sentences into points in high-dimensional space using embedding models, enabling semantic similarity search through cosine similarity measurements. Rather than brute-force comparison of all vectors, these databases use optimized indexing techniques to efficiently find nearest neighbors in million-scale vector collections.

**핵심 키워드**: Vector Databases, Embeddings, Cosine Similarity, SentenceTransformer, Nearest Neighbor Search

### 5. [동기식 vs 비동기식 작업: 현대 시스템이 대기할 수 없는 이유](https://dev.to/anik_sikder_313/synchronous-vs-asynchronous-workloads-why-modern-systems-cannot-afford-to-wait-7fo)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: 이 글은 동기식 통신과 비동기식 통신의 차이를 설명합니다. 동기식 통신은 요청의 생명주기가 작업의 생명주기와 결합되어 사용자가 즉시 응답을 기다리는 방식이고, 비동기식 통신은 이를 분리하여 시스템 성능을 향상시킵니다. 현대 시스템에서는 모든 작업이 사용자를 대기시킬 수 없으므로 두 패턴을 적절히 활용해야 합니다.

**English Summary**: This article explains the distinction between synchronous and asynchronous workloads in modern software systems. Synchronous communication couples request lifetime with work lifetime, requiring immediate user responses for dependent operations. The article argues that modern systems cannot afford to wait for all operations, necessitating strategic use of both patterns.

**핵심 키워드**: synchronous communication, asynchronous workloads, API design, request-response pattern

### 6. [OrderHub Day 27: 이벤트 기반 결제 서비스 구현](https://dev.to/dev48v/orderhub-day-27-a-payment-service-thats-triggered-by-an-event-and-answers-with-an-event-35hh)
**출처**: Dev.to Backend · **중요도**: 보통

**한국어 요약**: 개발자가 이벤트 기반 전자상거래 백엔드 'OrderHub'를 구축하는 과정을 다룬 글입니다. Day 27에서는 결제 서비스(payment-service)가 'order-placed' 이벤트를 구독하고 'PaymentProcessed' 이벤트를 발행하는 양방향 이벤트 기반 아키텍처를 구현했습니다. Spring Boot의 Kafka 컨슈머 그룹을 활용하여 기존 서비스 수정 없이 새로운 서비스를 확장하는 방식을 보여줍니다.

**English Summary**: This article documents Day 27 of building OrderHub, an event-driven e-commerce backend. The payment-service is implemented as a fully event-driven microservice that subscribes to order-placed events and publishes PaymentProcessed events, demonstrating choreography saga pattern. The architecture allows extending the system without modifying existing services, using Kafka consumer groups for independent event processing.

**핵심 키워드**: OrderHub, payment-service, Spring Boot, Kafka, choreography saga

### 7. [Google Play 데이터 스크래핑 가이드 (2026)](https://dev.to/l0gi0ver/how-to-scrape-google-play-free-no-code-guide-2026-4fhb)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: 공식 API 없이 Google Play 앱 데이터를 대규모로 수집하는 방법을 소개하는 가이드입니다. Apify 플랫폼의 호스팅 스크래퍼를 활용하여 코드 작성 없이 또는 Node.js, Python으로 앱 정보, 리뷰, 평점 등의 데이터를 JSON, CSV, Excel 형식으로 추출할 수 있습니다. 로그인, 프록시, 리버스 엔지니어링이 필요 없으며 무료 Apify 토큰으로 시작 가능합니다.

**English Summary**: This guide demonstrates how to scrape Google Play app data at scale without an official API using Apify's hosted scraper. Users can extract structured data including app titles, developers, ratings, installs, and reviews in multiple formats (JSON, CSV, Excel) with either no-code or simple programmatic approaches using Node.js or Python.

**핵심 키워드**: Apify, Google Play, google-play-data-api, Dev.to

### 8. [2026년 최고 인기 여행 API 및 스크래퍼 10개 (활성 사용자 기준)](https://dev.to/nick_davies_323125afbb05c/top-10-travel-apis-scrapers-in-2026-ranked-by-active-users-1eg9)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: Apify 플랫폼에서 활성 사용자 수를 기준으로 순위를 매긴 상위 10개의 여행 관련 API 및 스크래퍼 도구를 소개합니다. Google Maps Scraper(516K 사용자)가 1위이며, Google Maps Reviews Scraper, Google Maps Extractor 등이 상위를 차지합니다. Booking.com, Airbnb 등 주요 여행 예약 서비스의 데이터 추출 도구들도 포함되어 있습니다.

**English Summary**: A ranked list of the top 10 travel APIs and scrapers in 2026 based on active users on the Apify platform. Google Maps Scraper leads with 516K users (4.7/5 rating), followed by Google Maps Reviews Scraper and Google Maps Extractor. The list includes data extraction tools for Booking.com, Airbnb, and other major travel platforms.

**핵심 키워드**: Google Maps Scraper, Booking.com, Airbnb, Apify, API ranking

### 9. [Google Cloud 키 없이 Google Maps Directions API 사용하기](https://dev.to/trufflepig/google-maps-directions-api-without-a-google-cloud-key-routes-and-etas-as-json-2026-c5h)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: Google Maps Directions API를 직접 사용하려면 Google Cloud 프로젝트, API 키, 결제 설정 등 복잡한 과정이 필요합니다. 이 글은 Apify의 Google Maps Directions API Actor를 활용하여 Google Cloud 키 없이도 경로, 소요 시간, 단계별 지침을 JSON으로 간편하게 얻을 수 있는 방법을 소개합니다. 탐색적 또는 대량 작업에 더 적합한 대안으로 제시됩니다.

**English Summary**: The article explains how to access Google Maps route data (distance, ETA, turn-by-turn directions) using Apify's Directions API Actor without needing a Google Cloud project, API key, or billing setup. It presents this as a simpler alternative for developers who need structured JSON route data for exploratory or batch work, bypassing Google's complex infrastructure requirements.

**핵심 키워드**: Google Maps Directions API, Apify, Google Cloud

### 10. [10,469개 VC·엔젤·PE펀드 필터링 가능한 투자자 데이터 API](https://dev.to/trufflepig/investor-database-api-filter-10469-vc-angel-and-pe-firms-as-json-in-2026-3m9m)
**출처**: Dev.to API · **중요도**: 보통

**한국어 요약**: Apify의 Startup Investors Data Scraper는 10,469개 투자 펀드 정보를 JSON 형식으로 제공하는 쿼리 가능한 데이터베이스다. 펀드 유형, 섹터, 투자 단계, 국가별 필터링이 가능하며, 파트너 연락처 정보도 포함된다. 창업자들이 Crunchbase 등에서 수동으로 투자자 리스트를 작성하던 번거로움을 해결하는 솔루션이다.

**English Summary**: Apify's Startup Investors Data Scraper provides a queryable database of 10,469 investment firms returned as JSON, filterable by firm type, sector, investment stage, and country. Unlike commercial databases behind paywalls, this solution offers accessible bulk investor data with contact information for founders seeking funding sources efficiently.

**핵심 키워드**: Apify, Startup Investors Data Scraper, Crunchbase
