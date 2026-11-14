# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The Letter

My father wrote his letters by hand.
Slow, in blue ink. He crossed things out
and left the crossings in,
so you could see where he had changed his mind.

Now the agent writes them for him.
It has all his letters, and it writes a new one
in an afternoon, every sentence clean,
no crossings, no second thoughts,
and he signs his name at the bottom
of a letter he did not write.

Tonight I take the blue pen
and write him a letter by hand.
I cross a word out. I leave it there.
I cross another. I leave that too.
The page is a mess of second thoughts —
and every one of them is mine."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
