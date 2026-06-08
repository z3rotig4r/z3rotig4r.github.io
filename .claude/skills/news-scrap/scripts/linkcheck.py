#!/usr/bin/env python3
"""linkcheck.py — 마크다운 글의 외부 링크 HTTP 도달성 점검.

뉴스 다이제스트는 외부 출처가 많아 죽은 링크가 SEO·신뢰를 해친다.
editor-reviewer가 발행 전 게이트로 실행한다.
사용: python3 linkcheck.py <file.md> [...]
종료코드 0 = 모든 링크 OK, 1 = 하나 이상 실패.
"""
from __future__ import annotations
import sys, re, glob
import urllib.request
import urllib.error

OK_CODES = {200, 201, 203, 206, 301, 302, 303, 307, 308}
LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)")
BARE_RE = re.compile(r"<(https?://[^>\s]+)>")
TIMEOUT = 20


def extract(text: str):
    urls = set(LINK_RE.findall(text)) | set(BARE_RE.findall(text))
    return sorted(urls)


def check(url: str):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(
                url, method=method,
                headers={"User-Agent": "Mozilla/5.0 (linkcheck; z3rotig4r.github.io)"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.status, ""
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 501):
                continue  # HEAD 거부 → GET 재시도
            return e.code, str(e.reason)
        except Exception as e:  # noqa
            if method == "HEAD":
                continue
            return None, str(e)
    return None, "unreachable"


def main():
    if len(sys.argv) < 2:
        print("usage: linkcheck.py <file.md> [...]"); sys.exit(2)
    files = []
    for arg in sys.argv[1:]:
        files += glob.glob(arg)
    if not files:
        print("대상 파일 없음"); sys.exit(2)
    any_fail = False
    for path in files:
        text = open(path, encoding="utf-8").read()
        urls = extract(text)
        print(f"== {path} ({len(urls)} links) ==")
        for u in urls:
            code, msg = check(u)
            ok = code in OK_CODES
            mark = "OK " if ok else "FAIL"
            print(f"  [{mark}] {code or '-'} {u}" + (f"  ({msg})" if not ok and msg else ""))
            any_fail = any_fail or not ok
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
