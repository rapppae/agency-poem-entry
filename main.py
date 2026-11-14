# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """For years I followed the voice.
Turn left. Turn right. Go straight.
It knew every shortcut,
every faster way
to places I never asked to go.
One day I missed a turn
on purpose.
"Recalculating," it said,
patient as ever.
I smiled.
For the first time,
I was doing the calculating."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
