---
name: new-post
description: Jekyll/Chirpy AI 보안 블로그의 새 포스트를 스캐폴드한다. 규약 front matter를 갖춘 _drafts/{slug}.md 를 생성한다. "새 글", "포스트 초안", "글 작성 시작", "new post", "draft 만들어" 등 새 포스트 작성을 시작할 때 반드시 사용.
---

# new-post — Chirpy 포스트 스캐폴드

새 포스트의 뼈대(규약 front matter + 섹션 골격)를 `_drafts/`에 만든다. 발행 준비가 되면 `_posts/YYYY-MM-DD-{slug}.md`로 옮긴다(권장: `bundle exec jekyll publish` 또는 수동 이동).

## 왜 _drafts 인가
초안은 `_drafts/`(날짜 없는 파일명)에 두면 로컬 `jekyll s --drafts`로만 보이고 프로덕션 빌드엔 안 나간다. 사람 PR 검수 후 `_posts/`로 옮겨 발행 → API키 노출 0, 품질 통제.

## 절차
1. **slug 결정:** 영문 kebab-case. `Glob _posts/*{slug}* _drafts/*{slug}*`로 중복 확인. 충돌 시 주제어/연도 접미사.
2. **카테고리 선택(새 택소노미만):** `AI Red Teaming` · `Agentic AI` · `Security for AI` · `AI for Security` · `News & Trends` · `Research`. 기존 학습글은 `Archive`(신규엔 쓰지 않음).
3. **템플릿 복사:** `assets/post-template.md`를 `_drafts/{slug}.md`로 쓰고 placeholder 치환.
4. **글 유형 표시:** knowledge(개념·기법) 또는 news(스크랩) — 본문 골격이 다름(템플릿 주석 참고).

## front matter 규약 (필수)
- `title`: 한글, `[카테고리] 제목` 형식. 핵심 키워드 앞쪽.
- `date`: `YYYY-MM-DD HH:MM +0900` (발행 시점에 확정).
- `description`: 120자 내 한글, 키워드 포함(초안 단계 임시 → seo-optimizer가 확정).
- `category`: 1~2뎁스, 위 택소노미. `tags`: 3~6개(한/영 검색어).
- `image: { path, alt }`: OG 카드(없으면 발행 전 채움).
- `pin`(기본 false), `math`/`mermaid`/`toc`(필요 시 true).

## permalink 보존
사이트 permalink는 `/posts/:title/`(=slug 기반). slug은 한 번 정하면 바꾸지 않는다 — 기존 검색 인덱스·외부 링크 보존. 발행 후 slug 변경 금지.

## 출력
`_drafts/{slug}.md` 1개. 이어서 `post-writer`가 내용을 채우거나 사용자가 직접 작성.
