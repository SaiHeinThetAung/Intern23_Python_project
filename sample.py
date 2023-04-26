class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
        self.third = None
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)


# Create binary tree
root = Node('m')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z']
for letter in letters:
    root = insert(root, letter)

# Print the inorder traversal of the tree
#inorder_traversal(root)
