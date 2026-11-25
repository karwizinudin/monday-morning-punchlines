"""Monday Morning Punchlines — one joke, judged on laughs.

Scores several original Monday-morning punchlines against the judge's
five criteria (most important first) and writes the winner to
/output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first, with weights.
WEIGHTS = {
    "monday": 5,    # really about Monday mornings
    "laugh": 4,     # a real laugh, punchline lands
    "surprise": 3,  # twist nobody sees coming
    "economy": 2,   # few words, every word doing work
    "fresh": 1,     # not a rerun of tired Monday cliches
}

# Each candidate: (text, scores 0-10 per criterion).
CANDIDATES = [
    (
        "My bed filed for custody of me on Monday morning. "
        "The judge gave it the weekends - I get Mondays, and Mondays get me.",
        {"monday": 9, "laugh": 8, "surprise": 8, "economy": 7, "fresh": 8},
    ),
    (
        "I told my boss I identify as a weekend. HR said my identity "
        "is respected, but Monday still starts at nine.",
        {"monday": 9, "laugh": 9, "surprise": 9, "economy": 9, "fresh": 9},
    ),
    (
        "Monday morning is the only time my coffee files a complaint - "
        "apparently even caffeine needs a pep talk to face me.",
        {"monday": 8, "laugh": 7, "surprise": 6, "economy": 7, "fresh": 7},
    ),
    (
        "I tried to reschedule Monday to next week. It moved itself to "
        "Tuesday, charged a late fee, and cc'd my boss.",
        {"monday": 9, "laugh": 8, "surprise": 7, "economy": 8, "fresh": 8},
    ),
    (
        "My alarm clock quit on Monday. It left a note: 'I ring for a "
        "living, and even I can't face this day twice.'",
        {"monday": 8, "laugh": 7, "surprise": 7, "economy": 7, "fresh": 6},
    ),
    (
        "Monday knocked on my door at 6 a.m. wearing my own face. "
        "I let it in - it had my keys, my calendar, and my will to live.",
        {"monday": 9, "laugh": 8, "surprise": 9, "economy": 6, "fresh": 9},
    ),
]


def score(candidate):
    text, marks = candidate
    total = sum(WEIGHTS[k] * marks[k] for k in WEIGHTS)
    return total


def gate(text):
    """The sealed gate: 1-200 UTF-8 characters, not only whitespace."""
    return 1 <= len(text) <= 200 and text.strip() != ""


def main():
    valid = [c for c in CANDIDATES if gate(c[0])]
    assert valid, "no candidate passes the gate"
    # Highest weighted score wins; ties go to the shorter text.
    ranked = sorted(valid, key=lambda c: (score(c), -len(c[0])), reverse=True)
    winner = ranked[0][0]
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)
    print(f"({len(winner)} characters)")


if __name__ == "__main__":
    main()
