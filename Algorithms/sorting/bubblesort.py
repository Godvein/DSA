# Bubble Sort implementation
# Worst-case and Average-case Time Complexity: O(n^2)
# Best-case Time Complexity: O(n) if the array is already sorted

arr = [5, 0, -2, 3, 4, 10, -6]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    # Outer loop keeps running until no swaps are made
    while flag:
        flag = False  # Assume array is sorted initially
        for i in range(1, n):  # Inner loop runs (n-1) times per pass -> O(n)
            if arr[i - 1] > arr[i]:  # Compare adjacent elements
                flag = True  # A swap happened, so array might not be sorted
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Swap if elements are out of order
    
    return arr  # Return the sorted array

print(bubble_sort(arr))
