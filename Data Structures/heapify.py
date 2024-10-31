import heapq
#min heap
# Given list
a = [-1, -5, 0, 10, -6, 15, 7, 9, 4, -10]

# Convert the list into a heap in O(n) time complexity
heapq.heapify(a)  
print(a)  # Output the heap

# Push a new element (12) onto the heap in O(log n) time complexity
heapq.heappush(a, 12)  
print(a)  # Output the heap after pushing

# Pop the smallest element from the heap in O(log n) time complexity
heapq.heappop(a)  
print(a)  # Output the heap after popping


#max heap

# Given array
b = [-1, -5, 0, 10, -6, 15, 7, 9, 4, -10]

# Step 1: Negate the values to create a max heap using min heap
for i in range(len(b)):
    b[i] = -b[i]  # Swapping the negatives creates a max heap

# Step 2: Heapify the negated list in O(n) time
heapq.heapify(b)  
print(b)  # Print the max heap (negated)

# Step 3: Get the maximum value (original value) by popping the smallest from the negated heap
max_value = -heapq.heappop(b)  # O(log n) time to pop the max value
print(max_value)  # Print the maximum value
