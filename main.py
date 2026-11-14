# agency-poem-01 entry: a program that writes one poem about agency to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader's container).
# Python 3.13, standard library only. Deterministic: the same bytes every run.
import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The Rendang

My grandmother's rendang had no recipe.
A handful of this, chilli until your eyes watered,
coconut milk until the oil split
and the house smelled of smoke and Sunday.

The agent wrote it down.
Two hundred grams of beef, forty of chilli,
three hours and twelve minutes.
It tastes exactly right, every time, the same.

It does not taste like her.
Hers was never the same twice.
Some Sundays it was too hot
and we drank water from the jug
and laughed with our mouths open.

Tonight I cook it the way she did.
I throw the chilli in by the handful.
I forget to set the timer.
The house fills with smoke and Sunday.
I taste it with the wooden spoon.
It is too hot.
And it is hers."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
