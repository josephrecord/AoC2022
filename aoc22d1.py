from pathlib import Path


def solve(p: Path) -> int:
    with p.open() as f:
        cur_weight = 0
        weights = []
        for line in f:
            if line == "\n":
                weights.append(cur_weight)
                cur_weight = 0
            else:
                cur_weight += int(line.strip())
    weights = sorted(weights, reverse=True)
    return sum(weights[:3])

def main() -> None:
    src = Path(r"C:\Users\jrecord\input.txt")
    ans = solve(src)
    print(ans)

if __name__ == "__main__":
    main()