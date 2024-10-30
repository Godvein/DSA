# Singly linked list implementation
class SinglyList():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

# Creating singly linked list    
head = SinglyList(1)
a = SinglyList(3)
b = SinglyList(5)
c = SinglyList(7)

head.next = a
a.next = b
b.next = c

# Display singly linked list
def display_singly(head):
    # Time complexity: O(n), where n is the number of nodes in the list
    curr = head
    element = []
    while curr:
        element.append(str(curr.value))
        curr = curr.next
        
    print(' -> '.join(element))

display_singly(head)

# Search in singly linked list
def search_singly(head, value):
    # Time complexity: O(n), where n is the number of nodes in the list
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
        
    return False

print(search_singly(head, 7))

# Add a node at the beginning
def add_in_beginning(head, value):
    # Time complexity: O(1), constant time operation
    new_node = SinglyList(value, next=head)
    return new_node

head = add_in_beginning(head, 10)
display_singly(head)

# Add a node at the end
def add_in_end(tail, end_value):
    # Time complexity: O(1), constant time operation
    new_node = SinglyList(end_value)
    tail.next = new_node
    return new_node

tail = add_in_end(c, 15)
display_singly(head)
