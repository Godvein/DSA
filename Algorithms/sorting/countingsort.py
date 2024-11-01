arr = [5, 0, 2, 3, 4, 10, 6]

def counting_sort(arr):
    n = len(arr)               # Number of elements in the array
    maxx = max(arr)             # Find the maximum element in the array
    count = [0] * (maxx + 1)    # Create a count array of size max + 1

    # Step 1: Count the occurrences of each element
    for x in arr:
        count[x] += 1
    
    # Step 2: Reconstruct the sorted array from the count array
    i = 0
    for c in range(maxx + 1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

    return arr

print(counting_sort(arr))

# Time Complexity:
#   - O(n) for counting the elements in the original array.
#   - O(k) for iterating through the count array to reconstruct the sorted array, where k = max(arr) + 1.
#   - Total Time Complexity: O(n + k), where n is the number of elements and k is the range of input values.

# Space Complexity: O(k)
#   - We use a count array of size max(arr) + 1, which depends on the range of values, not on the number of elements.
