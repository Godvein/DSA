# Insertion Sort implementation
# Worst-case and Average-case Time Complexity: O(n^2)
# Best-case Time Complexity: O(n) if the array is already sorted

arr = [5, 0, -2, 3, 4, 10, -6]

def insertion_sort(arr):
    n = len(arr)
    # Outer loop goes through each element from index 1 to n-1
    for i in range(1, n):  # Outer loop runs (n-1) times -> O(n)
        # Inner loop compares the current element with the sorted portion
        for j in range(i, 0, -1):  # Inner loop runs up to i times in worst case
            if arr[j - 1] > arr[j]:  # Swap if previous element is greater
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # This swap takes constant time O(1)
            else:
                break  # Exit if elements are in the correct order
    return arr

print(insertion_sort(arr))
