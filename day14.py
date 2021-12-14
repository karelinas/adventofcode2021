from collections import Counter
from dataclasses import dataclass
from itertools import chain
from sys import stdin
from typing import Dict

from util import iterated_function


@dataclass
class Polymer:
    pair_counts: Counter
    element_counts: Counter
    rules: Dict[str, str]

    def copy(self):
        return Polymer(
            pair_counts=self.pair_counts.copy(),
            element_counts=self.element_counts.copy(),
            rules=rules,
        )


def insertion(polymer: Polymer) -> Polymer:
    new_polymer = polymer.copy()
    for pair, count in polymer.pair_counts.items():
        if pair in rules:
            new_element = rules[pair]
            left, right = iter(pair)
            new_polymer.element_counts[new_element] += count
            new_polymer.pair_counts[left + new_element] += count
            new_polymer.pair_counts[new_element + right] += count
            new_polymer.pair_counts[pair] -= count
    return new_polymer


template = list(next(stdin).strip())
rules = dict(rule.strip().split(" -> ") for rule in stdin if rule.strip())

polymer_0 = Polymer(
    pair_counts=Counter(
        left + right for left, right in zip(template, template[1:])
    ),
    element_counts=Counter(iter(template)),
    rules=rules,
)

polymer_10 = iterated_function(insertion, start=polymer_0, iterations=10)
polymer_40 = iterated_function(insertion, start=polymer_10, iterations=30)

print(max(polymer_10.element_counts.values()) - min(polymer_10.element_counts.values()))
print(max(polymer_40.element_counts.values()) - min(polymer_40.element_counts.values()))
