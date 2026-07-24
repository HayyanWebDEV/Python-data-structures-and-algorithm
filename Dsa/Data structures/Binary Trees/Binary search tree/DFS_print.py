

def print_pre_order(node):
    if not node:
        return
    print(node.value, end=" ")
    print_pre_order(node.left)
    print_pre_order(node.right)


def print_inorder(node):
    if node is None:
        return

    print_inorder(node.left)
    print(node.value, end=" ")
    print_inorder(node.right)


def print_postorder(node):
    if node is None:
        return

    print_inorder(node.left)
    print_inorder(node.right)
    print(node.value, end=" ")
