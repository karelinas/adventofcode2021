from dataclasses import dataclass
from re import match
from sys import stdin


@dataclass
class Fold:
    axis: str
    location: int


def parse_fold(s):
    axis, location = match(r"fold along (x|y)=(\d+)", s).groups()
    return Fold(axis=axis, location=int(location))


def parse_dots(s):
    return set(tuple(map(int, line.split(","))) for line in s.split())


def fold(dot, fold: Fold):
    x, y = dot
    if fold.axis == "x":
        new_x = 2 * fold.location - x if x > fold.location else x
        return (new_x, y)
    elif fold.axis == "y":
        new_y = 2 * fold.location - y if y > fold.location else y
        return (x, new_y)


def print_dots(dots):
    min_x, _ = min(dots, key=lambda dot: dot[0])
    max_x, _ = max(dots, key=lambda dot: dot[0])
    _, min_y = min(dots, key=lambda dot: dot[1])
    _, max_y = max(dots, key=lambda dot: dot[1])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x, y) in dots else " ", end="")
        print()


if __name__ == "__main__":
    dots, folds = stdin.read().split("\n\n")
    dots = parse_dots(dots)
    folds = [parse_fold(fold) for fold in folds.split("\n") if fold.strip()]

    print(len(set(fold(dot, folds[0]) for dot in dots)))

    for f in folds:
        dots = set(fold(dot, f) for dot in dots)
    print_dots(dots)
