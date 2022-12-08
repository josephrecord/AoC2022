from collections import defaultdict

class Tree:
    def __init__(self) -> None:
        self.nodes = None
    
    def prune(self, dir_name: str):
        pass


class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        self.parent = None


cmd_output = []
dirs = defaultdict(list)
direct_size = defaultdict(int)
depths = defaultdict(set)
parents = {}
dirset = set()

with open("input7test.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            # Command
            if cmd_output:
                # print(f"ls: {cmd_output}")
                pass
            cmd_output = [] # New command, clear previous output
            _, cmd, *args = line.split()
            if cmd == "cd":
                arg = args[0]
                # print(f"{cmd} {arg}")
                if arg == "/":
                    dirset.add(arg)
                    stack = ["/"]
                    depth = 0
                    parents[stack[-1]] = None
                elif arg == "..":
                    # move up to parent dir
                    stack.pop()
                    depth -= 1
                else:
                    # move down to child dir
                    dirset.add(arg)
                    parents[arg] = stack[-1] # we learn info on current dir's parent only when we go down a level
                    stack.append(arg)
                    depth += 1
                # print(f"Current dir: {stack[-1]} \t Depth: {depth}")
                depths[depth].add(stack[-1])
            else:
                # Only two commands so will print ls
                # print(cmd)
                pass
        else:
            # Output from a previous command
            cmd_output.append(line.split())
            field1, field2 = line.split()
            if field1 == "dir":
                dirs[stack[-1]].append(field2)
            else:
                direct_size[stack[-1]] += int(field1)


# `direct_size` contains directory names as keys and the sum of the size
# of the files in that immediate directory (but no info about sub-dirs).
# If the immediate file size of the directory is > 100000, we can ignore it.
small_dirs = {key: val for key, val in direct_size.items() if val <= 100000}

ans = 0

sizes = {}

full_depth = len(dirs['/'])

# print(dirset)

# Go to all leaves of tree
# Since leaf has no subdirs, leaf size = direct size
# Now treat leaf as file of parent dir

# print(depths)

# print(depths[full_depth])

for d in dirset:
    print(d)
    while parents[d]:
        d = parents[d]
        print(d)

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