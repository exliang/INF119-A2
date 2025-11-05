
def bucketsort(arr, k):
    """
    Sorts an array of integers using the bucket sort algorithm.

    Assumes all elements in arr are non-negative integers less than k.

    Args:
        arr: A list of non-negative integers.
        k: The maximum possible value in arr + 1 (range of elements is [0, k-1]).

    Returns:
        A new list containing the sorted elements of arr.
    """
    # 1. Initialize a counts array to store the frequency of each element.
    # The size of counts should be k, representing elements from 0 to k-1.
    counts = [0] * k

    # 2. Count the occurrences of each element in the input array.
    # This loop iterates through the input array 'arr'.
    for x in arr:
        # Ensure element is within the valid range [0, k-1]
        if 0 <= x < k:
            counts[x] += 1
        else:
            # Handle elements outside the expected range, or raise an error.
            # For now, we'll raise a ValueError to indicate an issue.
            raise ValueError(f"Element {x} is out of the expected range [0, {k-1}]")

    # 3. Build the sorted array from the counts.
    sorted_arr = []
    # Iterate through the 'counts' array. 'i' will be the element value,
    # and 'count' will be its frequency.
    for i, count in enumerate(counts):
        # Append the element 'i', 'count' times to the sorted_arr.
        sorted_arr.extend([i] * count)

    return sorted_arr
