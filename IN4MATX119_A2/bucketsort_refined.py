
def bucketsort(arr, k):
    """
    Sorts an array of non-negative integers less than k using a counting sort approach.

    Args:
        arr (list): A list of non-negative integers.
        k (int): The upper bound (exclusive) of the integers in arr.

    Returns:
        list: A new list containing the sorted elements of arr.
    """
    # Initialize a list to store the count of each number.
    # The size of this list is k, representing numbers from 0 to k-1.
    counts = [0] * k

    # Count the occurrences of each number in the input array.
    for x in arr:
        # Ensure the element is within the valid range [0, k-1]
        if not (0 <= x < k):
            raise ValueError(f"Element {x} is out of the specified range [0, {k-1})")
        counts[x] += 1

    # Build the sorted array based on the counts.
    sorted_arr = []
    # Iterate through the possible numbers (from 0 to k-1).
    for i in range(k):
        # For each number i, append it to sorted_arr 'counts[i]' times.
        # This is where the original code had a bug, iterating over 'arr' instead of 'counts'.
        sorted_arr.extend([i] * counts[i])

    return sorted_arr
