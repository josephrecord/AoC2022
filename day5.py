import re

from collections import defaultdict


def move(n: int, from_key: int, to_key: int, d: dict) -> dict:
    for _ in range(n):
        moving_crate = d[from_key].pop()
        d[to_key].append(moving_crate)
    return d



crate_dict = defaultdict(list)

with open("input5.txt") as f:
    for line_no, line in enumerate(f):
        if '[' in line:
            crates = re.finditer(r"(?<=\[)[A-Z](?=\])", line)
            for crate in crates:
                col = crate.start()
                crate_dict[col].append(crate.group(0))


# Re-map dictionary keys to correspond to the correctly numbered stack

# A new empty dictionary to map old_key: new_key
key_map: dict[int, int] = {}
for n, key in enumerate(sorted(crate_dict.keys()), start=1):
    key_map[key] = n
# Do the actual re-mapping and reverse the crate ordering 
remapped_dict = {key_map[key]: list(reversed(value)) for key, value in crate_dict.items()}

# print(remapped_dict)

with open("input5.txt") as f:
    for line in f:
        if 'move' in line:
            n, from_stack, to_stack = tuple(int(x) for x in re.findall(r"\d+", line))
            print(n, from_stack, to_stack)
            remapped_dict = move(n, from_stack, to_stack, remapped_dict)

# print(remapped_dict)

ans = ""
for key, val in sorted(remapped_dict.items()):
    ans += remapped_dict[key][-1]

print(ans)

