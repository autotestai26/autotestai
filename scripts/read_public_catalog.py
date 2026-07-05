#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog = root / "data" / "dataset" / "dataset_catalog_67.csv"
    split_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()

    with catalog.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            split_counts[row["Split"]] += 1
            source_counts[row["Source_Family"]] += 1

    print("Public anonymized catalog summary")
    for split, count in sorted(split_counts.items()):
        print(f"  {split}: {count}")
    print("Source families:")
    for source, count in sorted(source_counts.items()):
        print(f"  {source}: {count}")


if __name__ == "__main__":
    main()
