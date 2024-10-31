from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
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

# Level Order Traversal (BFS)
def level_order(node):
    d = deque()
    d.append(node)

    while d:
        node = d.popleft()
        print(node)
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)

# Time Complexity: O(N) - Each node is visited once.
# Space Complexity: O(W) - W is the maximum width of the tree, which can be at most O(N) in a completely balanced tree.

level_order(a)

# Binary Search Tree Structure
#       5
#    1      8
# -1   3   7    9

a2 = TreeNode(5)
b2 = TreeNode(1)
c2 = TreeNode(8)
d2 = TreeNode(-1)
e2 = TreeNode(3)
f2 = TreeNode(7)
g2 = TreeNode(9)

a2.left = b2
a2.right = c2
b2.left = d2
b2.right = e2
c2.left = f2
c2.right = g2

# Searching in Binary Search Tree
def search(node, target):
    if node is None:
        return False
    
    if node.value == target:
        return True 
    
    if target > node.value:
        return search(node.right, target)
    else:
        return search(node.left, target)

# Time Complexity: O(H) - H is the height of the tree. In the worst case (for a degenerate tree), it can be O(N).
# Space Complexity: O(H) - The space complexity is O(H) due to the call stack in recursion.

print(search(a2, -1))
