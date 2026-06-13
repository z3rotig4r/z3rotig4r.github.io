# CLAUDE.md — z3rotig4r.github.io

Jekyll/Chirpy 기반 AI 보안 기술 블로그. 정체성: AI Red Teaming · LLM/Agentic AI 보안 · AI for Security best-practice + 최신 뉴스·연구 스크랩. 한글 우선, 코드·전문용어 영어 병기.

## 핵심 규약
- **permalink 보존:** 포스트 URL은 `/posts/:title/`(slug 기반). 기존 글 slug·파일명 변경 금지(검색 인덱스·외부 링크 보존).
- **발행 흐름:** 초안은 `_drafts/`, 사람 PR 검수 후 `_posts/YYYY-MM-DD-slug.md`로 이동. **LLM 드래프팅을 GitHub Actions에 두지 않는다**(API키 노출 0). Actions는 빌드·검증·하우스키핑 전용.
- **카테고리 택소노미(1뎁스):** `AI Red Teaming` · `Agentic AI` · `Security for AI` · `AI for Security` · `News & Trends` · `Research` · `Archive`(기존 학습/cert 글, 신규엔 미사용).
- **SEO:** 신규 글은 `seo-lint` 통과 필수(description ≤120자·키워드, tags 3~6, OG image).

## 하네스: AI 보안 블로그 포스팅 자동화

**목표:** 신뢰 소스 기반 AI 보안 동향 스크랩 + 지식 정리 + AISEC wiki 발행을 일관된 파이프라인으로 자동 초안화(로컬·사람 검수).

**트리거:** 블로그 콘텐츠 작업("글 써", "포스트 발행", "뉴스 스크랩", "동향 정리", "wiki 발행", "초안 수정/보완/개선") 요청 시 `blog-orchestrator` 스킬을 사용하라. 단순 질문은 직접 응답.

**AISEC 연동:** `/mnt/c/z3rotig4r/AISEC` LLM-wiki는 비공개 원천(source of truth). `publish: true` 문서만 `wiki-to-post`로 단방향 변환. 블로그 repo엔 AISEC 코드 미포함.

**변경 이력:**
| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-06-08 | 초기 구성 (agents 5, skills 5) | 전체 | AI 보안 블로그 포스팅 하네스 신규 구축 |
| 2026-06-09 | image-designer 에이전트 + og-image 스킬 추가 (gpt-image-1 OG 커버) | agents/image-designer, skills/og-image, blog-orchestrator | 신규 글 검색 카드용 OG 배너 자동 생성 (로컬 OPENAI_API_KEY) |
| 2026-06-09 | 뉴스 스크랩 강화 (국내2:해외8, 한글번역, 출처필수, linkcheck) | agents/news-scout, skills/news-scrap | 해외 번역 다이제스트로 접근성·CTR↑, 죽은 링크 게이트 |
| 2026-06-13 | 다이제스트 hada.io 톤 불릿 포맷 | skills/news-scrap | 스캔성·CTR↑ |
| 2026-06-13 | 예약 발행 자동화 (미래날짜 _posts + 매일 cron 리빌드, seo-lint `scheduled:true` 예외) | pages-deploy.yml, skills/seo-lint | 날짜 분산 발행으로 freshness 신호↑, 사람은 PR 1회 검수 후 무방치 자동 게시 (LLM 미사용) |
| 2026-06-13 | post-writer "붕 뜨는 느낌 금지" 규약 (실무 예시·기업 best-practice·무할루시네이션) | agents/post-writer | 개념 글의 적용 감각↑, 사실성 강제 |
| 2026-06-13 | GEO/스키마 도입 (NotFair SEO 방법론 차용) — FAQPage JSON-LD 훅 + GEO 신호 스택 | _includes/metadata-hook.html, agents/seo-optimizer·post-writer | AI 검색(ChatGPT/Perplexity/AI Overview) 인용·리치결과로 CTR↑. NotFair는 SEO 스킬만 로컬 차용(원격 MCP·Ads 미사용) |
