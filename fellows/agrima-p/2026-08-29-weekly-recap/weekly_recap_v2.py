"""weekly_recap_v2.py — same week, split into DONE vs STARTING NEXT."""

DONE = [
    {"item": "Published \"The Death of the 'Generic' Resume\"", "where": "Substack"},
    {"item": "Learned the Brutalist video workflow (16:9 + 9:16)", "where": "brutalist.art"},
]

NEXT = [
    {"item": "Fashion sustainability: forecasting, sampling, traceability", "where": "kickoff held, work starts next week"},
]


def log():
    print("DONE THIS WEEK")
    for entry in DONE:
        print(f"  - {entry['item']}  ({entry['where']})")
    print("STARTING NEXT WEEK")
    for entry in NEXT:
        print(f"  - {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
