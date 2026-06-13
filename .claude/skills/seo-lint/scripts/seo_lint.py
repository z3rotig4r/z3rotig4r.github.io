#!/usr/bin/env python3
"""seo_lint.py — Chirpy 포스트 front matter / SEO 규약 검증.

사용: python3 seo_lint.py "<glob 또는 파일>" [...]
종료코드 0 = 모두 통과(FAIL 없음), 1 = FAIL 존재.
"""
from __future__ import annotations
import sys, glob, re, os

APPROVED = {"AI Red Teaming", "Agentic AI", "Security for AI",
            "AI for Security", "News & Trends", "Research", "Archive"}
DESC_MAX = 120
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2} [+-]\d{4}$")


def parse_front_matter(text: str):
    m = re.match(r"^---\n(.*?)\n---(.*)$", text, re.S)
    if not m:
        return None, None
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.split("\n"):
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, body


def first_sentence(body: str) -> str:
    for line in body.split("\n"):
        s = line.strip()
        if s and not s.startswith(("#", "<!--", "```", "-", ">", "|")):
            return s
    return ""


def parse_list(val: str):
    mm = re.match(r"\[(.*)\]", val or "")
    if not mm:
        return None
    return [x.strip().strip('"').strip("'") for x in mm.group(1).split(",") if x.strip()]


def lint(path: str):
    fails, warns = [], []
    text = open(path, encoding="utf-8").read()
    fm, body = parse_front_matter(text)
    if fm is None:
        return ["front matter 없음 또는 파싱 불가"], []
    is_post = os.path.basename(path)[:4].isdigit() and "_posts" in path.replace("\\", "/")

    title = fm.get("title", "").strip().strip('"')
    if not title:
        fails.append("title 없음/빈값")

    # Archive = 격리된 레거시 글(과목정리·cert·후기). 신규 SEO 규약(description/tags/OG)을
    # 소급 적용하지 않는다 — 발행 게이트는 신규 콘텐츠 품질만 보장. title 존재만 확인하고 통과.
    cats_early = parse_list(fm.get("category", ""))
    if cats_early and cats_early[0] == "Archive":
        return fails, ["Archive(레거시) — SEO 규약 검사 면제"]

    # 레거시(리모델 이전) 면제: 신규 SEO 규약은 2026-06-08 하네스 구축 이후 글에만 적용.
    # 그 이전 글(옛 Research·Paper Review 등)을 핀 정리 등으로 건드려도 게이트가 막지 않는다.
    date_early = fm.get("date", "")
    if is_post and DATE_RE.match(date_early):
        try:
            import datetime
            _pub = datetime.datetime.strptime(date_early, "%Y-%m-%d %H:%M %z")
            if _pub < datetime.datetime(2026, 6, 8, tzinfo=_pub.tzinfo):
                return fails, ["레거시(2026-06-08 이전) — SEO 규약 검사 면제"]
        except ValueError:
            pass

    desc = fm.get("description", "").strip().strip('"')
    if not desc:
        fails.append("description 없음/빈값")
    else:
        if len(desc) > DESC_MAX:
            fails.append(f"description 길이 {len(desc)} > {DESC_MAX}")
        if desc and desc == first_sentence(body).strip().strip('"'):
            fails.append("description 이 본문 첫 문장과 동일")

    cats = parse_list(fm.get("category", ""))
    if not cats:
        fails.append("category 없음")
    elif cats[0] not in APPROVED:
        fails.append(f"category 1뎁스 '{cats[0]}' 가 승인 택소노미 아님")

    tags = parse_list(fm.get("tags", ""))
    if tags is None:
        fails.append("tags 없음")
    elif not (3 <= len(tags) <= 6):
        fails.append(f"tags 개수 {len(tags)} (3~6 권장)")

    date = fm.get("date", "")
    if is_post and not DATE_RE.match(date):
        fails.append(f"date 형식 오류: '{date}' (YYYY-MM-DD HH:MM +0900)")
    elif not is_post and not DATE_RE.match(date):
        warns.append("date 미설정 (draft → 발행 시 확정)")
    # 미래 날짜 가드: 프로덕션 빌드는 future:false 라 미래 글을 통째로 제외 → 라이브에서 사라짐.
    # 단 `scheduled: true` 는 의도된 예약 발행(매일 cron 리빌드가 발행일에 자동 게시) → FAIL 대신 WARN.
    scheduled = fm.get("scheduled", "").strip().lower() == "true"
    if is_post and DATE_RE.match(date):
        try:
            import datetime
            pub = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M %z")
            if pub > datetime.datetime.now(pub.tzinfo):
                if scheduled:
                    warns.append(f"예약 발행 — {date} 게시 예정(현재 미래라 빌드 제외, cron이 발행일에 노출)")
                else:
                    fails.append(f"date 가 미래({date}) — 프로덕션 빌드에서 제외되어 라이브에 안 보임"
                                 " (의도된 예약이면 front matter에 scheduled: true)")
        except ValueError:
            pass

    if "image" not in fm and "image:" not in text.split("---")[1]:
        warns.append("OG image.path 없음 (검색 카드 약화)")

    if re.search(r"^# ", body, re.M):
        warns.append("본문에 H1(#) 존재 — title이 H1이므로 H2부터 권장")

    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(path)).rsplit(".", 1)[0]
    for other in glob.glob("_posts/*.md") + glob.glob("_drafts/*.md"):
        if os.path.abspath(other) == os.path.abspath(path):
            continue
        ob = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(other)).rsplit(".", 1)[0]
        if ob == base:
            fails.append(f"slug 충돌: {other}")
            break

    return fails, warns


def main():
    if len(sys.argv) < 2:
        print("usage: seo_lint.py '<glob>' [...]"); sys.exit(2)
    files = []
    for arg in sys.argv[1:]:
        files += glob.glob(arg)
    if not files:
        print("대상 파일 없음"); sys.exit(2)
    any_fail = False
    for path in sorted(set(files)):
        fails, warns = lint(path)
        status = "FAIL" if fails else ("WARN" if warns else "PASS")
        print(f"[{status}] {path}")
        for f in fails:
            print(f"   ✗ {f}")
        for w in warns:
            print(f"   ! {w}")
        any_fail = any_fail or bool(fails)
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
