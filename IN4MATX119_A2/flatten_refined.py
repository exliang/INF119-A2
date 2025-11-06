
def flatten(arr):
    """Flattens a nested list into a single-level iterator.

    Args:
        arr: A list that may contain nested lists.

    Yields:
        Individual elements from the nested list.
    """
    for x in arr:
        if isinstance(x, list):
            # If x is a list, recursively call flatten and yield its elements
            for y in flatten(x):
                yield y
        else:
            # If x is not a list, yield it directly
            yield x
