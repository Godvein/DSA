class SinglyLinked():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

# Creating nodes for the linked list
head = SinglyLinked(1)
a = SinglyLinked(2)
b = SinglyLinked(3)
c = SinglyLinked(4)

# Linking the nodes together
head.next = a
a.next = b
b.next = c

def reverse(node):
    # Base case: If the current node is None, return
    if not node:
        return
    
    # Recursive call to reverse the rest of the list
    reverse(node.next)
    
    # Print the current node after the recursive call returns
    print(node)

# Time Complexity: O(n) - We make a single recursive call for each of the n nodes in the linked list.
# Space Complexity: O(n) - The maximum depth of the call stack will be n due to the recursion.
reverse(head)
