from sys import stdin
from math import prod

from util import adjacent, is_in_grid


def is_low_point(grid, x, y):
    return all(
        grid[y][x] < grid[j][i] for i, j in adjacent(x, y) if is_in_grid(grid, i, j)
    )


def basin_size(grid, x, y, visited=None):
    if not visited:
        visited = set()
    if grid[y][x] == 9 or (x, y) in visited:
        return 0
    visited.add((x, y))
    return 1 + sum(
        basin_size(grid, i, j, visited)
        for i, j in adjacent(x, y)
        if is_in_grid(grid, i, j)
    )


grid = [[int(x) for x in row] for row in stdin.read().split()]
low_points = [
    (x, y)
    for y, row in enumerate(grid)
    for x, val in enumerate(row)
    if is_low_point(grid, x, y)
]
print(sum(grid[y][x] + 1 for x, y in low_points))
print(prod(sorted(basin_size(grid, x, y) for x, y in low_points)[-3:]))
