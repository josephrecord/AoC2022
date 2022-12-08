from collections import defaultdict


def get_all_subdirs(dir, tree):
    subdirs = tree[dir]
    if not subdirs:
        return None
    else:
        return get_all_subdirs(tree[dir])


cmd_output = []
dirs = defaultdict(list)
direct_size = defaultdict(int)
depths = defaultdict(set)
parents = {}

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
                    stack = ["/"]
                    depth = 0
                    parents[stack[-1]] = None
                elif arg == "..":
                    # move up to parent dir
                    stack.pop()
                    depth -= 1
                else:
                    # move down to child dir
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


# Go to all leaves of tree
# Since leaf has no subdirs, leaf size = direct size
# Now treat leaf as file of parent dir

for dir in direct_size.keys():  # For each dir that we saw...
    if dir not in dirs.keys():  # ... if that dir has no childen...
        sizes[dir] = direct_size[dir]  # ...its true size is its direct size
        # That dir can now be treated as a file.
        # Find the parent of that dir, remove the dir from the list
        # of children and increase the parent's direct size by 
        # the direct size of dir
        parent = parents[dir]
        print(f"dir: {dir},    parent: {parent}")
        # print(dirs)
        # print(dirs[parent])
        direct_size[parent] += direct_size[dir]
        dirs[parent].remove(dir)