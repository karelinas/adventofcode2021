from functools import reduce as foldl
from math import prod
from sys import stdin


def instruction(s):
    command, arg = s.split()
    return command, int(arg)


instructions = [instruction(s) for s in stdin]

moves = {
    "forward": lambda x, y, arg: (x + arg, y),
    "down": lambda x, y, arg: (x, y + arg),
    "up": lambda x, y, arg: (x, y - arg),
}

print(
    prod(
        foldl(
            lambda pos, instr: moves[instr[0]](*pos, instr[1]),
            instructions,
            (0, 0),
        )
    )
)

moves_v2 = {
    "forward": lambda x, y, aim, arg: (x + arg, y + aim * arg, aim),
    "down": lambda x, y, aim, arg: (x, y, aim + arg),
    "up": lambda x, y, aim, arg: (x, y, aim - arg),
}

print(
    prod(
        foldl(
            lambda pos, instr: moves_v2[instr[0]](*pos, instr[1]),
            instructions,
            (0, 0, 0),
        )[:2]
    )
)
