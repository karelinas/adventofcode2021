import math
from collections import defaultdict
from heapq import heappop, heappush
from itertools import chain
from sys import stdin

from util import is_in_grid, adjacent, transpose


def dijkstra(edges, start, finish):
    queue = []
    distances = {k: math.inf for k in edges.keys()}
    heappush(queue, (0, start))
    distances[start] = 0
    seen = set()

    while queue:
        distance, current = heappop(queue)
        seen.add(current)

        if current == finish:
            return distances[finish]

        for destination, risk in edges[current].items():
            if destination in seen:
                continue
            new_distance = distance + risk
            if new_distance < distances[destination]:
                distances[destination] = new_distance
                heappush(queue, (new_distance, destination))


def make_edges(grid):
    return {
        (x, y): {
            (i, j): grid[j][i] for i, j in adjacent(x, y) if is_in_grid(grid, i, j)
        }
        for y, line in enumerate(grid)
        for x, _ in enumerate(line)
    }


def sideways_expansion(grid):
    return [
        list(
            chain(
                line,
                *[
                    [(line[n] + m - 1) % 9 + 1 for n in range(len(line))]
                    for m in range(1, 5)
                ]
            )
        )
        for line in grid
    ]


def expanded_grid(grid):
    return transpose(sideways_expansion(transpose(sideways_expansion(grid))))


# Part 1
grid_1 = [[int(ch) for ch in line.strip()] for line in stdin]
edges_1 = make_edges(grid_1)
start = (0, 0)
finish_1 = (len(grid_1[-1]) - 1, len(grid_1) - 1)
print(dijkstra(edges_1, start, finish_1))

# Part 2
grid_2 = expanded_grid(grid_1)
edges_2 = make_edges(grid_2)
finish_2 = (len(grid_2[-1]) - 1, len(grid_2) - 1)
print(dijkstra(edges_2, start, finish_2))
