from pathlib import Path


def main() -> None:
    total = 0
    input = Path("day_1/input.txt").read_text()
    rows = [tuple(map(int, r.split("   "))) for r in input.split("\n")[:-1]]
    left = [r[0] for r in rows]
    left.sort()
    right = [r[1] for r in rows]
    right.sort()

    total = sum(map(lambda r: abs(r[0] - r[1]), zip(left, right)))
    print(total)


if __name__ == "__main__":
    main()
