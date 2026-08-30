"""weekly_recap_v1.py — log this week's real work, one flat list."""

WEEK = [
    {"item": "Published \"The Death of the 'Generic' Resume\"", "where": "Substack"},
    {"item": "Learned the Brutalist video workflow (16:9 + 9:16)", "where": "brutalist.art"},
    {"item": "Met with the team: fashion sustainability project", "where": "kickoff"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
