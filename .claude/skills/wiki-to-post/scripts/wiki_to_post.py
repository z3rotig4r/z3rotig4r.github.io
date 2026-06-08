#!/usr/bin/env python3
"""wiki_to_post.py — AISEC Obsidian wiki(md) → Chirpy 포스트 초안 변환.

단방향(wiki→blog), read-only. AISEC 원본 미수정.
사용:
  python3 wiki_to_post.py --scan                # publish:true 문서 목록
  python3 wiki_to_post.py <md_path> --category "AI Red Teaming"
  python3 wiki_to_post.py --all-published --category "AI Red Teaming"
경로 미접속 시 비정상 종료(빈 산출물 금지).
"""
from __future__ import annotations
import sys, os, re, glob, argparse, datetime

AISEC_ROOT = os.environ.get("AISEC_ROOT", "/mnt/c/z3rotig4r/AISEC")
WIKI_GLOB = os.path.join(AISEC_ROOT, "ai-redteam-wiki", "wiki", "**", "*.md")
OUT_DIR = os.path.join("_workspace", "wiki_converted")
LOG = os.path.join("_workspace", "wiki_publish_log.md")

PRIVATE_BLOCK = re.compile(r"<!--\s*private\s*-->.*?<!--\s*/private\s*-->", re.S | re.I)
PRIVATE_HEAD = re.compile(r"^#{1,6}\s*(내부메모|내부\s*노트|운영|TODO|private).*$", re.I)


def require_mount():
    if not os.path.isdir(AISEC_ROOT):
        sys.exit(f"ERROR: AISEC 마운트 미접속: {AISEC_ROOT} (변환 중단)")


def parse_fm(text: str):
    m = re.match(r"^---\n(.*?)\n---(.*)$", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, m.group(2)


def is_published(fm: dict) -> bool:
    return str(fm.get("publish", "")).lower() in ("true", "yes", "1")


def slugify(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


def load_publish_map():
    """_workspace/wiki_publish_log.md 에서 wiki제목→slug 매핑 로드."""
    m = {}
    if os.path.exists(LOG):
        for line in open(LOG, encoding="utf-8"):
            mm = re.match(r"\|\s*(.+?)\s*\|\s*([a-z0-9-]+)\s*\|", line)
            if mm and mm.group(2) != "slug":
                m[mm.group(1).strip()] = mm.group(2).strip()
    return m


def strip_private(body: str) -> tuple[str, list]:
    removed = []
    if PRIVATE_BLOCK.search(body):
        removed.append("private block(<!--private-->)")
        body = PRIVATE_BLOCK.sub("", body)
    out, skip, level = [], False, 0
    for line in body.split("\n"):
        h = re.match(r"^(#{1,6})\s", line)
        if h and skip and len(h.group(1)) <= level:
            skip = False
        if PRIVATE_HEAD.match(line):
            skip = True
            level = len(re.match(r"^(#{1,6})", line).group(1))
            removed.append(line.strip())
            continue
        if not skip:
            out.append(line)
    return "\n".join(out), removed


def map_wikilinks(body: str, pubmap: dict) -> tuple[str, list]:
    unresolved = []

    def repl(m):
        target = m.group(1).strip()
        disp = (m.group(2) or target).strip()
        slug = pubmap.get(target)
        if slug:
            return f"[{disp}](/posts/{slug}/)"
        unresolved.append(target)
        return disp

    body = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", repl, body)
    return body, unresolved


def convert(path: str, category: str, pubmap: dict):
    fm, body = parse_fm(open(path, encoding="utf-8").read())
    title = fm.get("title", "").strip('"') or _h1(body) or os.path.basename(path)[:-3]
    slug = slugify(fm.get("slug", "") or title)
    body, removed = strip_private(body)
    body, unresolved = map_wikilinks(body, pubmap)
    today = datetime.date.today().isoformat()
    fmout = (
        "---\n"
        "layout: post\n"
        f'title: "[{category}] {title}"\n'
        f"date: {today} 09:00 +0900\n"
        f'description: "TODO: seo-optimizer 가 120자 내 한글 요약 작성"\n'
        f"category: [{category}]\n"
        "tags: [ai-security]\n"
        "math: false\nmermaid: true\ntoc: true\n"
        "---\n"
    )
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, slug + ".md")
    open(out_path, "w", encoding="utf-8").write(fmout + body.lstrip("\n"))
    return out_path, slug, title, removed, unresolved


def _h1(body: str):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def append_log(rows: list):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    new = not os.path.exists(LOG)
    with open(LOG, "a", encoding="utf-8") as f:
        if new:
            f.write("# wiki→post 발행 로그\n\n| wiki_title | slug | source | removed | unresolved |\n|---|---|---|---|---|\n")
        for r in rows:
            f.write("| {title} | {slug} | {src} | {rem} | {unres} |\n".format(**r))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--all-published", action="store_true")
    ap.add_argument("--category", default="AI Red Teaming")
    a = ap.parse_args()
    require_mount()

    if a.scan:
        found = []
        for p in glob.glob(WIKI_GLOB, recursive=True):
            fm, _ = parse_fm(open(p, encoding="utf-8").read())
            if is_published(fm):
                found.append(p)
        print(f"publish:true 문서 {len(found)}건:")
        for p in found:
            print("  ", p)
        if not found:
            print("  (없음) — wiki 문서에 'publish: true' front matter 추가 필요")
        return

    targets = []
    if a.all_published:
        for p in glob.glob(WIKI_GLOB, recursive=True):
            fm, _ = parse_fm(open(p, encoding="utf-8").read())
            if is_published(fm):
                targets.append(p)
    elif a.path:
        targets = [a.path]
    else:
        sys.exit("대상 없음: <md_path> 또는 --all-published / --scan")

    pubmap = load_publish_map()
    rows = []
    for p in targets:
        out_path, slug, title, removed, unresolved = convert(p, a.category, pubmap)
        print(f"변환: {p} → {out_path}")
        if removed:
            print("  제거 섹션:", "; ".join(removed))
        if unresolved:
            print("  미해결 wikilink(평문 처리):", ", ".join(sorted(set(unresolved))))
        rows.append(dict(title=title, slug=slug, src=p,
                         rem=("; ".join(removed) or "-"),
                         unres=(", ".join(sorted(set(unresolved))) or "-")))
    append_log(rows)
    print(f"로그: {LOG}")


if __name__ == "__main__":
    main()
