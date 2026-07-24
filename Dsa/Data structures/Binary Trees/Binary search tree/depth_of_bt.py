def height_of_bt(root):
    if root is None:
        return 0

    left = height_of_bt(root.left)
    right = height_of_bt(root.right)

    return 1 + max(left, right)