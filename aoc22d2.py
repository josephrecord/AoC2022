from pathlib import Path
from typing import Tuple



def score1(them, you) -> int:
    them = ord(them) - 64
    you = ord(you) - 23 - 64
    if them == you:
        return you + 3
    diff = them - you
    if diff == -1:
        return you + 6
    elif diff == 2:
        return you + 6
    elif diff == 1:
        return you
    elif diff == -2:
        return you
    else:
        raise ValueError


def win_against(rps: int) -> int:
    if rps == 1:  # If they have r
        return 2
    elif rps == 2:
        return 3
    elif rps == 3:
        return 1
    else:
        raise ValueError("Unexpected input")

    
def lose_against(rps: int) -> int:
    if rps == 1:
        return 3
    elif rps == 2:
        return 1
    elif rps == 3:
        return 2
    else:
        raise ValueError("Unexpected input")


def score2(them, outcome) -> int:
    them = ord(them) - 64
    if outcome == 'Y':     # draw
        return them + 3
    elif outcome == 'X':   # loss
        return lose_against(them)
    elif outcome == 'Z':   # win
        return 6 + win_against(them)
    else:
        raise ValueError("Outcome incorrectly formatted")


def solve(p: Path) -> Tuple[int, int]:
    scores = []
    scores2 = []
    with p.open() as f:
        for line in f:
            them, you =  line.strip().split()
            scores.append(score1(them, you))
            scores2.append(score2(them, you))
    return sum(scores), sum(scores2)


def main() -> None:
    src = Path(r"C:\Users\jrecord\2022day2input.txt")
    # src = Path(r"C:\Users\jrecord\d2test.txt")
    ans = solve(src)
    print(ans)

if __name__ == "__main__":
    main()