/**
 * LLM 기반 자연어 검색 — Cloudflare Worker 연동
 * _includes/search-loader.html에서 LLM_SEARCH_WORKER_URL이 설정된 경우 로드됨
 */

(function () {
  "use strict";

  const searchInput = document.getElementById("search-input");
  const resultsContainer = document.getElementById("search-results");

  if (!searchInput || !resultsContainer || typeof LLM_SEARCH_WORKER_URL === "undefined") {
    return;
  }

  const workerUrl = LLM_SEARCH_WORKER_URL;
  let debounceTimer = null;
  let currentRequest = null;

  function showLoading() {
    resultsContainer.innerHTML =
      '<p class="search-loading" style="padding:1rem;color:#666;">🔍 AI가 검색 중입니다...</p>';
    resultsContainer.style.display = "block";
  }

  function showError(msg) {
    resultsContainer.innerHTML = `<p class="search-error" style="padding:1rem;color:#c00;">${msg}</p>`;
    resultsContainer.style.display = "block";
  }

  function showResults(data) {
    const { results, summary } = data;

    if (!results || results.length === 0) {
      resultsContainer.innerHTML =
        '<p class="no-results" style="padding:1rem;color:#666;">관련 기사를 찾을 수 없습니다.</p>';
      resultsContainer.style.display = "block";
      return;
    }

    let html = "";
    if (summary) {
      html += `<p class="search-summary" style="padding:0.5rem 1rem;font-size:0.85rem;color:#555;border-bottom:1px solid #eee;">${summary}</p>`;
    }

    results.forEach((item) => {
      html += `
        <div class="search-result-item" style="padding:0.75rem 1rem;border-bottom:1px solid #f0f0f0;">
          <a href="${item.url}" class="search-result-title" style="font-weight:600;display:block;margin-bottom:0.25rem;">${item.title}</a>
          ${item.date ? `<span class="search-result-date" style="font-size:0.75rem;color:#999;">${item.date}</span>` : ""}
          ${item.reason ? `<p class="search-result-reason" style="font-size:0.8rem;color:#666;margin:0.25rem 0 0;">${item.reason}</p>` : ""}
        </div>`;
    });

    resultsContainer.innerHTML = html;
    resultsContainer.style.display = "block";
  }

  function hideResults() {
    resultsContainer.innerHTML = "";
    resultsContainer.style.display = "none";
  }

  async function doSearch(query) {
    if (!query || query.trim().length < 2) {
      hideResults();
      return;
    }

    // 이전 요청 취소
    if (currentRequest) {
      currentRequest.abort();
    }

    showLoading();

    const controller = new AbortController();
    currentRequest = controller;

    try {
      const url = `${workerUrl}?q=${encodeURIComponent(query.trim())}`;
      const res = await fetch(url, { signal: controller.signal });
      const data = await res.json();

      if (currentRequest !== controller) return; // 구버전 응답 무시

      if (data.error) {
        showError(data.error);
      } else {
        showResults(data);
      }
    } catch (err) {
      if (err.name === "AbortError") return;
      showError("검색 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.");
    } finally {
      if (currentRequest === controller) {
        currentRequest = null;
      }
    }
  }

  // 입력 이벤트 — 800ms 디바운스
  searchInput.addEventListener("input", function () {
    clearTimeout(debounceTimer);
    const query = this.value.trim();
    if (!query) {
      hideResults();
      return;
    }
    debounceTimer = setTimeout(() => doSearch(query), 800);
  });

  // 검색창 외부 클릭 시 결과 숨김
  document.addEventListener("click", function (e) {
    if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
      hideResults();
    }
  });

  // Enter 키 즉시 검색
  searchInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      clearTimeout(debounceTimer);
      doSearch(this.value.trim());
    }
    if (e.key === "Escape") {
      hideResults();
    }
  });
})();
