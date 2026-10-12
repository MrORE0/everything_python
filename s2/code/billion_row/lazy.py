"""
Billion-row attempt #2 -- a lazy generator pipeline.
"""

from common import DATA_FILE, Stopwatch, print_results


def read_lines(path):
    with open(path) as f:
        for line in f:  # the file object is itself a lazy iterator (slide 3)
            yield line


def parse(lines):
    for line in lines:
        station, _, temp = line.partition(";")
        yield station, float(temp)


def aggregate(rows):
    # we go through as many stations are in the buffer (lines)
    acc = {}  # station -> [min, max, total, count]
    for station, temp in rows:  # each iteration asks for the next to be yielded
        entry = acc.get(station)
        if entry is None:
            acc[station] = [temp, temp, temp, 1]
        else:
            if temp < entry[0]:
                entry[0] = temp
            if temp > entry[1]:
                entry[1] = temp
            entry[2] += temp
            entry[3] += 1
    return {s: (lo, total / n, hi) for s, (lo, hi, total, n) in acc.items()}


def main():
    with Stopwatch() as sw:
        stats = aggregate(parse(read_lines(DATA_FILE)))
    print_results(stats, sw.seconds)


if __name__ == "__main__":
    main()
