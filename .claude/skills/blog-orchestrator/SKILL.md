---
name: blog-orchestrator
description: z3rotig4r AI 보안 블로그의 포스팅 파이프라인을 조율한다. 뉴스 스크랩·지식 정리·AISEC wiki 발행 요청을 받아 news-scout/post-writer/seo-optimizer/editor-reviewer/wiki-publisher 팀을 구성·실행한다. "블로그 글 써", "포스트 발행", "뉴스 스크랩", "wiki 발행", "글 업데이트/재작성/보완", "이전 초안 개선", "AI 보안 글" 등 블로그 콘텐츠 작업 시 반드시 사용. 단순 질문은 직접 응답.
---

# blog-orchestrator — 블로그 포스팅 조율

AI 보안 블로그 콘텐츠 작업을 에이전트 팀으로 조율한다. **실행 모드: 에이전트 팀**(파이프라인). 발행은 항상 사람 PR 검수 — 자동 머지 없음.

## Phase 0: 컨텍스트 확인
- `_workspace/` 존재 + 부분 수정 요청 → **부분 재실행**(해당 에이전트만).
- `_workspace/` 존재 + 새 입력 → **새 실행**(기존을 `_workspace_prev/`로 이동).
- 미존재 → **초기 실행**.
- 기존 `_drafts/{slug}.md`가 있으면 덮어쓰지 않고 개선.

## Phase 1: 요청 분류 (라우팅)
| 요청 | 진입점 | 파이프라인 |
|------|--------|-----------|
| "뉴스 스크랩"/"동향 정리" | `news-scout` | scout → (사용자 선택) → writer → seo → review |
| "개념/기법 정리"/"지식 글" | `post-writer` | writer → seo → review (필요 시 scout가 출처 보강) |
| "wiki 발행"/"AISEC 글" | `wiki-publisher` | publisher → writer(공개용 다듬기) → seo → review |
| "초안 개선"/"수정"/"보완" | 해당 단계 | 지적된 에이전트만 재호출 |

## Phase 2: 팀 구성·실행
- `TeamCreate`로 필요한 멤버만 구성(팀 크기 2~4). `TaskCreate`로 작업·의존성 등록.
- 모든 Agent 호출 `model: "opus"`.
- **데이터 전달:** 파일 기반(`_workspace/`) + 태스크 기반(조율) + 메시지(실시간). 중간 산출물은 `_workspace/{phase}_{agent}_{artifact}.md` 보존.
- 파이프라인 순서: 수집/변환 → 초안 → SEO → 검수. 각 단계 산출물이 다음 입력.

## Phase 3: 게이트 (발행 차단 조건)
- `seo-lint` FAIL → seo-optimizer로 반려.
- `editor-reviewer` 판정 `BLOCK`/`CHANGES_REQUESTED` → 해당 에이전트 반려.
- `bundle exec jekyll b` 실패 → 빌드 통과까지 차단.
- **APPROVE**여도 자동 발행 안 함 — 사람이 `_drafts/`→`_posts/` 이동 + PR 머지.

## 에러 핸들링
- 에이전트 1회 재시도, 재실패 시 누락 명시하고 진행(리포트에 기록).
- 상충 사실은 삭제 말고 출처 병기 → editor-reviewer가 판정.
- AISEC 마운트 미접속: wiki 경로는 건너뛰고 사용자에 보고.

## 데이터 흐름
```
news-scout ─┐
            ├─→ post-writer ─→ seo-optimizer ─→ editor-reviewer ─→ (APPROVE) ─→ 사람 PR 머지
wiki-publisher ┘                                     │
                                          (CHANGES) ─┘ 반려→해당 에이전트
```

## 테스트 시나리오
- **정상:** "이번 주 LLM 보안 뉴스 스크랩해줘" → scout 후보 8건 → 사용자 3건 선택 → writer 묶음 초안 → seo-lint PASS → review APPROVE → `_drafts/` 결과 보고.
- **에러:** "AISEC 레드팀 글 발행" + 마운트 미접속 → wiki-publisher 즉시 보고, 빈 초안 생성 안 함, 대안(로컬 작성) 제시.

## 후속 작업
description의 "수정/보완/개선/재작성/이전 초안" 키워드로 트리거. Phase 0에서 기존 산출물 판별 → 해당 단계만 재실행.
