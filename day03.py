from collections import Counter
from itertools import count
from sys import stdin


def inverse(bit):
    return "0" if bit == "1" else "1"


def power_consumption(numbers):
    most_common = [
        Counter(position).most_common(1)[0][0] for position in map(list, zip(*numbers))
    ]
    least_common = map(inverse, most_common)
    gamma_rate = int("".join(most_common), 2)
    epsilon_rate = int("".join(least_common), 2)
    return gamma_rate * epsilon_rate


def all_equal(lst):
    return len(set(lst)) == 1


def preferred_most_common(position, preferred="1"):
    counter = Counter(position)
    return preferred if all_equal(counter.values()) else counter.most_common(1)[0][0]


def oxygen_generator_criteria(position):
    return preferred_most_common(position)


def co_scrubber_criteria(position):
    return inverse(preferred_most_common(position))


def rating(numbers, bit_criteria):
    for i in count():
        ith_bits = [num[i] for num in numbers]
        wanted_bit = bit_criteria(ith_bits)
        numbers = list(filter(lambda num: num[i] == wanted_bit, numbers))
        if len(numbers) == 1:
            break
    return int(numbers[0], 2)


def life_support_rating(numbers):
    oxygen_generator_rating = rating(numbers, bit_criteria=oxygen_generator_criteria)
    co_scrubber_rating = rating(numbers, bit_criteria=co_scrubber_criteria)
    return oxygen_generator_rating * co_scrubber_rating


numbers = [line.strip() for line in stdin]
print(power_consumption(numbers))
print(life_support_rating(numbers))
