---
layout: post
title: "2026-04-20 프론트엔드 데일리 브리핑"
date: 2026-04-20 00:07:00 +0900
categories: [frontend]
tags:
  - CPU optimization
  - JavaScript
  - architecture comparison
  - browser profiling
  - closures
  - drawing applications
  - falsy values
  - javascript
  - language design
  - lexical-environment
  - null handling
  - programming-concepts
  - scrml
  - web performance
---

> 수집 시각: 2026-04-19 21:53 UTC | 총 3건

## 커뮤니티

### 1. [2년 만에 깨달은 JavaScript 클로저의 진정한 의미](https://dev.to/samareshdas/why-closures-finally-clicked-for-me-after-2-years-3i2g)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: 개발자가 2년간 이해하지 못했던 JavaScript 클로저의 개념을 finally 깨닫게 된 경험담. 클로저는 함수가 자신이 생성된 렉시컬 환경의 변수들을 "기억"하는 현상이며, 카운터 함수 예제를 통해 이를 명확히 설명. 복잡해 보이지만 실제로는 함수가 변수들의 작은 "배낭"을 가지고 다니는 것으로 이해할 수 있음.

**English Summary**: A developer shares their journey to finally understanding JavaScript closures after two years of confusion. The article explains that closures are simply functions that "remember" their lexical environment (the variables and functions available where they were declared) even when executed outside their original scope. A practical counter function example demonstrates how closures work by showing how an inner function retains access to the parent function's variables.

**핵심 키워드**: JavaScript, closures, lexical environment, counter function

### 2. [JavaScript의 null과 falsy: 수십 년의 설계 오류](https://dev.to/bryan_maclee/null-was-a-billion-dollar-mistake-falsy-was-the-second-3o61)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: JavaScript의 null과 undefined가 별개의 값으로 존재하고, 'falsy' 개념이 두 가지 주요 설계 오류라는 주장을 담은 기술 칼럼입니다. 저자는 이러한 문제를 해결하기 위해 scrml이라는 단일 파일 풀스택 반응형 웹 언어를 개발했으며, 1965년 Tony Hoare가 지적한 null 참조 오류의 현대적 사례를 설명합니다.

**English Summary**: The article critiques JavaScript's design choices from the 1990s, specifically having both null and undefined as distinct values and the 'falsy' concept, comparing them to Tony Hoare's famous 'billion-dollar mistake.' The author created scrml, a full-stack reactive web language, partly to address these inherited design flaws in JavaScript.

**핵심 키워드**: Tony Hoare, JavaScript, null, undefined, falsy, scrml

### 3. [드로잉 앱이 유휴 상태에서 2% CPU를 소비하는 이유](https://dev.to/eugenioenko/why-your-drawing-app-uses-2-cpu-when-youre-not-using-it-10e0)
**출처**: Dev.to JavaScript · **중요도**: 보통

**한국어 요약**: Figma, tldraw, Excalidraw, Skedoodle 등 웹 기반 드로잉 앱들의 유휴 상태 CPU 소비를 비교 분석한 연구다. Figma는 3.49%의 CPU를 사용하는 반면 Skedoodle은 측정 오차 수준에 불과했다. 렌더링 아키텍처와 이벤트 루프 구현의 차이가 CPU 소비의 주요 원인으로 드러났다.

**English Summary**: A performance analysis comparing CPU usage of popular web drawing apps (Figma, tldraw, Excalidraw, Skedoodle) on idle blank canvases. Figma consumes 3.49% CPU while Skedoodle uses minimal resources at measurement noise floor. The research reveals that rendering architecture choices and event loop implementations are the key factors determining idle CPU consumption.

**핵심 키워드**: Figma, tldraw, Excalidraw, Skedoodle, Playwright, Chrome DevTools Protocol
