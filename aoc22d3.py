a = "vJrwpWtwJgWrhcsFMMfFFhFp"
b = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
c = "PmmdzqPrVvPwwTWBwg"
d = "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"
e = "ttgJtRGJQctTZtZT"
f = "CrZsJsPPZsGzwwsLwLmpwMDw"


def find_shared_items(rucksack: str) -> str:
    """Split the rucksack's contents into left and right compartments"""
    midpoint = len(rucksack) // 2
    left, right = set(rucksack[:midpoint]), set(rucksack[midpoint:])
    return left.intersection(right).pop()


def priority(item: str) -> int:
    """To help prioritize item rearrangement, every item type can be converted to a priority:
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52."""
    if item.isupper():
        return ord(item.swapcase()) - 70
    else:
        return ord(item.swapcase()) - 64


# print(find_shared_items(a))
# print(find_shared_items(b))
# print(find_shared_items(e))
# print(find_shared_items(d))
# print(find_shared_items(e))
# print(find_shared_items(f))


def solve1(rucksacks: list[str]) -> int:
    total_priority = 0
    for rucksack in rucksacks:
        total_priority += priority(find_shared_items(rucksack))
    return total_priority

def solve2(rucksacks: list[str]) -> int:
    total_priority = 0
    it = iter(rucksacks)
    for x in it:
        ruck1 = set(x)
        ruck2 = set(next(it))
        ruck3 = set(next(it))
        item = ruck1.intersection(ruck2, ruck3).pop()
        total_priority += priority(item)
    return total_priority


def main() -> None:
    with open("input3.txt") as f:
        parsed_input = [x.strip() for x in f.readlines()]

    ans1 = solve1(parsed_input)
    ans2 = solve2(parsed_input)
    print(ans1, ans2)


if __name__ == "__main__":
    main()

