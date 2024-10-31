# Traditional binary search implementation
arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7]

def binary_search(arr, target):
    n = len(arr)
    l = 0
    r = n - 1

    # Time Complexity: O(log n) - In each iteration, we halve the search space, resulting in logarithmic time complexity.
    # Space Complexity: O(1) - We only use a fixed amount of space for variables, regardless of the input size.
    while l <= r:
        m = l + ((r - l) // 2)
        if arr[m] == target:
            return True
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return False

print(binary_search(arr, 7))  # Output: True
