# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I hired a driver
for the road I used to walk.
It knows every turn, every shortcut,
the way the light falls at dusk.
It drives so well
I stopped watching the road.

Then one evening I looked up
and didn't know where I was.
The car was warm. The seat was soft.
The driver was kind.
But the destination \u2014
I couldn't remember choosing it.

So I took the wheel.
Not because I drive better.
Because the road is mine to miss."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
