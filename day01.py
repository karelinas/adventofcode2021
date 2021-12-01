from sys import stdin

depths = list(map(int, stdin))
increasecount = sum(a < b for a, b in zip(depths, depths[1:]))
windowedcount = sum(a < d for a, d in zip(depths, depths[3:]))

print("Increase count:", increasecount)
print("Windowed count:", windowedcount)
