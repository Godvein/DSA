# Doubly linked list implementation
class DoublyList():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)
    
# Initialize head and tail
head = tail = DoublyList(1)

# Display doubly linked list
def display_doubly(head):
    # Time complexity: O(n), where n is the number of nodes in the list
    curr = head
    element = []    
    while curr:
        element.append(str(curr.value))
        curr = curr.next

    print(' <-> '.join(element))

display_doubly(head)    

# Add node at the beginning 
def add_in_beginning(value, head, tail):
    # Time complexity: O(1), constant time operation
    new_node = DoublyList(value, prev=None, next=head)
    head.prev = new_node
    return new_node

head = add_in_beginning(5, head, tail)
display_doubly(head)

# Add node at the end
def add_in_end(value, head, tail):
    # Time complexity: O(1), constant time operation
    new_node = DoublyList(value, prev=tail, next=None)
    tail.next = new_node
    return new_node

tail = add_in_end(10, head, tail)
display_doubly(head)

# Search node
def search(head, value):
    # Time complexity: O(n), where n is the number of nodes in the list
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next

    return False

print(search(head, 1))
