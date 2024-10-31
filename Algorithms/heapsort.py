import heapq

# Given array to be sorted
arr = [4, 3, 2, 0, -1, -16, 5, 28, 15, -15]

def heap_sort(arr):
    # O(n): Transform the list into a heap
    heapq.heapify(arr)  
    n = len(arr)
    element = []

    # O(n log n): Repeatedly extract the minimum element from the heap
    while arr:
        # O(log n): Pop the smallest element
        min_elem = heapq.heappop(arr)  
        element.append(min_elem)  # Append the popped element to the result list
    
    return element  # Return the sorted list

# O(n log n): Print the sorted output
print(heap_sort(arr))

