#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


def print_csv(path: Path) -> None:
    print(f"\n== {path} ==")
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    for row in rows[:12]:
        print(", ".join(row))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    targets = [
        root / "data" / "dataset" / "dataset_summary_summary.csv",
        root / "data" / "executability" / "executability_validation_overall.csv",
        root / "data" / "hallucination" / "hallucination_expanded_120_annotated_overall.csv",
        root / "data" / "human_evaluation" / "human_evaluation_summary.csv",
    ]
    for target in targets:
        print_csv(target)


if __name__ == "__main__":
    main()
