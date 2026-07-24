from NODE import Node

def sort_into_bst(arry):
    arry.sort()

    def build_bst(left,right):
        if left > right:
            return None

        middle = (left + right) // 2
        root_node = Node(arry[middle])

        root_node.left = build_bst(left ,  middle - 1)
        root_node.right = build_bst(middle + 1 , right)

        return root_node

    return build_bst(0 , len(arry) - 1)

# create a preorder List

def list_of_bst(node):
    if not node:
        return []

    tree = []

    tree.append(node.value)
    tree.extend(list_of_bst(node.left))
    tree.extend(list_of_bst(node.right))

    return tree

def bfs_print(node, level, que):
    # Base case
    if node is None:
        return

    # Add a new level to the result if needed
    if len(que) <= level:
        que.append([])

    # Add current node's data to its corresponding level
    que[level].append(node.value)

    # Recur for left and right children
    bfs_print(node.left, level + 1, que)
    bfs_print(node.right, level + 1, que)

# Function to perform level order traversal
def levelOrder(node):
    # Stores the result level by level
    queues = []
    bfs_print(node, 0, queues)
    return queues


# unsorted_list = [10,2,3,4,7,5,9,1,0,-1,6,-2,8]
# result = sort_into_bst(unsorted_list)
# print(result.left.left.right.value)
# print_pre_order(result)
