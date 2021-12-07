def constant_cost(n):
    return n


def increasing_cost(n):
    return n * (n + 1) // 2


def find_cheapest(nums, *, cost_function):
    start = min(nums)
    end = max(nums)
    return min(
        sum(cost_function(abs(n - alignment)) for n in nums)
        for alignment in range(start, end + 1)
    )


data = sorted(int(num) for num in input().split(","))
print(find_cheapest(data, cost_function=constant_cost))
print(find_cheapest(data, cost_function=increasing_cost))
