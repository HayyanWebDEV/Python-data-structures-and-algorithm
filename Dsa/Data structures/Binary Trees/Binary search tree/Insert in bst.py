from Array_to_BST import sort_into_bst,list_of_bst,levelOrder
from depth_of_bt import height_of_bt
from DFS_print import print_inorder,print_postorder,print_pre_order
from Show_BST import add_nodes, dot
from Daimeter_of_bt import find_dia
from NODE import Node

def insert_list_to_bst(root,lst):
    for i in lst:
        insert_to_bst(root , i)
    return root

def insert_to_bst(root , val):

    if root is None:
        return Node(val)


    if val > root.value:
        root.right = insert_to_bst(root.right , val)
    else:
        root.left = insert_to_bst(root.left, val)

    return root


unsorted_list = [10,2,3,4,7,5,9,1,0,-1,6,-2,8]
print(unsorted_list)
result = sort_into_bst(unsorted_list)
print_pre_order(result)
num_list = [13 , -3 , 19 , -15]
new_tree = insert_list_to_bst(result , num_list)
print("")
tree_list = list_of_bst(new_tree)
print_pre_order(new_tree)
print("")
print(tree_list)
print_inorder(new_tree)
print("")
print_postorder(new_tree)
print("")
que = levelOrder(new_tree)

for level in que:
    print(' '.join(map(str, level)))

height = height_of_bt(new_tree)
print(f"height of tree is {height}")

dia = find_dia(new_tree)
print(f"diameter of bt is {dia}")

add_nodes(new_tree)
dot.render("bst", format="png", view=True)