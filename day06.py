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


def iterated_function(n, f, *args):
    return f(*args) if n == 1 else iterated_function(n - 1, f, f(*args))


def fish_count(generation):
    return sum(generation.values())


generation_0 = Counter(int(n) for n in stdin.read().split(","))
generation_80 = iterated_function(80, next_generation, generation_0)
generation_256 = iterated_function(256 - 80, next_generation, generation_80)

print(fish_count(generation_80))
print(fish_count(generation_256))
