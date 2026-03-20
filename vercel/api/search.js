/**
 * Vercel Serverless Function: LLM 기반 테크 뉴스 검색
 * URL: https://your-project.vercel.app/api/search?q=검색어
 *
 * 환경변수 (Vercel 대시보드에서 설정):
 *   - ANTHROPIC_API_KEY: Anthropic API 키
 *   - SITE_URL: GitHub Pages URL (기본값: https://jeonggeunjo.github.io/AI-NEWS)
 */

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export default async function handler(req, res) {
  // CORS preflight
  if (req.method === "OPTIONS") {
    return res.status(200).set(CORS_HEADERS).end();
  }

  // CORS 헤더 적용
  Object.entries(CORS_HEADERS).forEach(([k, v]) => res.setHeader(k, v));

  if (req.method !== "GET") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const query = req.query.q?.trim();

  if (!query) {
    return res.status(400).json({ error: "검색어를 입력해주세요." });
  }

  if (query.length > 200) {
    return res.status(400).json({ error: "검색어가 너무 깁니다." });
  }

  try {
    // GitHub Pages에서 경량 검색 인덱스 fetch
    // llm-search-index.json이 없으면 기존 search.json으로 폴백
    const siteUrl =
      process.env.SITE_URL || "https://jeonggeunjo.github.io/AI-NEWS";

    let indexRes = await fetch(`${siteUrl}/assets/js/data/llm-search-index.json`);
    if (!indexRes.ok) {
      indexRes = await fetch(`${siteUrl}/assets/js/data/search.json`);
    }
    if (!indexRes.ok) {
      throw new Error(`Failed to fetch search index: ${indexRes.status}`);
    }

    const articles = await indexRes.json();

    // 최근 200개만 Claude에 전달 (토큰 절약)
    const recentArticles = articles.slice(0, 200).map((a) => ({
      title: a.title,
      url: a.url,
      date: a.date,
      categories: a.categories,
      snippet: a.snippet,
    }));

    // Claude API 호출
    const claudeRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        model: "claude-haiku-4-5",
        max_tokens: 1200,
        system:
          "You are a tech news search assistant. Find relevant articles from the provided list and explain why they match the query. Always respond with valid JSON only.",
        messages: [
          {
            role: "user",
            content: `사용자 검색 쿼리: "${query}"

다음 기사 목록에서 이 쿼리와 관련된 기사를 최대 5개 선정해줘.
관련성이 없으면 빈 배열을 반환해.

응답 형식 (JSON only):
{
  "results": [
    {
      "url": "기사 URL",
      "title": "기사 제목",
      "date": "날짜",
      "reason": "이 기사가 검색어와 관련된 이유 (한국어 1-2문장)"
    }
  ],
  "summary": "검색 결과 요약 (한국어 1문장, 결과 없으면 '관련 기사를 찾을 수 없습니다.')"
}

기사 목록:
${JSON.stringify(recentArticles)}`,
          },
        ],
      }),
    });

    if (!claudeRes.ok) {
      const err = await claudeRes.text();
      throw new Error(`Claude API error: ${claudeRes.status} ${err}`);
    }

    const claudeData = await claudeRes.json();
    const rawText = claudeData.content?.[0]?.text || "{}";

    // JSON 파싱 (방어적)
    let parsed;
    try {
      parsed = JSON.parse(rawText);
    } catch {
      const match = rawText.match(/\{[\s\S]+\}/);
      parsed = match
        ? JSON.parse(match[0])
        : { results: [], summary: "검색 중 오류가 발생했습니다." };
    }

    return res.status(200).json({
      query,
      results: parsed.results || [],
      summary: parsed.summary || "",
    });
  } catch (err) {
    console.error("Search error:", err);
    return res
      .status(500)
      .json({ error: "검색 중 오류가 발생했습니다.", details: err.message });
  }
}
