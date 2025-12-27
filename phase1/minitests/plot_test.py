"""Mini-Test: Plot (Matplotlib)
Ziel: Nachweis, dass Lernzeit-Daten visualisiert werden können.
Ausgabe: Plot-Fenster + 'OK: ...'
"""

import matplotlib.pyplot as plt

def main() -> None:
    totals = {
        "DLBDSOOFPP01": 65,
        "DLBDSCC01": 30,
        "DLBDSAI01": 90,
    }

    codes = list(totals.keys())
    minutes = list(totals.values())

    plt.figure()
    plt.bar(codes, minutes)
    plt.title("Lernzeit pro Modul (Minuten)")
    plt.xlabel("Modul")
    plt.ylabel("Minuten")
    plt.tight_layout()
    plt.show()

    print("OK: Plot wurde angezeigt.")

if __name__ == "__main__":
    main()
