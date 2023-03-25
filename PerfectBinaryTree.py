# A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes
# and all the leaf nodes are at the same level.

# Checking if a binary tree is a perfect binary tree in Python


class NewNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


# Calculate the depth
def calculateDepth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d


# Check if the tree is a perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if root is None:
        return True

    # Check the presence of trees
    if root.left is None and root.right is None:
        return d == level + 1

    if root.left is None or root.right is None:
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))


root = NewNode(1)
root.left = NewNode(2)
root.right = NewNode(3)
root.left.left = NewNode(4)
root.left.right = NewNode(5)
root.right.right = NewNode(6)
root.right.left = NewNode(7)

if is_perfect(root, calculateDepth(root)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")