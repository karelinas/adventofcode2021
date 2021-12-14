from collections import Counter
from itertools import chain
from sys import stdin


def insertion(polymer, rules):
    return chain(
        *[
            (
                left,
                rules[left + right],
            )
            if left + right in rules
            else (left,)
            for left, right in zip(polymer, polymer[1:])
        ],
        (polymer[-1],)
    )


polymer = list(next(stdin).strip())
rules = dict(tuple(rule.strip().split(" -> ")) for rule in stdin if len(rule.strip()))

for _ in range(10):
    polymer = list(insertion(polymer, rules))

counter = Counter(polymer)
print(max(counter.values()) - min(counter.values()))
