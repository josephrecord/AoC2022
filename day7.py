from collections import defaultdict
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, order=True)
class Dir:
    depth: int
    name: str
    parent: Union[None, "Dir"]


@dataclass(frozen=True, order=True)
class File:
    size: int
    name: str
    directory: Dir

root = Dir(0, '/', None)

size = defaultdict(int)
total_size = {}
files = defaultdict(set)
ls = defaultdict(int)    # num times ls run in dir (to prevent overcounting)
ls2 = defaultdict(int)    # num times ls run in dir (to prevent overcounting)
dirset = set()
fileset = set()

dirset2 = set()


with open("input7.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

for line in lines:
    if line.startswith("$ cd"):
        *_, arg = line.split()
        if arg == "/":
            current_dir = root
        elif arg == "..":
            current_dir = current_dir.parent
        else:
            p = current_dir
            current_dir = Dir(p.depth + 1, arg, p)
        dirset.add(current_dir)
    elif line.startswith("$ ls"):
        ls[current_dir] += 1  # num times ls run in current dir
        ls2[current_dir.name] += 1
    else:
        # `line` is output from a previous command
        field1, field2 = line.split()
        if field1 == "dir":
            subdir = Dir(current_dir.depth + 1, field2, current_dir)
            dirset2.add(subdir)
            pass
        else:
            # file
            file = File(int(field1), field2, current_dir)
            fileset.add(file)
            files[current_dir].add(field2)
            if ls[current_dir] == 1:
                size[current_dir] += int(field1)
            else:
                print(f"ls'ed again: {current_dir}")
               

ans1 = 0
threshold = 100000
total_diskspace = 70000000 # total disk space available to the filesystem
needed_free_space = 30000000

# find a directory you can delete that will free up enough space to run the update

fileless_dirs = 0
for dir in dirset:
    if dir not in size:
        fileless_dirs += 1

assert len(size) + fileless_dirs == len(dirset)


for dir in list(sorted(dirset, reverse=True)):
    cur_size = size[dir]
    total_size[dir] = cur_size
    if cur_size <= threshold:
        ans1 += size[dir]
    if dir is not root:
        size[dir.parent] += size[dir]

print(ans1)

# Get the actual free space
free_space = total_diskspace - size[root]

# Find how much space needs to be freed
to_be_freed = needed_free_space - free_space

dirs_to_del = []
for dir in total_size:
    if total_size[dir] > to_be_freed:
        dirs_to_del.append(total_size[dir])


ans2 = min(dirs_to_del)
print(ans2)


# correct ans: 1325919
# last guess: 1260326
# last guess: 1517771
# last guess: 1057868
# last guess: 987658