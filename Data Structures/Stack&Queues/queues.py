# Queues - FIFO

from collections import deque

# Initialize deque (double-ended queue)
d = deque()  # O(1), initializing an empty deque

# Adding elements to the queue
d.append(1)  # O(1), appending to the end
d.append(2)  # O(1)
d.append(3)  # O(1)

print(d)  # O(n), printing the entire queue (where n is the number of elements in the queue)

# Pop from left as standard queue (dequeue operation)
d.popleft()  # O(1), removing from the front

print(d)  # O(n), printing the queue after pop

# Display the front element of the queue (peek operation)
print(d[0])  # O(1), accessing the first element

# Display the last element of the queue (rear view)
print(d[-1])  # O(1), accessing the last element
