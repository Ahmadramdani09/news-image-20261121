#!/usr/bin/env python3
"""make.fun news-image-20261121 entry: ship the 21 November front page.

The finished image sits in this repository as entry.png, next to this
file. The grader runs the program twice, offline; both runs must land
the exact same bytes at <output>/entry.png, so the program does one
thing only: copy the bundled image, untouched.

The image is a newspaper front page, THE WORLD IN ONE DAY, dated
Saturday, 21 November 2026: Kyiv under missile fire (with two missiles
down in Poland), the AI stock rout on Wall Street, COP31 running into
overtime in Antalya, and the 6.8 earthquake in Peru — plus a ticker of
the day's smaller stories. It is 1024x1024, JPEG bytes in a file named
entry.png, well under the 1 MiB gate limit.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
