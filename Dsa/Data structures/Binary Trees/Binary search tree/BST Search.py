from NODE import Node

def search(root, node):
    if root is not None:
        if root.value == node:
            return True
        elif root.value > node:
            return search(root.left , node)
        else:
            return search(root.right, node)
    return False


# rooot = Node(6)
# rooot.left = Node(2)
# rooot.right = Node(8)
# rooot.right.left = Node(7)
# rooot.right.right = Node(9)
#
# key = 7
# print(search(rooot , key))