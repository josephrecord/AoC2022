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


print(find_shared_items(a))
print(find_shared_items(b))
print(find_shared_items(e))
print(find_shared_items(d))
print(find_shared_items(e))
print(find_shared_items(f))

total_priority = 0 

with open("input3.txt") as f:
    for line in f:
        rucksack = line.strip()
        total_priority += priority(find_shared_items(rucksack))

total_priority