import collections

from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


with open("input6.txt") as f:
    code = f.readline().strip()


windows = sliding_window(code, 4)

i = 4
for window in windows:
    if len(window) == len(set(window)):
        print(i)
        break
    i += 1
