# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The door was never locked.
I only thought it was,
because I kept knocking
and waiting for someone
to say come in.
One day I turned the handle.
It opened.
The room was empty,
and it was mine."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
