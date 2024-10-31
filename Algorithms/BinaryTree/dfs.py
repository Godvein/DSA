# Depth First Search
class TreeNode():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
    
# Tree Structure:
#       1
#      / \
#     5   4
#    / \ /
#   3  2 10

a = TreeNode(1)
b = TreeNode(5)
c = TreeNode(4)
d = TreeNode(3)
e = TreeNode(2)
f = TreeNode(10)

a.left = b
a.right = c
b.right = e
b.left = d
c.left = f

# Pre-order traversal (recursive): root -> left -> right
# Big O Notation: O(n), where n is the number of nodes
def pre_order(node):
    if node is None:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

print("pre-order traversal")
pre_order(a)

# In-order traversal (recursive): left -> root -> right
# Big O Notation: O(n), where n is the number of nodes
def in_order(node):
    if node is None:
        return 
    
    in_order(node.left)
    print(node)
    in_order(node.right)

print("in-order traversal")
in_order(a)

# Post-order traversal (recursive): left -> right -> root
# Big O Notation: O(n), where n is the number of nodes
def post_order(node):
    if node is None:
        return 
    
    post_order(node.left)
    post_order(node.right)
    print(node)

print("post-order traversal")
post_order(a)
        
# Pre-order traversal (iterative): root -> left -> right
# Big O Notation: O(n), where n is the number of nodes
# Space Complexity: O(h), where h is the height of the tree (stack space for DFS)
def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
    
print("pre-order iterative")
pre_order_iterative(a)
