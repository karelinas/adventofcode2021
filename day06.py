from collections import Counter
from sys import stdin


def next_generation(current_generation):
    reproduction_count = current_generation[0]
    non_reproducers = Counter(
        {age - 1: count for age, count in current_generation.items() if age > 0}
    )
    reproducers = Counter({6: reproduction_count})
    babies = Counter({8: reproduction_count})
    return non_reproducers + reproducers + babies


def iterated_function(f, *, start, iterations):
    return (
        start
        if iterations == 0
        else iterated_function(f, start=f(start), iterations=iterations - 1)
    )


def fish_count(generation):
    return sum(generation.values())


generation_0 = Counter(int(n) for n in stdin.read().split(","))
generation_80 = iterated_function(next_generation, start=generation_0, iterations=80)
generation_256 = iterated_function(
    next_generation, start=generation_80, iterations=256 - 80
)

print(fish_count(generation_80))
print(fish_count(generation_256))
