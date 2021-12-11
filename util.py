def iterated_function(f, *, start, iterations):
    """
    Composes a function with itself many times.

    Function f is called a number of times, starting with f(start) and chaining
    the output of each previous call as the input for the next call.

    I.e.:

        iterations=0 => start
        iterations=1 => f(start)
        iterations=2 => f(f(start))
        iterations=3 => f(f(f(start)))
        ...

    For example, the call

        iterated_function(f, start=0, iterations=2)

    would be equivalent to:

        f(f(0))

    Args:
        f: The function to call.
        start: The initial argument to use for the first call.
        iterations: The number of iterations. Must be greater than or equal to 0.

    Returns:
        The value of the last call to f, or the value of start if iterations=0.
    """
    assert iterations >= 0, "iterations must be greater than or equal to 0"
    return (
        start
        if iterations == 0
        else iterated_function(f, start=f(start), iterations=iterations - 1)
    )



def neighbors(x, y):
    """
    Returns the neighboring coordinates for (x, y), including diagonals.
    """
    # fmt: off
    return [
        (x-1, y-1), (x  , y-1), (x+1, y-1),
        (x-1, y  ),             (x+1, y  ),
        (x-1, y+1), (x  , y+1), (x+1, y+1),
    ]

def is_in_grid(grid, x, y):
    """
    Returns True if (x, y) is within the bounds of the two-dimensional array grid.
    """
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])
