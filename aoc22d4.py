def subset(a: set, b: set) -> bool:
    if a.issubset(b):
        return True
    elif b.issubset(a):
        return True
    else:
        return False


def solve1(section_assignment_pairs: list[str]) -> int:
    count = 0  # assignment pairs ranges that fully contain the other
    for pair in section_assignment_pairs:
        first, second = pair.split(",")
        first_start, first_end = tuple(int(x) for x in first.split("-"))
        second_start, second_end = tuple(int(x) for x in second.split("-"))
        first_set = set(range(first_start, first_end + 1))
        second_set = set(range(second_start, second_end + 1))
        if subset(first_set, second_set):
            count += 1
    return count


def solve2(section_assignment_pairs: list[str]) -> int:
    disjoint_count = 0
    overlapping_count = 0
    for pair in section_assignment_pairs:
        first, second = pair.split(",")
        first_start, first_end = tuple(int(x) for x in first.split("-"))
        second_start, second_end = tuple(int(x) for x in second.split("-"))
        first_set = set(range(first_start, first_end + 1))
        second_set = set(range(second_start, second_end + 1))
        if first_set.isdisjoint(second_set):
            disjoint_count += 1
        else:
            overlapping_count += 1
    return overlapping_count


def main() -> None:
    with open("input4.txt") as f:
        parsed_input = [x.strip() for x in f.readlines()]

    ans1 = solve1(parsed_input)
    print(ans1)
    ans2 = solve2(parsed_input)
    print(ans2)


if __name__ == "__main__":
    main()
