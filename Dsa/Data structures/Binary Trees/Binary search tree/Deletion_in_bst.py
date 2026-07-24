import Array_to_BST

def delete_in_Bst(tree_list,value):
    for x in range(len(tree_list) - 1):
        if tree_list[x] == value:
            tree_list.pop(x)



    binary_tree = Array_to_BST.sort_into_bst(tree_list)
    tree_list = Array_to_BST.list_of_bst(binary_tree)

    return tree_list

unsorted_list = [10,2,3,4,7,5,9,1,0,-1,6,-2,8]
val = 8
bleh = delete_in_Bst(unsorted_list,val)
print(bleh)