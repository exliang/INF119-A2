def flatten(arr):
    """Yields elements from a nested iterable, unnesting lists."""
    for x in arr:
        if isinstance(x, list):
            yield from flatten(x)  # Use yield from for cleaner delegation
        else:
            yield x  # Yield the element directly if it's not a list

# Example Usage:
# nested_list = [1, [2, 3], [4, [5, 6]], 7]
# for item in flatten(nested_list):
#     print(item)
