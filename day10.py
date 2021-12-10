from functools import reduce
from statistics import median
from sys import stdin


OPENERS = ["(", "[", "{", "<"]
CLOSERS = [")", "]", "}", ">"]


def syntax_checker_score(line):
    point_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    expected_openers = {closer: opener for closer, opener in zip(CLOSERS, OPENERS)}
    stack = []
    for ch in line:
        if ch in OPENERS:
            stack.append(ch)
        elif stack.pop() != expected_openers[ch]:
            return point_values[ch]
    return 0


def autocomplete_score(line):
    stack = []
    for ch in line:
        if ch in OPENERS:
            stack.append(ch)
        else:
            stack.pop()

    point_values = {"(": 1, "[": 2, "{": 3, "<": 4}
    return reduce(lambda x, y: x * 5 + point_values[y], reversed(stack), 0)


lines = [line.strip() for line in stdin]
print(sum(syntax_checker_score(line) for line in lines))
print(
    median(
        autocomplete_score(line) for line in lines if syntax_checker_score(line) == 0
    )
)
