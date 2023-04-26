class ThirdNode:
    def __init__(self):
        self.data = None
        self.se = None
        self.left = None
        self.right = None


tree = ThirdNode()


def third_insertion(root_tree, name, se):
    # print(root_tree.data)
    if root_tree is None: root_tree = ThirdNode()
    if root_tree.data is None:
        root_tree.data = name
        print(root_tree.data, 'stored at third tree.')
    elif se < root_tree.se:
        third_insertion(root_tree.left, name, se)
    else:
        third_insertion(root_tree.right, name, se)


def get_third(root_tree, name, se):
    # print('We reach', root_tree.data)
    if root_tree.data is not None:
        return root_tree.data
    elif root_tree.se and se < root_tree.se:
        return get_third(root_tree.left, name, se)
    elif root_tree.se:
        return get_third(root_tree.right, name, se)
    return None


def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)

# printing(tree)

# def get_tree():
#     return tree
