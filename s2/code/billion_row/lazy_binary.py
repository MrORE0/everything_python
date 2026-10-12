"""
Billion-row attempt #3 -- a plausible-sounding optimization. Does it help?
Same lazy pipeline, but:
  * read raw bytes (no text decoding)
  * parse the temperature as an integer of tenths (no float())
Sounds faster, right? RUN IT AND MEASURE -- compare with lazy.py, a few runs each.
"""

from common import DATA_FILE, Stopwatch, print_results


def parse_tenths(raw):
    """b'-12.3' -> -123 (temperature in tenths of a degree)."""
    return int(raw.replace(b".", b""))  # "b" makes it a bytes object


def main():
    acc = {}  # station(bytes) -> [min, max, total, count]
    with Stopwatch() as sw:
        with open(DATA_FILE, "rb") as f:
            for line in f:
                station, _, raw = line.partition(b";")
                t = parse_tenths(raw)
                entry = acc.get(station)
                if entry is None:
                    acc[station] = [t, t, t, 1]
                else:
                    if t < entry[0]:
                        entry[0] = t
                    if t > entry[1]:
                        entry[1] = t
                    entry[2] += t
                    entry[3] += 1
        stats = {
            s.decode(): (lo / 10, total / n / 10, hi / 10)
            for s, (lo, hi, total, n) in acc.items()
        }
    print_results(stats, sw.seconds)


if __name__ == "__main__":
    main()

"""
EXPLANATION:
We removed a cheap step (decoding, float) and replaced it
with costlier ones (replace, int, a function call)."""
