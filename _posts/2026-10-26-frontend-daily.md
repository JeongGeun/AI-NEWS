---
layout: post
title: "2026-10-26 프론트엔드 데일리 브리핑"
date: 2026-10-26 00:07:00 +0900
categories: [frontend]
tags:
  - 2D rendering
  - Android
  - Astro
  - CSS
  - Express
  - Framer
  - JavaScript
  - JavaScript optimization
  - LLM-tooling
  - Next.js
  - Nginx
  - UI-component
  - Unicode
  - WordPress migration
  - algorithm design
  - analytics
  - bill splitting
  - bug fix
  - calculator-library
  - charting
---

> 수집 시각: 2026-10-25 23:38 UTC | 총 10건

## 커뮤니티

### 1. [JavaScript에서 금액 분할 시 발생하는 반올림 오류 해결법](https://dev.to/mercerk17/split-a-bill-three-ways-without-losing-a-cent-2mb7)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: JavaScript의 부동소수점 연산에서 $103.25를 3명이 나눌 때 toFixed() 함수 사용으로 인해 1센트 오류가 발생하는 문제를 다룬다. 정수 센트 단위로 작업한 후 몫과 나머지를 이용해 분배하는 해결 방법을 제시한다. 이 방식은 모든 결과의 합이 원래 금액과 정확히 일치하고 개인 간 차이를 최소화한다.

**English Summary**: The article demonstrates a floating-point arithmetic bug in JavaScript where splitting $103.25 three ways using toFixed() results in a total of $103.26. It provides a solution using integer cent arithmetic with a base amount distribution plus remainder handling, ensuring the sum always equals the original total with minimal per-person variance.

**핵심 키워드**: Dev.to, Node 22, toFixed(), Math.floor()

### 2. [브라우저에서 스프라이트 애니메이션이 느린 이유](https://dev.to/h0dson/why-moving-sprites-are-slow-in-the-browser-55gg)
**출처**: Dev.to JavaScript · **중요도**: 높음

**한국어 요약**: GPU는 수백만 개의 스프라이트를 그릴 수 있지만, 대부분의 브라우저 게임은 수만 개 수준에서 성능이 저하된다. 문제는 GPU가 아니라 JavaScript의 오버헤드다. 개발팀이 만든 오픈소스 2D 렌더러 'spryte'는 기존의 PixiJS보다 2-4배 빠른 성능을 보여주며, 프레임당 16.7ms 예산 내에서 각 스프라이트의 JavaScript 처리 비용을 최소화하는 것이 핵심이다.

**English Summary**: Browser games struggle to render tens of thousands of sprites due to JavaScript overhead, not GPU limitations. A new open-source 2D renderer called 'spryte' achieves 2-4x faster sprite rendering than PixiJS by optimizing how much JavaScript work each sprite requires, addressing the bottleneck of describing sprites to the GPU within the 16.7ms per-frame budget at 60Hz.

**핵심 키워드**: spryte, PixiJS, GPU, 2D renderer, JavaScript

### 3. [브라우저가 키보드 감지 실패할 때의 해결책](https://dev.to/marya1994/when-the-browser-doesnt-tell-you-the-keyboard-is-open-490o)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: Android 15의 edge-to-edge 기본 설정으로 인해 일부 저가형 휴대폰의 기본 브라우저에서 소프트 키보드 열림을 감지하지 못하는 문제가 발생했다. 브라우저가 resize 이벤트나 visualViewport 변화를 보고하지 않아 페이지가 키보드 표시를 알 수 없었다. 개발자는 텍스트 필드 포커스 후 짧은 대기 시간 후 높이 변화를 감지하지 못하면 키보드가 열린 것으로 가정하고 시트를 화면 상단으로 이동시키는 해결책을 제시했다.

**English Summary**: Android 15's edge-to-edge rendering breaks keyboard detection in budget phone browsers that use Android System WebView, as resize events and visualViewport changes are not reported. The author proposes a pragmatic workaround: assuming the keyboard is open after detecting focus on a text field with no viewport height change, then repositioning UI elements above the predicted keyboard area.

**핵심 키워드**: Android 15, Android System WebView, visualViewport API, Redmi phone, bottom sheets

### 4. [npm 의존성 없이 만든 소셜 사이트, 고양이 CEO가 운영](https://dev.to/yupthatscole/i-built-a-little-social-site-with-zero-npm-dependencies-and-a-cat-runs-it-4lo3)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: 개발자가 Node.js 22의 기본 라이브러리만 사용하여 GeoCities/MySpace 스타일의 소셜 플랫폼 'catcloud'를 개발했습니다. 사용자는 개인 페이지를 자유롭게 꾸밀 수 있으며, 게스트북, 픽셀 게임, 실시간 채팅 등의 기능을 제공합니다. Cloudflare Workers 무료 플랜에서 SQLite 데이터베이스로 운영되며, HTML/CSS 작성 시 iframe과 Content-Security-Policy로 보안을 확보합니다.

**English Summary**: A developer built catcloud, a social platform with zero npm dependencies using only Node.js 22 built-ins, featuring customizable personal pages, pixel art games, and live hangout rooms. The application runs on Cloudflare Workers' free tier with SQLite backend and employs iframe sandboxing with strict Content-Security-Policy to safely allow user-written HTML/CSS.

**핵심 키워드**: catcloud, Node.js 22, Cloudflare Workers, SQLite, Durable Object, Content-Security-Policy

### 5. [사용자 정의 대시보드 구축 라이브러리 @datastripes/dashboard](https://dev.to/superior_studio_d5ebd0d6f/let-your-users-to-build-their-own-dashboards-in-your-app-2k9c)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: @datastripes/dashboard는 사용자가 직접 대시보드를 구성할 수 있는 JavaScript 패키지입니다. 그리드 시스템, 차트 카탈로그, 필터링, 레이아웃 저장 등의 기능을 포함하며, React, Vue, Angular, Web Components 등 주요 프레임워크를 지원합니다. JSON 설정 기반으로 작동하며 선택적 peer dependency 구조로 설계되어 있습니다.

**English Summary**: @datastripes/dashboard is a multi-framework JavaScript package that enables users to build and customize dashboards within applications. It provides grid systems, chart widgets, filtering, and layout persistence through a JSON-based configuration, with support for React 19, Vue 3.4+, Angular 18-19, and Web Components.

**핵심 키워드**: @datastripes/dashboard, React, Vue, Angular, Web Components

### 6. [LLM 비용 계산기를 포함한 DevKit: 검증된 공식의 원파일 계산기 라이브러리](https://dev.to/astrodevkit/devkit-a-one-file-calculator-library-with-tested-formulas-now-with-an-llm-cost-calculator-4c8k)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: 개발자 DevKit은 69개의 도구를 포함한 경량 계산기 라이브러리로, 모든 기능이 브라우저에서 클라이언트 사이드로 실행된다. 새로 추가된 LLM 비용 계산기는 언어모델 요청의 예상 비용과 토큰/초 시뮬레이터를 제공한다. 모든 공식은 테스트를 통해 검증되어 신뢰성을 보장한다.

**English Summary**: DevKit is a lightweight one-file calculator library with 69 tools running client-side in the browser. The newest feature is an LLM cost calculator that estimates request costs and shows how generation speed affects timing. All formulas are verified with tests to ensure accuracy.

**핵심 키워드**: DevKit, LLM cost calculator, client-side calculator

### 7. [Next.js로 11개 언어 지원하는 러브 계산기 구현 방법](https://dev.to/lovecalcsapp/making-a-love-calculator-work-in-11-languages-unicode-names-stable-scores-and-locale-routing-in-1304)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: LoveCalcs에서 11개 언어를 지원하는 러브 계산기 개발 시 겪은 기술적 과제들을 소개합니다. 동일한 이름 입력 시 항상 같은 결과를 도출하기 위해 유니코드, 안정적인 스코어링 알고리즘, 로케일 라우팅을 활용했습니다. 문자 빈도, 음운 유사성, 초성 거리, 모음 균형, 수비학 등 5가지 부분 점수를 조합하여 최종 친화도(Affinity Quotient)를 계산합니다.

**English Summary**: This article documents the technical challenges of building a multilingual love calculator supporting 11 languages at LoveCalcs. The developer explains how to ensure deterministic results using an algorithm combining five weighted sub-scores (letter frequency, phonetic matching, first letter proximity, vowel balance, and numerology), and addresses Unicode handling and locale routing in Next.js.

**핵심 키워드**: LoveCalcs, Next.js, Affinity Quotient, Unicode names, locale routing

### 8. [WordPress에서 Astro로 전환: 소규모 비즈니스 사이트 개발 방식의 변화](https://dev.to/lincchad/why-we-stopped-using-wordpress-for-small-business-client-sites-and-moved-to-astro-2cfi)
**출처**: Dev.to WebDev · **중요도**: 보통

**한국어 요약**: 개발사들이 소규모 비즈니스 클라이언트 사이트를 WordPress에서 Astro로 마이그레이션하고 있다. Claude Code와 Cursor 같은 AI 코딩 어시스턴트로 몇 시간 내에 깔끔한 Astro 사이트를 구축할 수 있어 WordPress의 오버헤드가 불필요해졌다. URL 리다이렉트 관리, 간단한 JSON 기반 데이터 관리, 통합 배포 플랫폼 사용 등의 마이그레이션 전략이 제시된다.

**English Summary**: Development agencies are migrating small business client sites from WordPress to Astro, leveraging AI coding assistants like Claude Code and Cursor to build clean sites in hours. The article outlines a practical migration workflow including URL mapping, skipping headless CMS for simple clients, and centralized deployment to reduce overhead and maintenance costs.

**핵심 키워드**: WordPress, Astro, Claude Code, Cursor, Elementor, novence.ai

### 9. [Nginx 리버스 프록시로 Framer 페이지 애널리틱스 추적 문제 해결](https://dev.to/jobkaehenry/same-origin-or-bust-proxying-no-code-pages-through-nginx-so-our-analytics-could-see-them-15kf)
**출처**: Dev.to WebDev · **중요도**: 보통

**한국어 요약**: 디자이너가 Framer로 만든 페이지를 제품에 임베드할 때 Same-Origin 정책으로 인해 행동 애널리틱스 도구(Beusable)가 작동하지 않는 문제가 발생했다. 팀은 Express에서 검증 후 Nginx 리버스 프록시를 도입하여 Framer 호스팅 페이지를 같은 도메인으로 제공함으로써 문제를 해결했다. 이를 통해 클릭, 마우스 움직임, 스크롤 같은 상세한 사용자 행동 데이터를 수집할 수 있게 되었다.

**English Summary**: A development team faced an issue where behavior analytics tools couldn't track user interactions on Framer-embedded pages due to Same-Origin Policy restrictions. They solved this by implementing an Nginx reverse proxy that serves Framer pages under the same domain, enabling precise behavioral data collection from tools like Beusable.

**핵심 키워드**: Nginx, Framer, Beusable, Express, GTM, Hotjar

### 10. [JavaScript 없이 순수 CSS로 차트를 만드는 st-core.fscss 라이브러리](https://dev.to/fscss/st-corefscss-a-library-for-creating-pure-css-charts-without-javascript-compatible-with-any-tech-3cp)
**출처**: Dev.to WebDev · **중요도**: 보통

**한국어 요약**: st-core.fscss는 JavaScript, SVG, Canvas 없이 순수 CSS만으로 통계 대시보드를 구현하는 라이브러리입니다. v2에서는 동적 데이터셋, 레이더 차트, 자동 X축 간격 조정 등이 추가되었으며, CSS 변수를 통해 React, Vue, Svelte 등 모든 프레임워크와 호환됩니다. FSCSS 컴파일 후 CSS 변수로 데이터를 바인딩하기만 하면 됩니다.

**English Summary**: st-core.fscss is a pure-CSS statistical charting library built on FSCSS that eliminates the need for JavaScript, SVG, Canvas, or charting libraries like D3 or Chart.js. Version 2 introduces dynamic datasets, radar charts, automatic X-axis spacing, and dual-pass line strokes, all controlled through CSS custom properties. The library works seamlessly with any JavaScript framework (React, Vue, Svelte) by simply binding data through CSS variables.

**핵심 키워드**: st-core.fscss, FSCSS, CSS custom properties, clip-path: polygon()
