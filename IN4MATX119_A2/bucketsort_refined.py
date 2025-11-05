
def bucketsort(arr, k):
    # Initialize a list to store the frequency of each number.
    # The size of the list is k, assuming numbers are in the range [0, k-1].
    counts = [0] * k

    # Count the occurrences of each number in the input array.
    # Assumes all elements in arr are non-negative and less than k.
    for x in arr:
        # Potential IndexError if x is out of range [0, k-1].
        # Based on the problem description, we assume valid input.
        counts[x] += 1

    # Build the sorted array.
    sorted_arr = []
    # Iterate through the counts list. 'i' represents the number,
    # and 'count' is its frequency.
    for i, count in enumerate(counts):
        # Extend the sorted_arr by adding 'i' 'count' times.
        sorted_arr.extend([i] * count)

    return sorted_arr
