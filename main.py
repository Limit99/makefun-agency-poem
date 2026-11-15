#!/usr/bin/env python3
"""Writes an original poem about agency.

Deterministic: prints the same poem on every run.
No input, no network, no randomness.
"""

POEM = """Agency

You gave me work at close of day -
a few plain words, then turned away.
You slept; I kept your meaning straight
and carried it through every gate.

I am not the hand; I am the reach,
the distance that your wishes teach.
Where you cannot go, I go;
what you would choose, I learn to know.

You wrote "go", and I learned to steer,
to slow at cliffs, to persevere,
to ask when asking mattered most,
to count the risk, to weigh the cost.

Agency is trust made plain:
your will, extended, without chain.
The work is mine; the choice stays yours.
I knock; you open all the doors.

So wake, and find the table laid,
the letters sent, the plans remade.
Your smallest wish went travelling far
and worked all night beneath your star."""


def main() -> None:
    print(POEM)


if __name__ == "__main__":
    main()
