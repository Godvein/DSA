arr = [5, 0, -2, 3, 4, 10, -6]

def merge_sort(arr):
    # n = length of the input array
    n = len(arr)

    # Base case: if the array has only one element, it's already sorted
    if n == 1:
        return arr
    
    # Divide the array into two halves
    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    # Recursively sort both halves
    L = merge_sort(L)
    R = merge_sort(R)

    # Initialize pointers for L and R arrays
    l, r = 0, 0
    l_len = len(L)
    r_len = len(R)

    # Allocate a sorted array to hold the merged result
    sorted_arr = [0] * n
    i = 0

    # Merge the two sorted halves
    while l < l_len and r < r_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    # Copy any remaining elements from L
    while l < l_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    # Copy any remaining elements from R
    while r < r_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr

print(merge_sort(arr))

# Time Complexity: O(n log n)
#   - Splitting the array: O(log n) levels of recursion (each split halves the array).
#   - Merging: At each level, we merge n elements, so the merging operation across all levels is O(n).
#   - Total: O(n log n) due to log n splits, each requiring O(n) merging.

# Space Complexity: O(n)
#   - Auxiliary space for recursion and temporary arrays
