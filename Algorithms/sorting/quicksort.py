arr = [5, 0, -2, 3, 4, 10, -6]

def quick_sort(arr):
    # n = length of the array
    n = len(arr)
    
    # Base case: An array with 0 or 1 elements is already sorted
    if n <= 1:
        return arr
    
    # Choosing the last element as the pivot
    p = arr[-1]

    # Partition the array into elements less than or equal to the pivot (l) and greater than the pivot (r)
    l = [x for x in arr[:-1] if x <= p]
    r = [x for x in arr[:-1] if x > p]

    # Recursively sort the left and right partitions
    l = quick_sort(l)
    r = quick_sort(r)

    # Combine the sorted partitions and pivot
    return l + [p] + r

# Testing the quick sort function
print(quick_sort(arr))

# Time Complexity:
#   - Average Case: O(n log n)
#     - In the average case, the pivot splits the array into roughly equal halves, requiring log n splits,
#       with each split requiring O(n) to partition the elements.
#     - Total: O(n log n)
#   - Worst Case: O(n^2)
#     - If the pivot is the smallest or largest element (e.g., in
