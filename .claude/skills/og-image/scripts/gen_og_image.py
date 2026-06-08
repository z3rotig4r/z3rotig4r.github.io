#!/usr/bin/env python3
"""gen_og_image.py — gpt-image-1 로 포스트 OG 커버 배너 생성.

텍스트 없는 추상 배너 + 고정 브랜드 스타일 → 1200x630 → front matter image 주입.
사용:
  python3 gen_og_image.py <post.md> [--subject "english visual desc"] [--dry-run]
env: OPENAI_API_KEY(필수), OPENAI_IMAGE_MODEL(기본 gpt-image-1), OPENAI_IMAGE_QUALITY(기본 medium)
"""
from __future__ import annotations
import sys, os, re, base64, argparse

# 전 글 공통 — 브랜드 일관성. 바꾸면 과거 커버와 톤 어긋남.
STYLE_SUFFIX = (
    "dark near-black background, single crimson red accent color, "
    "abstract circuit and neural network and cybersecurity motif, "
    "geometric, cinematic volumetric lighting, depth of field, high detail, "
    "editorial tech magazine cover art, minimal, sophisticated, no people"
)
NEGATIVE = ("text, letters, words, captions, numbers, watermark, logo, "
            "signature, ui screenshot, blurry, distorted, low quality")
OG_W, OG_H = 1200, 630
ASSET_BASE = "assets/img/contents"


def parse_fm(text: str):
    m = re.match(r"^---\n(.*?)\n---(.*)$", text, re.S)
    if not m:
        return None, None, None
    return m.group(1), m.group(2), m  # fm_raw, body, match


def fm_get(fm_raw: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.*)$", fm_raw, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def slug_of(path: str) -> str:
    base = os.path.basename(path).rsplit(".", 1)[0]
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)


def clean_title(title: str) -> str:
    return re.sub(r"^\[[^\]]*\]\s*", "", title).strip()


def build_subject(title: str, category: str) -> str:
    """--subject 미지정 시 title/category로 기본 SUBJECT 구성(영문)."""
    t = clean_title(title)
    return (f"an abstract conceptual illustration representing '{t}' "
            f"in the context of {category or 'AI security'}, "
            f"metaphorical, no literal screenshots")


def build_prompt(subject: str) -> str:
    return f"{subject}. Style: {STYLE_SUFFIX}. Avoid: {NEGATIVE}."


def inject_image(text: str, slug: str, alt: str) -> str:
    """기존 image 블록 제거 후 새 블록 주입. 빈 블록 절대 생성 안 함."""
    fm_raw, body, m = parse_fm(text)
    if fm_raw is None:
        raise SystemExit("front matter 없음")
    lines = fm_raw.split("\n")
    out, i = [], 0
    while i < len(lines):
        if re.match(r"^image:\s*$", lines[i]):
            i += 1
            while i < len(lines) and re.match(r"^\s+\S", lines[i]):
                i += 1
            continue
        if re.match(r"^image:\s*\{", lines[i]):
            i += 1
            continue
        out.append(lines[i]); i += 1
    path = f"/{ASSET_BASE}/{slug}/cover.png"
    out += ["image:", f"  path: {path}", f'  alt: "{alt}"']
    return "---\n" + "\n".join(out) + "\n---" + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post")
    ap.add_argument("--subject", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if not os.path.exists(a.post):
        raise SystemExit(f"파일 없음: {a.post}")
    text = open(a.post, encoding="utf-8").read()
    fm_raw, _, _ = parse_fm(text)
    if fm_raw is None:
        raise SystemExit("front matter 파싱 불가")
    title = fm_get(fm_raw, "title")
    category = re.sub(r"[\[\]]", "", fm_get(fm_raw, "category")).split(",")[0].strip()
    slug = slug_of(a.post)
    subject = a.subject or build_subject(title, category)
    prompt = build_prompt(subject)

    print(f"slug    : {slug}")
    print(f"subject : {subject}")
    print(f"prompt  : {prompt}\n")
    if a.dry_run:
        print("[dry-run] API 호출 안 함."); return

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("ERROR: OPENAI_API_KEY 미설정 (로컬 env 필요). 이미지 미생성.")

    try:
        from openai import OpenAI
    except ImportError:
        raise SystemExit("ERROR: openai 미설치 — pip install openai")

    model = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
    quality = os.environ.get("OPENAI_IMAGE_QUALITY", "medium")
    client = OpenAI()
    print(f"생성 중... (model={model}, quality={quality}, size=1536x1024)")
    resp = client.images.generate(model=model, prompt=prompt,
                                  size="1536x1024", quality=quality,
                                  moderation="auto", n=1)
    raw = base64.b64decode(resp.data[0].b64_json)

    out_dir = os.path.join(ASSET_BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cover.png")
    try:
        from PIL import Image, ImageOps
        import io
        img = Image.open(io.BytesIO(raw)).convert("RGB")
        img = ImageOps.fit(img, (OG_W, OG_H), Image.LANCZOS)  # cover-crop 중앙
        img.save(out_path, "PNG", optimize=True)
        print(f"저장: {out_path} ({OG_W}x{OG_H})")
    except ImportError:
        open(out_path, "wb").write(raw)
        print(f"저장: {out_path} (원본 1536x1024 — Pillow 없어 크롭 생략. pip install pillow 권장)")

    alt = clean_title(title) or slug
    new_text = inject_image(text, slug, alt)
    open(a.post, "w", encoding="utf-8").write(new_text)
    print(f"front matter image 주입 완료: {a.post}")


if __name__ == "__main__":
    main()
