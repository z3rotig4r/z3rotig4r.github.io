---
name: seo-lint
description: Jekyll/Chirpy 포스트의 front matter와 SEO 규약 준수를 검증한다. description 길이/존재, title 키워드, category 택소노미, tags 개수, OG image, slug/permalink 충돌을 점검한다. "SEO 점검", "front matter 검증", "발행 전 체크", "seo lint" 또는 포스트 발행 직전에 반드시 사용.
---

# seo-lint — 포스트 SEO/규약 검증

발행 전 포스트가 SEO·Chirpy 규약을 지키는지 결정적으로 검증한다. 사람의 판단이 필요 없는 기계적 점검은 스크립트로 처리한다.

## 사용법
```bash
python3 .claude/skills/seo-lint/scripts/seo_lint.py <파일 또는 글롭>
# 예: 모든 초안
python3 .claude/skills/seo-lint/scripts/seo_lint.py "_drafts/*.md"
```
종료코드 0 = 전부 PASS, 1 = 하나 이상 실패(CI에서 게이트로 사용 가능).

## 검사 항목 (FAIL = 발행 차단)
- front matter 존재 + 파싱 가능.
- `title` 존재, 비어있지 않음.
- `description` 존재, **길이 ≤ 120자**(한글 기준), 비어있지 않음, 본문 첫 문장과 동일하지 않음.
- `category` 존재 + 승인 택소노미(`AI Red Teaming`, `Agentic AI`, `Security for AI`, `AI for Security`, `News & Trends`, `Research`, `Archive`)에 속함.
- `tags` 3~6개.
- `date` 형식 `YYYY-MM-DD HH:MM +0900`(_posts만; _drafts는 WARN).

## 검사 항목 (WARN = 권장)
- `image.path` 존재(OG 카드). 없으면 경고.
- 본문 H1 중복 없음(title이 H1).
- slug 충돌(`_posts`/`_drafts` 교차) — 충돌 시 FAIL.

## 왜 스크립트인가
규약 점검은 결정적·반복적이라 LLM 추론보다 스크립트가 정확·저렴하다. 에이전트는 결과를 읽고 실패 항목만 고치면 된다.

## 출력 해석
각 파일별 `PASS`/`WARN`/`FAIL` + 항목별 사유. FAIL이 있으면 `seo-optimizer`가 해당 항목만 수정 후 재실행.
