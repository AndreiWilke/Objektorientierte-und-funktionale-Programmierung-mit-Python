"""Mini-Test: Timer (Start/Stop)
Ziel: Nachweis, dass eine Lernsession-Dauer gemessen werden kann.
Ausgabe: 'OK: ...'
"""

import time

def main() -> None:
    start = time.perf_counter()
    time.sleep(1.1)  # simuliert Lernzeit
    duration = time.perf_counter() - start

    assert duration > 0.5
    print(f"OK: Gemessene Dauer ~ {duration:.2f}s")

if __name__ == "__main__":
    main()
