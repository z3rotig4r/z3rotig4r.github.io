---
name: news-scrap
description: AI 보안 최신 뉴스·연구 동향을 신뢰 소스에서 수집·큐레이션하여 블로그 스크랩 초안을 만든다. arXiv/MITRE ATLAS/OWASP/벤더 보안블로그/KISA 등에서 AI Red Teaming·LLM 보안 항목을 모아 _drafts/ 초안 생성. "뉴스 스크랩", "동향 정리", "최신 연구 가져와", "이번 주 AI 보안", "news scrap" 등 동향 수집·정리 요청 시 반드시 사용.
---

# news-scrap — AI 보안 동향 수집·큐레이션

신뢰 소스에서 AI 보안 신규 항목을 모아 선별하고, 선택 항목을 한글 스크랩 초안으로 만든다. 실행은 로컬, 발행은 사람 PR 검수.

## 포맷: 주간 묶음 다이제스트 (GeekNews/hada.io 톤)
- 1회 = **8~10건 묶음 한 글**(개별 단건 아님). 제목 예: `[News & Trends] AI 보안 위클리 (YYYY-MM-DD)`. category `[News & Trends]`.
- **수집 비율 국내 2 : 해외 8** — 해외(영어) 항목은 한글 번역 접근성으로 CTR 우위(국내는 이미 접근성 좋음). 엄격 정수비보다 "해외 우위" 원칙.
- **항목 1개 구조 (hada.io 스캔형 — 문단 금지, 불릿 위주):**
  ```
  ### {짧고 사실적인 헤드라인 — 무엇이 일어났나}
  - {핵심 사실 1 — 짧은 문장/구}
  - {핵심 사실 2 — 수치·버전·CVE 등 구체값}
  - {핵심 사실 3}
  - **왜 중요한가:** {한 줄 임팩트·맥락}
  > 출처: [{기관/제목}]({1차 URL}) — YYYY-MM-DD
  ```
  - 헤드라인은 낚시 금지·사실형(GeekNews 톤): "X가 Y했다", "A 취약점, B로 악용". 해외 항목도 헤드라인·불릿 **한글 번역**, 고유명사·CVE·용어는 영어 병기.
  - 불릿은 2~4개. 원문 직접 인용은 blockquote + 출처. 사실/내 해석 분리(`왜 중요한가`가 해석 슬롯).
- 글 머리에 **한 줄 인트로 + 이번 호 항목 수·국내/해외 비율** 표기(스캔성).
- 글 **하단 `## 참고/출처` 섹션 필수**: 항목별 `[제목](1차 URL) — 기관, YYYY-MM-DD`.

## 워크플로우
1. **수집(news-scout):** 소스에서 후보 수집 → `_workspace/scout_candidates.md`. 국내2:해외8, 신선도 14일, 1차출처 우선.
2. **사용자 선택:** 후보 목록 제시 → 발행할 항목 선택받음(임의 전량 발행 금지).
3. **초안화(post-writer):** 선택 항목을 위 다이제스트 포맷으로 묶어 `_drafts/{slug}.md`. 해외 항목 한글 번역. 하단 출처 섹션.
4. **검증 게이트(editor-reviewer):**
   - (a) 각 항목 1차 출처 존재.
   - (b) **모든 외부 링크 HTTP 200** — `python3 .claude/skills/news-scrap/scripts/linkcheck.py <draft>` 로 확인.
   - (c) 번역이 원문 주장을 왜곡하지 않음(사실 보존).
   - (d) 사실/해석 분리. 미통과 항목은 글에서 제외.
5. **SEO:** `seo-lint` 통과(category `[News & Trends]`, description·tags).

## 신뢰 소스 (news-scout 정의와 동일)
1차: arXiv cs.CR/cs.AI, MITRE ATLAS, OWASP LLM Top10, NIST AI RMF, Anthropic/Google/MS/OpenAI 보안·레드팀 블로그.
2차: Project Zero, GitHub Security Lab, PortSwigger, Simon Willison, Embrace The Red, HiddenLayer.
국내: KISA, KrCERT, NCSC, 보안뉴스(주요), 네이버/카카오 기술블로그.

## 큐레이션 원칙 (왜)
- **1차 출처 우선:** 보도보다 원 논문·공식 advisory를 대표 링크로 → 정확성·신뢰.
- **사실/해석 분리:** 원문 주장과 내 분석을 문단으로 구분 → 신뢰성·표절 방지.
- **출처 필수:** 모든 사실에 링크. 신뢰도 낮은 소스는 교차검증 또는 제외.
- **묶음 vs 단건:** 작은 항목은 "이번 주 AI 보안 동향" 묶음, 큰 사건/논문은 단독 글.

## ingest 재사용 (선택, 로컬)
AISEC `ingest/fetch_arxiv.py`·`fetch_sources.py` 로직을 로컬에서 차용해 수집 자동화 가능(중복 구현 회피). 블로그 repo엔 코드 미포함 — 로컬 실행만.

## 산출물
후보 목록(`_workspace/scout_candidates.md`) + 선택 항목 초안(`_drafts/*.md`). 발행은 PR 머지.
