from collections import defaultdict
from sys import stdin


def draw_line(grid, x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        return
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[x, y] += 1

def draw_line2(grid, x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        x_start, x_end = min(x1, x2), max(x1, x2)
        y_start, y_end = min(y1, y2), max(y1, y2)
        for x in range(x_start, x_end+1):
            for y in range(y_start, y_end+1):
                grid[x, y] += 1
    else:
        x_sign = 1 if x1 < x2 else -1
        y_sign = 1 if y1 < y2 else -1
        for x, y in zip(range(x1, x2+x_sign, x_sign), range(y1, y2+y_sign, y_sign)):
            grid[x, y] += 1

lines = [(*map(int, pos1.split(',')), *map(int, pos2.split(','))) for pos1, pos2 in
         [[pos for pos in line.split(' -> ')] for line in stdin.readlines()]]

grid = defaultdict(int)
for line in lines:
    draw_line(grid, *line)
print(sum(val >= 2 for val in grid.values()))

grid = defaultdict(int)
for line in lines:
    draw_line2(grid, *line)
print(sum(val >= 2 for val in grid.values()))
