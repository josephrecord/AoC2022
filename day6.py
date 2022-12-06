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




start_of_packet = 4
start_of_message = 14

packet_windows = sliding_window(code, 4)
message_windows = sliding_window(code, 14)

for window in packet_windows:
    if len(set(window)) == 4:  # Four unique characters
        break
    start_of_packet += 1

for window in message_windows:
    if len(set(window)) == 14:  # Four unique characters
        break
    start_of_message += 1


print(start_of_packet)
print(start_of_message)