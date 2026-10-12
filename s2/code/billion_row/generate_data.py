"""
Generate a measurements file: one "station;temperature" row per line.

    python3 generate_data.py              # 1,000,000 rows (~13 MB)
    python3 generate_data.py 10000000     # 10 million rows (~130 MB)

The real challenge has 1,000,000,000 rows (~13 GB). Scale up gradually.
"""

import random
import sys

from common import DATA_FILE

STATIONS = {
    "Hamburg": 9.7,
    "Oslo": 5.7,
    "Cairo": 21.4,
    "Sofia": 10.6,
    "Lisbon": 17.5,
    "Reykjavik": 4.3,
    "Dubai": 28.0,
    "Bangkok": 28.6,
    "Moscow": 5.8,
    "Sydney": 18.4,
    "Tokyo": 15.4,
    "Nairobi": 17.8,
    "Lima": 19.2,
    "Toronto": 9.4,
    "Mumbai": 27.1,
    "Madrid": 15.0,
    "Berlin": 10.3,
    "Athens": 18.5,
    "Denver": 10.4,
    "Cape Town": 16.2,
}


def main():
    rows = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    random.seed(42)
    names = list(STATIONS)
    means = [STATIONS[n] for n in names]

    with open(DATA_FILE, "w") as f:
        batch = []
        for _ in range(rows):
            i = random.randrange(len(names))
            batch.append(f"{names[i]};{random.gauss(means[i], 5):.1f}\n")
            if len(batch) == 100_000:
                f.writelines(batch)
                batch.clear()
        f.writelines(batch)
    print(f"wrote {rows:,} rows to {DATA_FILE.name}")


if __name__ == "__main__":
    main()
