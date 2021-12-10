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


def syntax_checker_score(character):
    point_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return point_values[character]


def autocomplete_score(open_chunks):
    point_values = {"(": 1, "[": 2, "{": 3, "<": 4}
    return reduce(lambda x, y: x * 5 + point_values[y], reversed(open_chunks), 0)


lines = [parse(line.strip()) for line in stdin]
print(sum(syntax_checker_score(unexpected) for _, unexpected in lines if unexpected))
print(
    median(
        autocomplete_score(open_chunks)
        for open_chunks, unexpected in lines
        if not unexpected
    )
)
