
def bucketsort(arr: list[int], k: int) -> list[int]:
    """
    Sorts a list of non-negative integers using the Counting Sort algorithm.

    Args:
        arr: A list of non-negative integers to be sorted.
        k: The exclusive upper bound of the values in arr. 
           Assumes values in arr are in the range [0, k-1].

    Returns:
        A new list containing the sorted elements of arr.
    """
    if not arr:
        return []

    # Initialize counts array with size k, all elements set to 0.
    # counts[i] will store the frequency of value i in arr.
    counts = [0] * k

    # Count the occurrences of each element in arr.
    for x in arr:
        if not (0 <= x < k):
            raise ValueError(f"Element {x} is out of the expected range [0, {k-1})")
        counts[x] += 1

    sorted_arr = []
    # Reconstruct the sorted array based on the counts.
    # For each number 'num' from 0 to k-1, add it 'count' times.
    for num, count in enumerate(counts):
        sorted_arr.extend([num] * count)

    return sorted_arr
