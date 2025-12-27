"""Mini-Test: Aggregation (CSV -> Summen)
Ziel: Nachweis, dass Lernzeit pro Modul aggregiert werden kann.
Eingabe: data_sessions.csv
Ausgabe: Summen je Modul + 'OK: ...'
"""

import csv
from collections import defaultdict
from pathlib import Path

def main() -> None:
    path = Path("data_sessions.csv")
    if not path.exists():
        raise FileNotFoundError("data_sessions.csv nicht gefunden (liegt im gleichen Ordner wie dieses Skript).")

    totals = defaultdict(int)

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totals[row["module_code"]] += int(row["duration_minutes"])

    print("OK: Lernzeit-Summen (Minuten) pro Modul:")
    for code, minutes in sorted(totals.items()):
        print(f"  {code}: {minutes}")

if __name__ == "__main__":
    main()
