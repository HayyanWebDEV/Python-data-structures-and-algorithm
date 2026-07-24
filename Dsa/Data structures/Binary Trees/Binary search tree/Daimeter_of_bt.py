def find_dia(node):

    diameter = 0

    def diameter_of_bt(root):
        nonlocal diameter

        if root is None:
            return 0

        left = diameter_of_bt(root.left)
        right = diameter_of_bt(root.right)

        diameter = max(diameter,(left + right))

        return 1 + max(left, right)

    diameter_of_bt(node)
    return diameter