from functools import reduce
from statistics import median
from sys import stdin


def parse(line):
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    expected_openers = {closer: opener for closer, opener in zip(closers, openers)}
    stack = []
    for ch in line:
        if ch in openers:
            stack.append(ch)
        elif stack.pop() != expected_openers[ch]:
            return stack, ch
    return stack, None


def syntax_checker_score(line):
    point_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    _, unexpected = parse(line)
    return point_values[unexpected] if unexpected else 0


def autocomplete_score(line):
    point_values = {"(": 1, "[": 2, "{": 3, "<": 4}
    leftovers, _ = parse(line)
    return reduce(lambda x, y: x * 5 + point_values[y], reversed(leftovers), 0)


lines = [line.strip() for line in stdin]
print(sum(syntax_checker_score(line) for line in lines))
print(
    median(
        autocomplete_score(line) for line in lines if syntax_checker_score(line) == 0
    )
)
