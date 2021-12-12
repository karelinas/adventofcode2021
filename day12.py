from collections import defaultdict
from sys import stdin


def path_count(exits, current="start", allow_small_double_visit=False, seen=None):
    seen = seen if seen else set()
    if current == "start" and current in seen:
        return 0
    if current == "end":
        return 1
    if current.islower() and current in seen:
        if not allow_small_double_visit:
            return 0
        allow_small_double_visit = False
    return sum(
        path_count(exits, destination, allow_small_double_visit, seen | {current})
        for destination in exits[current]
    )


exits = defaultdict(list)
for s, e in [line.strip().split("-") for line in stdin]:
    exits[s].append(e)
    exits[e].append(s)
print(path_count(exits))
print(path_count(exits, allow_small_double_visit=True))
