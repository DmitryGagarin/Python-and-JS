# A balanced binary tree, also referred to as a height-balanced binary tree,
# is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
# Conditions:
# 1) difference between the left and the right subtree for any node is not more than one
# 2) the left subtree is balanced
# 3) the right subtree is balanced

# Checking if a binary tree is height balanced in Python


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

if isHeightBalanced(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')