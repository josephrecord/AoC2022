from collections import defaultdict
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True):
class Dir:
    depth: int
    name: str
    parent: Union[None, "Dir"]

root = Dir(0, '/', None)
current_dir = root

size = defaultdict(int)
ls = defaultdict(int)    # num times ls run in dir (to prevent overcounting)
parent = {}

with open("input7.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            # Command
            _, cmd, *args = line.split()
            if cmd == "cd":
                arg = args[0]
                if arg == "/":
                    depth = 0
                    stack = root
                    current_dir = (depth, stack[-1])
                elif arg == "..":
                    depth -= 1
                    stack.pop()
                    current_dir = (depth, stack[-1])
                else:
                    p = current_dir
                    depth += 1
                    stack.append(arg)
                    current_dir = Dir(depth, stack[-1])
                    parent[current_dir] = p
                print(current_dir)
            else:
                ls[current_dir] += 1  # num times ls run in current dir
        else:
            # `line` is output from a previous command
            # print(line)
            field1, field2 = line.split()
            if field1 == "dir":
                # directory
                pass
            else:
                # file
                if ls[current_dir] == 1:
                    size[current_dir] += int(field1)
               

ans = 0
threshold = 100000
# print(size)

for dir in list(sorted(size, reverse=True)):
    if size[dir] > threshold:
        print(f"{dir}:  {size[dir]} > {threshold} --> ignore")
    else:
        print(f"{dir}:  {size[dir]} <= {threshold} --> include")
        print(f"total is {ans} + {size[dir]} = {ans+size[dir]}")
        ans += size[dir]
    try:
        print(f"add to parent {parent[dir]}: {size[parent[dir]]} + {size[dir]} = {size[parent[dir]] + size[dir]}")
        size[parent[dir]] += size[dir]
        # size[dir] = 0
    except KeyError:
        print(f"{dir} has no parent")

print(size)
print(ans)

# last guess: 1057868
# last guess: 987658

# Go to all leaves of tree
# Since leaf has no subdirs, leaf size = direct size
# Now treat leaf as file of parent dir

# print(depths)

# print(depths[full_depth])

# for d in dirset:
#     print(d)
#     while parents[d]:
#         d = parents[d]
#         print(d)

# print(parents)

# for dir, subdirs in dirs.items():
#     for subdir in subdirs:
#         if len(dirs[subdir]) != 0:
#             # subdir has children
#             return get_children(dirs[child])
#         else:
#             # subdir has no children
#             # check next subdir
#             pass

# for dir in direct_size.keys():  # For each dir that we saw...
#     print(dir)
#     if len(dirs[dir]) == 0:  # ... if that dir has no childen...
#         sizes[dir] = direct_size[dir]  # ...its true size is its direct size
#         # That dir can now be treated as a file.
#         # Find the parent of that dir, remove the dir from the list
#         # of children and increase the parent's direct size by 
#         # the direct size of dir
#         parent = parents[dir]
#         print(f"dir: {dir},  parent: {parent}, dirs: {dirs}")
#         direct_size[parent] += direct_size[dir]
#         dirs[parent].remove(dir)
#         # print(dirs)