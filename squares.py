"""Computation of weighted average of squares."""

def average_of_squares(list_of_numbers, list_of_weights=None):
    """
    Return the (weighted) average of the squares of the values.

    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.

    Examples
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length
    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)

    numerator = sum(w * (x * x) for x, w in zip(list_of_numbers, effective_weights))
    denom = sum(effective_weights)
    if denom == 0:
        raise ValueError("sum of weights must be > 0")
    return numerator / denom


def convert_numbers(list_of_strings):
    """
    Convert a list of strings into integers, ignoring whitespace.

    Examples
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]
    """
    tokens = []
    for s in list_of_strings:
        # split() collapses whitespace and strips; no need to strip() each token
        tokens.extend(s.split())
    return [int(t) for t in tokens]


if __name__ == "__main__":
    numbers_strings = ["1", "2", "4"]
    weight_strings = ["1", "1", "1"]

    numbers = convert_numbers(numbers_strings)
    weights = convert_numbers(weight_strings)

    result = average_of_squares(numbers, weights)
    print(result)
