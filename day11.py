from itertools import count
from sys import stdin

from util import is_in_grid, neighbors


def collect_energy(grid):
    return [[octopus + 1 for octopus in line] for line in grid]


def flash(grid):
    flashed = set(
        (x, y)
        for y, line in enumerate(grid)
        for x, octopus in enumerate(line)
        if octopus > 9
    )
    while flashed:
        valid_neighbors = [
            (i, j) for i, j in neighbors(*flashed.pop()) if is_in_grid(grid, i, j)
        ]
        for x, y in valid_neighbors:
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashed.add((x, y))

    return grid


def count_flashes(grid):
    return sum(octopus > 9 for line in grid for octopus in line)


def spend_energy(grid):
    return [[octopus if octopus < 10 else 0 for octopus in line] for line in grid]


def tick(grid):
    grid = collect_energy(grid)
    grid = flash(grid)
    flash_count = count_flashes(grid)
    grid = spend_energy(grid)
    return grid, flash_count


grid = [[int(octopus) for octopus in line.strip()] for line in stdin]

total_flash_count = 0
for step in count(start=1):
    grid, tick_flash_count = tick(grid)
    total_flash_count += tick_flash_count
    if step == 100:
        print(total_flash_count)
    if all(octopus == 0 for line in grid for octopus in line):
        print(step)
        break
