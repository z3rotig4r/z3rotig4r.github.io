---
name: og-image
description: 블로그 포스트의 OG 커버 배너를 gpt-image-1(OpenAI)로 생성한다. 텍스트 없는 추상 이미지 + 고정 브랜드 팔레트로 1200x630 커버를 만들고 front matter image를 주입한다. "커버 이미지", "OG 이미지", "배너 생성", "썸네일 만들어", "cover image" 또는 발행 직전 OG가 없을 때 반드시 사용.
---

# og-image — OG 커버 배너 생성 (gpt-image-1)

포스트 1편당 검색 카드용 배너 1장을 생성한다. 이미지 모델은 글자를 못 그리므로 **텍스트 없는 추상 배너**를 만들고, 고정 스타일로 블로그 전체 톤을 통일한다.

## 사용법
```bash
export OPENAI_API_KEY=sk-...            # 로컬 env (필수, Actions 미포함)
# 자동 SUBJECT(title/category에서 구성)
python3 .claude/skills/og-image/scripts/gen_og_image.py _posts/2026-06-09-what-is-ai-red-teaming.md
# 직접 SUBJECT 지정(권장 — 더 정교)
python3 .claude/skills/og-image/scripts/gen_og_image.py <post> --subject "a glowing red neural network probed by adversarial nodes, shield silhouette"
# 프롬프트만 확인(API 호출·과금 없음)
python3 .claude/skills/og-image/scripts/gen_og_image.py <post> --dry-run
```
환경변수: `OPENAI_IMAGE_MODEL`(기본 `gpt-image-1`), `OPENAI_IMAGE_QUALITY`(기본 `medium`).

## 프롬프트 구조 (왜 이렇게)
최종 프롬프트 = `SUBJECT + STYLE_SUFFIX + NEGATIVE`. 이미지 품질의 핵심은 입력 구성이다.
- **SUBJECT**(글마다): 주제의 시각 은유 1~2개. 추상적·은유적. 실제 UI·스크린샷·인물·로고 금지.
- **STYLE_SUFFIX**(전 글 공통, 스크립트에 고정): 다크 배경, 단일 크림슨 액센트, 추상 회로/뉴럴/보안 모티프, 시네마틱 볼류메트릭 라이팅, editorial tech-magazine 표지, 미니멀.
- **NEGATIVE**: text, letters, words, captions, watermark, logo, signature, blurry, distorted — 글자·워터마크 배제가 가장 중요.

> 브랜드 일관성: SUBJECT만 바뀌고 STYLE은 고정 → 모든 커버가 한 시리즈처럼 보인다. STYLE_SUFFIX를 바꾸면 과거 글과 톤이 어긋나니 신중히.

## 동작
1. post front matter에서 `title`/`category`/`description` 읽어 SUBJECT 자동 구성(또는 `--subject` 사용).
2. `images.generate(model, prompt, size="1536x1024", quality, moderation="auto", n=1)` → `b64_json`.
3. Pillow로 **1200×630 크롭/리사이즈**(OG 권장비 1.91:1). Pillow 없으면 원본 저장 + 경고.
4. `assets/img/contents/<slug>/cover.png` 저장.
5. front matter에 `image: {path: /assets/img/contents/<slug>/cover.png, alt: <한글 alt>}` 주입. **빈 image 블록은 절대 만들지 않는다**(홈 프리뷰 깨짐 방지) — 생성 성공 시에만 주입.

## 비용·안전
장당 ~$0.02–0.19(quality 의존). `--dry-run`으로 프롬프트 먼저 확인. `OPENAI_API_KEY` 없으면 에러·미생성(더미 금지). 의존성: `pip install openai pillow`.

## 검증
생성 후 `bundle exec jekyll b` + htmlproofer로 `/{` 깨진 이미지 없음 확인. `seo-lint`의 OG WARN 해소 확인.
