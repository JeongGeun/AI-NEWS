---
layout: post
title: "2026-11-19 프론트엔드 데일리 브리핑"
date: 2026-11-19 00:07:00 +0900
categories: [frontend]
tags:
  - A/B Testing
  - AI development tools
  - API
  - Apps Script
  - Chrome Extension
  - Educational Technology
  - Gemini Nano
  - Google Forms
  - Implementation
  - JavaScript
  - Manifest V3
  - On-Device AI
  - Policy Compliance
  - Quiz Scoring
  - Remote Configuration
  - audio-editing
  - backend infrastructure
  - browser-based
  - coding tutorial
  - cost analysis
---

> 수집 시각: 2026-11-19 02:34 UTC | 총 9건

## 커뮤니티

### 1. [Chrome 확장 프로그램에서 온디바이스 AI 실행하기: Prompt API 3단계 가이드](https://dev.to/extensionbooster/prompt-api-3-steps-to-on-device-ai-in-chrome-extensions-46kj)
**출처**: Dev.to JavaScript · **중요도**: 높음

**한국어 요약**: Chrome Prompt API를 활용하여 Gemini Nano 모델을 사용자 기기에서 직접 실행할 수 있습니다. API 키, 토큰 비용, 데이터 외부 전송이 필요 없으며 오프라인에서도 작동합니다. 하드웨어 요구사항(Windows 10/11, macOS 13+, 22GB 디스크, 16GB RAM)을 확인한 후 3단계로 첫 프롬프트를 구현할 수 있습니다.

**English Summary**: The Chrome Prompt API enables running Gemini Nano directly on users' devices without API keys, per-request billing, or data leaving the browser. This eliminates cloud costs, latency, offline limitations, and rate-limiting issues. The article provides a 3-step implementation guide with hardware requirements (Windows 10/11, macOS 13+, Chrome 138+, 22GB disk, 16GB RAM).

**핵심 키워드**: Chrome Prompt API, Gemini Nano, ExtensionBooster, LanguageModel API

### 2. [Google Forms에서 Apps Script로 감점 채점 구현하기](https://dev.to/facilodev/negative-marking-in-google-forms-with-apps-script-2035)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: Google Forms는 기본적으로 정답만 점수를 주고 오답과 공란을 같게 처리한다. 많은 실제 시험처럼 오답에 감점을 적용해야 할 경우, Apps Script의 FormApp API를 활용하여 답안지를 읽고 각 응답에 음수 점수를 할당한 후 결과를 저장함으로써 감점 채점을 구현할 수 있다. Nota Justa라는 애드온을 개발하여 이 기능을 Forms 내에서 직접 처리하는 방식을 소개한다.

**English Summary**: Google Forms' default scoring system awards points only for correct answers, treating wrong and blank answers identically. This article demonstrates how to implement negative marking using Apps Script's FormApp API, allowing educators to penalize incorrect responses as required by many standardized tests. The approach involves reading the answer key, determining response correctness, and writing negative scores back to responses.

**핵심 키워드**: Google Forms, Apps Script, FormApp API, Nota Justa, JavaScript

### 3. [오픈소스 오피스 스위트 Radii Office, Writeout 문서 편집기 출시](https://dev.to/patientduck394/radii-office-an-open-source-office-suite-with-tons-of-capabilities-2afn)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: Radii Office는 Writeout이라는 무료 오픈소스 문서 작성 도구를 선보였다. 자체 포맷팅 언어인 Keydown을 통해 18,000개 이상의 스타일을 제공하며, 기호 입력으로 빠르게 스타일을 적용할 수 있다. 개발자들은 GitHub에서 프로젝트를 지원할 수 있으며, 더 나은 사용자 경험을 위해 피드백을 제공할 수 있다.

**English Summary**: Radii Office introduces Writeout, a free open-source document editor featuring Keydown, a custom formatting language with over 18,000 styles. Users can quickly apply styles using symbol shortcuts (e.g., #C# creates cyan highlights). The project encourages community support through GitHub starring and welcomes user feedback.

**핵심 키워드**: Radii Office, Writeout, Keydown, GitHub

### 4. [MV3에서 정책 준수하며 Chrome 확장 프로그램 A/B 테스트 구현하기](https://dev.to/extensionbooster/chrome-extension-ab-testing-in-mv3-without-breaking-policy-3al6)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: Chrome 웹 스토어의 Manifest V3 정책을 준수하면서 Chrome 확장 프로그램에서 A/B 테스트를 실행하는 방법을 소개합니다. 핵심은 모든 변형 코드를 빌드에 포함하고 원격 설정으로만 실험을 활성화/비활성화하는 것으로, 이는 원격 코드 실행으로 보이지 않아 정책 검토를 통과할 수 있습니다. 각 설치에 고유한 ID를 부여하고 가중치를 조정하여 실제 실험을 진행할 수 있습니다.

**English Summary**: The article explains how to implement A/B testing in Chrome extensions while complying with Manifest V3 policy restrictions. The key approach is shipping all variant code within the extension package and using remote configuration only to toggle experiments on/off and adjust weights—avoiding the appearance of remote code execution. This policy-safe design works across Chrome, Edge, and Firefox without triggering review rejection.

**핵심 키워드**: Chrome Web Store, Manifest V3, Firefox AMO, Microsoft Edge, A/B Testing

### 5. [JavaScript String replace() 함수: 문자열 텍스트 교체 방법](https://dev.to/code1/javascript-string-replace-function-replacing-text-in-a-string-7fl)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: JavaScript의 replace() 함수는 문자열에서 특정 부분을 찾아 다른 문자열로 교체하는 기능을 제공합니다. 부분 문자열이나 정규표현식 패턴을 사용하여 검색하며, 기본적으로 첫 번째 매칭만 교체하지만 'g' 플래그를 사용하면 모든 매칭을 교체할 수 있습니다. 원본 문자열은 변경되지 않고 새로운 문자열이 반환됩니다.

**English Summary**: The JavaScript replace() function searches for a specific substring or regular expression pattern in a string and replaces it with a new value. By default, only the first match is replaced, but the 'g' flag in regex patterns enables replacing all matches. The original string remains unchanged and a new string is returned.

**핵심 키워드**: JavaScript, replace(), regular expression, Dev.to

### 6. [Shopify 스토어에 음성 AI 통합하는 방법](https://dev.to/voice_developer/how-to-integrate-voice-ai-with-shopify-stores-4nn1)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: 본 가이드는 ElevenLabs의 텍스트-음성 변환(TTS) 서비스를 활용하여 Shopify 스토어에 음성 AI 기능을 통합하는 방법을 설명합니다. 음성 AI를 통해 사용자는 손을 사용하지 않고 제품 정보를 청취할 수 있으며, 브랜드 음성 클로닝으로 개인화된 경험을 제공합니다. Node.js 또는 Python 백엔드와 ElevenLabs API를 연결하여 제품 제목, 설명, 고객 리뷰를 음성으로 재생하는 위젯을 구축할 수 있습니다.

**English Summary**: This tutorial demonstrates how to integrate voice AI into Shopify stores using ElevenLabs' text-to-speech service to enable hands-free product browsing and personalized audio narration. The guide covers prerequisites including a Shopify storefront, Node.js/Python backend, ElevenLabs API key, and ngrok tunnel setup to create a functional voice widget for reading product information aloud.

**핵심 키워드**: ElevenLabs, Shopify, Text-to-Speech (TTS), Storefront API, Voice Cloning

### 7. [게임 'RIFTFIRE' 플레이가마로 이전, 'Null Point'로 재명명](https://dev.to/kehinde_owolabi_e2e54567a/riftfire-is-now-null-point-live-on-playgama-1i7o)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: CrazyGames 거절 후 레이캐스트 FPS 게임 RIFTFIRE가 Playgama 플랫폼으로 이전하며 'Null Point'로 새롭게 명명됐다. 게임명 변경은 기존 동명 게임으로 인한 검색 가시성 문제와 더 강한 장르명 필요성 때문이다. 개선된 빌드와 함께 플레이가마에서 즉시 플레이 가능하다.

**English Summary**: RIFTFIRE, a raycast FPS game, has been rebranded as 'Null Point' and published on Playgama platform after being rejected by CrazyGames. The rename was driven by discoverability issues with the original name and a stronger thematic fit for the genre. The game maintains its core features with 360 levels and multiple weapons, now live on Playgama.

**핵심 키워드**: RIFTFIRE/Null Point, Playgama, CrazyGames, Limn Engine, PlaygamaMCP

### 8. [WordPress에서 Lovable + Supabase로 전환한 6개월 성과 분석](https://dev.to/oxymoreservices/why-we-replaced-our-freelance-wordpress-stack-with-lovable-supabase-6-month-numbers-1fg9)
**출처**: Dev.to WebDev · **중요도**: 보통

**한국어 요약**: 웹 개발사가 WordPress 기반 스택을 Lovable + Supabase + Vercel로 교체한 결과를 공개했다. 기존 스택은 월 $480의 비용이 들었지만 숨겨진 지원 비용이 연 $1,632에 달했으며, 성능 점수도 모바일 42점으로 낮았다. AI 기반 React/Next.js 생성 도구와 Postgres 기반 백엔드 솔루션으로 전환하여 생산성과 유지보수성을 대폭 개선했다.

**English Summary**: A web development agency replaced its WordPress + Elementor + WPEngine stack with Lovable + Supabase + Vercel for small business clients. While the old stack's direct costs were $480/year per client, hidden support costs averaged $1,632/year due to plugin conflicts and updates. The new AI-assisted stack using React/Next.js scaffolding and Postgres-based backend significantly reduced maintenance burden and improved performance scores.

**핵심 키워드**: Lovable, Supabase, Vercel, WordPress, React, Next.js, Postgres

### 9. [브라우저에서 무료로 산악 호수 영상 오디오 편집하기](https://dev.to/zjch022/how-to-trim-audio-for-a-mountain-lake-video-free-in-your-browser-4f1e)
**출처**: Dev.to WebDev · **중요도**: 낮음

**한국어 요약**: 산악 지역 영상 촬영 시 바람 소음과 오디오 길이 문제를 해결하기 위해 AudioCutter 같은 브라우저 기반 도구를 사용하여 간단히 오디오를 편집할 수 있다. 이 방법은 별도 소프트웨어 설치 없이 로컬에서 처리되므로 파일 업로드 걱정이 없다. 정밀한 편집으로 의도된 결과물을 만들 수 있다.

**English Summary**: The article provides a practical guide on trimming audio for mountain lake videos using browser-based tools like AudioCutter. It explains common audio problems in outdoor recordings—wind noise and mismatched music length—and demonstrates how to solve them using free, in-browser audio editing without installing software.

**핵심 키워드**: AudioCutter, audio trimming, mountain filming, browser-based editing
