---
name: wiki-to-post
description: AISEC Obsidian LLM-wiki(/mnt/c/z3rotig4r/AISEC)의 마크다운 문서를 Chirpy 블로그 포스트로 변환한다. publish:true 문서만 선별, [[wikilink]]를 /posts/slug 로 매핑, 내부 전용 섹션 제거, Chirpy front matter 주입. "wiki 발행", "AISEC 글 가져와", "wiki to post", "옵시디언 글 블로그로" 등 wiki→블로그 변환 시 반드시 사용.
---

# wiki-to-post — AISEC wiki → Chirpy 변환

AISEC 지식베이스(비공개 원천)의 문서를 블로그 공개용 초안으로 **단방향** 변환한다. read-only로 마운트 경로를 읽고, 산출물은 `_workspace/wiki_converted/`에만 쓴다(AISEC 원본 미수정).

## 핵심 원칙 (왜)
- **단방향:** wiki=source of truth. 블로그→wiki 역수집 없음 → 원천 일관성 유지.
- **명시 발행만:** `publish: true` 없는 문서는 내부 전용. 임의 발행은 비공개 유출 위험 → 절대 금지.
- **죽은 링크 금지:** 아직 발행 안 된 `[[wikilink]]`는 링크 대신 평문 → 404·SEO 손상 방지.
- **AISEC 비공개:** 캐노니컬 백링크는 공개 mkdocs URL이 생기기 전엔 넣지 않음.

## 사용법
```bash
# publish:true 문서 스캔(목록만)
python3 .claude/skills/wiki-to-post/scripts/wiki_to_post.py --scan
# 변환(특정 파일 또는 --all-published)
python3 .claude/skills/wiki_to_post.py <wiki_md_path> --category "AI Red Teaming"
```
경로 미접속(/mnt/c 없음) 시 즉시 에러 종료 — 빈 산출물 생성 안 함.

## 변환 파이프라인
1. **선별:** front matter `publish: true` 또는 인자로 받은 화이트리스트만.
2. **내부 섹션 제거:** `<!-- private -->...<!-- /private -->` 블록, `## 내부메모`/`## TODO`/`## 운영` 류 헤딩 섹션.
3. **wikilink 매핑:** `[[Note Name]]` / `[[Note Name|표시]]` → 발행 매핑표(`_workspace/wiki_publish_log.md`의 slug)가 있으면 `[표시](/posts/{slug}/)`, 없으면 표시 텍스트만.
4. **front matter 주입:** Chirpy 규약(layout/title/date/description(임시)/category/tags/image/toc). 제목은 wiki 제목 또는 H1.
5. **출력:** `_workspace/wiki_converted/{slug}.md` + 로그(원본↔산출, 제거 섹션, 미해결 링크).

## 후처리
변환물은 초안일 뿐 — `seo-optimizer`(description/태그/OG)와 `editor-reviewer`(사실성·빌드)를 거쳐 `_drafts/`→`_posts/`로 발행. 공개 부적합 표현(내부 도구명, 미공개 PoC)은 `post-writer`가 공개용으로 다듬는다.

## 스크립트 한계
스크립트는 결정적 변환(섹션 제거·링크 치환·front matter)만. 공개 적합성 판단·문맥 다듬기는 에이전트 몫.
