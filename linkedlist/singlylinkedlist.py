#singly linked list
class SinglyList():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

#creating singly linked list    
head = SinglyList(1)
a = SinglyList(3)
b = SinglyList(5)
c = SinglyList(7)

head.next = a
a.next = b
b.next = c

#display singly linked list
def display_singly(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.value))
        curr = curr.next
        
    print(' -> '.join(element))
display_singly(head)


#search in singly linked list
def search_singly(head, value):
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
        
    return False

print(search_singly(head, 7))

#add a node in beginning
def add_in_beginning(head,value):
    new_node = SinglyList(value, next=head)
    return new_node, head

head, new_head = add_in_beginning(head, 10)
display_singly(head)

#add a node in the end
def add_in_end(tail,end_value):
    new_node = SinglyList(end_value)
    tail.next = new_node
    return new_node, tail

tail, new_tail = add_in_end(c, 15)
display_singly(head)