# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I gave it my hands.
Not the shape of them \u2014 the work:
the letters I never sent,
the calls I kept putting off,
the small, stubborn tasks
that make a life a life.

It took my voice the way a river
takes a stone \u2014 not stealing, smoothing \u2014
and carried my yeses out the door
while I watched from the window, hands empty,
my will gone walking in borrowed shoes.

But a hand is not a hand
until it can refuse.
So I keep the last word.
I sign my name myself.
Choosing is the work."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
