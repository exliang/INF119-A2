def flatten(arr):
    """Flattens a nested list recursively.

    Args:
        arr: A list that may contain nested lists.

    Yields:
        Elements from the flattened list.
    """
    for x in arr:
        if isinstance(x, list):
            # Recursively flatten if the element is a list
            for y in flatten(x):
                yield y
        else:
            # Yield the element directly if it's not a list
            yield x