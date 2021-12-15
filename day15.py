import math
from heapq import heappop, heappush
from sys import stdin

from util import is_in_grid, adjacent, transpose


def dijkstra(edges, start, finish):
    queue = []
    path_risks = {k: math.inf for k in edges.keys()}
    heappush(queue, (0, start))
    path_risks[start] = 0
    seen = set()

    while queue:
        risk_to_current, current = heappop(queue)
        seen.add(current)

        if current == finish:
            return risk_to_current

        for destination, destination_risk in edges[current].items():
            if destination in seen:
                continue
            risk_to_destination = risk_to_current + destination_risk
            if risk_to_destination < path_risks[destination]:
                path_risks[destination] = risk_to_destination
                heappush(queue, (risk_to_destination, destination))


def make_graph(grid):
    return {
        (x, y): {
            (i, j): grid[j][i] for i, j in adjacent(x, y) if is_in_grid(grid, i, j)
        }
        for y, line in enumerate(grid)
        for x, _ in enumerate(line)
    }


def line_continuation(line, times=4):
    return [
        (risk + tile_offset - 1) % 9 + 1
        for tile_offset in range(1, times + 1)
        for risk in line
    ]


def sideways_expansion(grid):
    return [line + line_continuation(line) for line in grid]


def expanded_grid(grid):
    return transpose(sideways_expansion(transpose(sideways_expansion(grid))))


# Part 1
grid_1 = [[int(ch) for ch in line.strip()] for line in stdin]
start = (0, 0)
edges_1 = make_graph(grid_1)
finish_1 = (len(grid_1[-1]) - 1, len(grid_1) - 1)
print(dijkstra(edges_1, start, finish_1))

# Part 2
grid_2 = expanded_grid(grid_1)
edges_2 = make_graph(grid_2)
finish_2 = (len(grid_2[-1]) - 1, len(grid_2) - 1)
print(dijkstra(edges_2, start, finish_2))
