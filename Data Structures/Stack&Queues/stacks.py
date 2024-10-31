# Stacks - LIFO (can be implemented like a dynamic array)
stk = []  # Initialize an empty stack (O(1))

# Push elements onto the stack
stk.append(1)  # O(1)
stk.append(2)  # O(1)
stk.append(3)  # O(1)

print(stk)  # Output entire stack (O(n))

# Remove element from stack (pop operation)
x = stk.pop()  # O(1), as it removes the last element
print(x)
print(stk)  # Output entire stack after pop (O(n))

# Display the top element of stack
print(stk[-1])  # O(1), accessing the last element by index

# Search for an element in stack
if 1 in stk:  # O(n), as it searches through the entire stack if necessary
    print(True)
