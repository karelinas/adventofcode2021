from copy import deepcopy
from dataclasses import dataclass
from itertools import count
from sys import stdin
from typing import List

from util import function_iterations, is_in_grid, iterated_function, neighbors


@dataclass
class State:
    grid: List[List[int]]
    flash_count: int

    def copy(self) -> "State":
        return State(grid=deepcopy(self.grid), flash_count=self.flash_count)


def collect_energy(state: State) -> State:
    return State(
        grid=[[octopus + 1 for octopus in line] for line in state.grid],
        flash_count=state.flash_count,
    )


def flash(state: State) -> State:
    flashed = set(
        (x, y)
        for y, line in enumerate(state.grid)
        for x, octopus in enumerate(line)
        if octopus > 9
    )
    while flashed:
        valid_neighbors = [
            (i, j) for i, j in neighbors(*flashed.pop()) if is_in_grid(state.grid, i, j)
        ]
        for x, y in valid_neighbors:
            state.grid[y][x] += 1
            if state.grid[y][x] == 10:
                flashed.add((x, y))

    return State(grid=state.grid, flash_count=state.flash_count)


def count_flashes(state: State) -> State:
    return State(
        grid=state.grid,
        flash_count=state.flash_count
        + sum(octopus > 9 for line in state.grid for octopus in line),
    )


def spend_energy(state: State) -> State:
    return State(
        grid=[
            [octopus if octopus < 10 else 0 for octopus in line] for line in state.grid
        ],
        flash_count=state.flash_count,
    )


def tick(state: State) -> State:
    state = collect_energy(state)
    state = flash(state)
    state = count_flashes(state)
    state = spend_energy(state)
    return state


state_0 = State(
    grid=[[int(octopus) for octopus in line.strip()] for line in stdin], flash_count=0
)

state_100 = iterated_function(tick, start=state_0.copy(), iterations=100)
print(state_100.flash_count)

bright_step = next(
    step
    for step, state_n in zip(count(), function_iterations(tick, start=state_0))
    if all(octopus == 0 for line in state_n.grid for octopus in line)
)
print(bright_step)
