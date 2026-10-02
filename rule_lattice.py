#!/usr/bin/env python3
"""Render an elementary cellular automaton as a reproducible text pattern."""

import argparse
import random


def next_row(cells, rule, wrap):
    width = len(cells)
    row = []
    for index, cell in enumerate(cells):
        left = cells[index - 1] if index else (cells[-1] if wrap else 0)
        right = cells[index + 1] if index + 1 < width else (cells[0] if wrap else 0)
        neighborhood = (left << 2) | (cell << 1) | right
        row.append((rule >> neighborhood) & 1)
    return row


def main():
    parser = argparse.ArgumentParser(
        description="Draw a one-dimensional cellular automaton using '#' for live cells."
    )
    parser.add_argument("--rule", type=int, default=30, help="Wolfram rule number, 0–255 (default: 30)")
    parser.add_argument("--width", type=int, default=65, help="columns, 1–240 (default: 65)")
    parser.add_argument("--rows", type=int, default=31, help="generations, 1–120 (default: 31)")
    parser.add_argument("--seed", type=int, help="seed a reproducible random first row instead of one center cell")
    parser.add_argument("--wrap", action="store_true", help="join the left and right edges")
    args = parser.parse_args()

    for value, name, low, high in (
        (args.rule, "rule", 0, 255),
        (args.width, "width", 1, 240),
        (args.rows, "rows", 1, 120),
    ):
        if not low <= value <= high:
            parser.error(f"{name} must be between {low} and {high}")

    if args.seed is None:
        cells = [0] * args.width
        cells[args.width // 2] = 1
        seed_label = "center"
    else:
        bits = random.Random(args.seed).getrandbits(args.width)
        cells = [(bits >> index) & 1 for index in range(args.width - 1, -1, -1)]
        if not any(cells):
            cells[args.width // 2] = 1
        seed_label = str(args.seed)

    boundary = "wrap" if args.wrap else "zero"
    print(f"Rule {args.rule} | width {args.width} | rows {args.rows} | seed {seed_label} | boundary {boundary}")
    for _ in range(args.rows):
        print("".join("#" if cell else " " for cell in cells))
        cells = next_row(cells, args.rule, args.wrap)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
