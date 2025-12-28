import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def main() -> None:
    totals = defaultdict(int)

    with open("data_sessions.csv", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            totals[row["module_code"]] += int(row["duration_minutes"])

    codes = list(totals.keys())
    minutes = list(totals.values())

    plt.figure()
    plt.bar(codes, minutes)
    plt.title("Lernzeit pro Modul (Minuten)")
    plt.xlabel("Modul")
    plt.ylabel("Minuten")
    plt.tight_layout()
    plt.show()

    print("OK: Plot angezeigt")

if __name__ == "__main__":
    main()
