"""Mini-Test: Persistenz (JSON)
Ziel: Nachweis, dass Entity-Daten einfach nach JSON geschrieben und wieder gelesen werden können.
Ausgabe: 'OK: ...'
"""

import json
from pathlib import Path

def main() -> None:
    data_path = Path("module_test.json")

    payload = {
        "code": "DLBDSOOFPP01",
        "name": "Objektorientierte & funktionale Programmierung",
        "cp": 5,
        "status": "IN_BEARBEITUNG",
    }

    data_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    loaded = json.loads(data_path.read_text(encoding="utf-8"))

    assert loaded["code"] == payload["code"]
    assert loaded["cp"] == payload["cp"]
    assert loaded["status"] == payload["status"]

    print("OK: JSON write/read funktioniert ->", data_path.resolve())

if __name__ == "__main__":
    main()
