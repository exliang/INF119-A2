from collections.abc import Iterable

def flatten(arr):
    """
    Recursively flattens a nested iterable, yielding elements one by one.

    Args:
        arr: The iterable to flatten.

    Yields:
        Elements from the flattened iterable.

    Raises:
        TypeError: If the input `arr` is not iterable.
    """
    if not isinstance(arr, Iterable):
        raise TypeError(f"Input must be an iterable, but got {type(arr).__name__}")

    for x in arr:
        # Check if x is an iterable but not a string (which we want to treat as atomic)
        if isinstance(x, Iterable) and not isinstance(x, str):
            # Recursively flatten the sub-iterable
            yield from flatten(x)
        else:
            # Yield the atomic element
            yield x