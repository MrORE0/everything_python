"""
Billion-row attempt #1 -- the naive way.
"""

from common import DATA_FILE, Stopwatch, print_results


def main():
    with Stopwatch() as sw:
        # whole file as one string, then a list of strings
        lines = DATA_FILE.read_text().splitlines()
        # ANOTHER full copy, as lists of strings
        rows = [line.split(";") for line in lines]
        readings = [(s, float(t)) for s, t in rows]  # and a THIRD copy

        per_station = {}
        for station, temp in readings:
            per_station.setdefault(station, []).append(temp)  # every value kept

        stats = {s: (min(v), sum(v) / len(v), max(v)) for s, v in per_station.items()}
    print_results(stats, sw.seconds)


if __name__ == "__main__":
    main()
