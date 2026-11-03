"""Track ticket reopen rates per category from a ticket CSV.

Usage: python3 main.py tickets.csv
CSV columns: ticket,category,status (open/closed/reopened).
Reopen rate = reopened / total per category, highest rate first.
Categories with fewer than 5 tickets are flagged as small samples.
"""
import argparse, csv, sys
from collections import Counter


def rates(rows):
    totals, reopened = Counter(), Counter()
    for row in rows:
        category = row["category"].strip()
        totals[category] += 1
        if row["status"].strip().lower() == "reopened":
            reopened[category] += 1
    out = []
    for category, total in totals.items():
        rate = reopened[category] / total
        note = " (small sample)" if total < 5 else ""
        out.append((category, rate, total, note))
    return sorted(out, key=lambda r: -r[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for category, rate, total, note in rates(list(csv.DictReader(f))):
            print(f"{category}: {rate:.0%} reopened ({total} tickets){note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
