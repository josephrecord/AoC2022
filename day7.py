from collections import defaultdict


cmd_output = []
dirs = defaultdict(list)
size = defaultdict(int)
depths = defaultdict(set)
parent = {} # key's parent is value
dirset = set()
filesize = 0

with open("input7.txt") as f:
    for line in f:
        line = line.strip()
        # print(f"raw: {line}")
        if line.startswith("$"):
            if cmd_output:
                # print(f"ls: {cmd_output}")
                pass
            cmd_output = [] # New command, clear previous output
            # Command
            _, cmd, *args = line.split()
            if cmd == "cd":
                arg = args[0]
                # print(f"{cmd} {arg}")
                if arg == "/":
                    depth = 0
                    # print("cd /")
                    dir = (0, '/')
                    stack = [dir]
                    dirset.add(dir)
                    parent[dir] = None
                elif arg == "..":
                    depth -= 1
                    # print("cd ..")
                    # move up to parent dir
                    stack.pop()
                else:
                    # move down to child dir
                    depth += 1
                    # print(f"cd {arg}")
                    dir = (depth, arg)
                    parent[dir] = stack[-1] # we learn info on current dir's parent only when we go down a level
                    stack.append(dir)
                    dirset.add(dir)
                # print(f"Current dir: {stack[-1]}")
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
                dirs[stack[-1]].append((depth + 1, field2))
            else:
                filesize += int(field1)
                size[stack[-1]] += int(field1)


# `direct_size` contains directory names as keys and the sum of the size
# of the files in that immediate directory (but no info about sub-dirs).
# If the immediate file size of the directory is > 100000, we can ignore it.
# small_dirs = {key: val for key, val in direct_size.items() if val <= 100000}

ans = 0
threshold = 100000

# for depth in reversed(depths.keys()):
#     print(f"depth: {depth}")
#     for dir in depths[depth]:
#         dirsize = size[dir]
#         parent = parents[dir]
#         parent_size = size[parent]
#         print(f"folder {dir} size: {dirsize}   parent {parent} size: {parent_size}")
#         if dirsize > threshold:
#             # any parent dir that contains `folder` can be ignored
#             print(f"ignore {dir}")
#         else:
#             print(f"include {dir}")
#             print(f"total is {ans} + {dirsize} = {ans+dirsize}")
#             ans += dirsize
#         # treat the folder as a file and add it to its parents' direct size
#         size[parent] += dirsize 
#         print(f"parent {parent} new size: {size[parent]}")

s1 = size

for dir in list(sorted(dirset, reverse=True)):
    if size[dir] > threshold:
        print(f"{dir}:  {size[dir]} > {threshold} --> ignore")
    else:
        print(f"{dir}:  {size[dir]} <= {threshold} --> include")
        print(f"total is {ans} + {size[dir]} = {ans+size[dir]}")
        ans += size[dir]
    print(f"add to parent {parent[dir]}: {size[parent[dir]]} + {size[dir]} = {size[parent[dir]] + size[dir]}")
    size[parent[dir]] += size[dir]

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