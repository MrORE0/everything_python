"""Shared helpers for the billion-row demos."""

import sys
import time
from pathlib import Path

DATA_FILE = Path(__file__).parent / "measurements.txt"


def peak_memory_mb():
    """Peak resident memory of this process, in MB (None on Windows)."""
    try:
        import resource
    except ImportError:  # Windows has no `resource` module
        return None
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes, Linux reports kilobytes
    return peak / (1024 * 1024) if sys.platform == "darwin" else peak / 1024


class Stopwatch:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *exc):
        self.seconds = time.perf_counter() - self.start


def print_results(stats, seconds):
    """stats: {station: (min, mean, max)} -- prints a few rows plus totals."""
    for station in sorted(stats)[:5]:
        lo, mean, hi = stats[station]
        print(f"  {station:<14} min={lo:6.1f}  mean={mean:6.1f}  max={hi:6.1f}")
    print(f"  ... {len(stats)} stations total")
    mem = peak_memory_mb()
    print(f"time: {seconds:.2f}s   peak memory: " + (f"{mem:.0f} MB" if mem else "n/a"))
