from sys import stdin


def windows(lst, n=3):
    while len(lst) >= n:
        yield lst[:n]
        lst = lst[1:]


depths = list(map(int, stdin))
increasecount = sum(a < b for a, b in zip(depths[:-1], depths[1:]))
windowedcount = sum(
    sum(a) < sum(b) for a, b in zip(windows(depths[:-1]), windows(depths[1:]))
)

print("Increase count:", increasecount)
print("Windowed count:", windowedcount)
