from collections import Counter
from sys import stdin


def is_straight_line(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def straight_line(x1, y1, x2, y2):
    return [
        (x, y)
        for x in range(min(x1, x2), max(x1, x2) + 1)
        for y in range(min(y1, y2), max(y1, y2) + 1)
    ]


def diagonal_line(x1, y1, x2, y2):
    x_sign = 1 if x1 < x2 else -1
    y_sign = 1 if y1 < y2 else -1
    return [
        (x, y)
        for x, y in zip(range(x1, x2 + x_sign, x_sign), range(y1, y2 + y_sign, y_sign))
    ]


lines = [
    (*map(int, pos1.split(",")), *map(int, pos2.split(",")))
    for pos1, pos2 in [
        [pos for pos in line.split(" -> ")] for line in stdin.readlines()
    ]
]

straight_lines = [straight_line(*line) for line in lines if is_straight_line(*line)]
grid1 = Counter(coord for line in straight_lines for coord in line)
print(sum(val >= 2 for val in grid1.values()))

both_lines = [
    straight_line(*line) if is_straight_line(*line) else diagonal_line(*line)
    for line in lines
]
grid2 = Counter(coord for line in both_lines for coord in line)
print(sum(val >= 2 for val in grid2.values()))
