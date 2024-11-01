# Selection Sort implementation
# Time Complexity: O(n^2) in all cases (best, average, and worst)
# Space Complexity: O(1) as it sorts in place without extra memory allocation

arr = [5, 0, -2, 3, 4, 10, -6]

def selection_sort(arr):
    n = len(arr)
    # Outer loop goes through each element in the array
    for i in range(n):  # Runs n times -> O(n)
        min_index = i
        # Inner loop finds the minimum element in the unsorted portion
        for j in range(i + 1, n):  # Runs (n - i - 1) times on average -> O(n)
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr  # Return the sorted array

print(selection_sort(arr))
