from Node import Node

node0 = Node(5)
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node35 = Node(35)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(80)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

def print_node(start):
    current_node = start
    while current_node is not None:
        print(current_node.data , end="->")
        current_node = current_node.next
    print("None")

def insert_node_end(start,node):
    current_node = start
    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = node

def inset_node_begin(start, new_node):
    new_node.next = start
    return new_node

def insert_by_val(start , val , new_node):
    current_node = start
    while current_node is not None and current_node.data != val:
        current_node = current_node.next
    new_node.next = current_node.next
    current_node.next = new_node


def delete_start(start):
    if start is not None:
        return start.next
    return None

def delete_end(start):
    current_node = start
    while current_node.next.next is not None:
        current_node = current_node.next

    current_node.next = None

def delete_by_val(start,val):
    current_node = start
    while current_node.next.data is not val:
        current_node = current_node.next
    current_node.next = current_node.next.next



print_node(head)
insert_node_end(node1 , node7)
print_node(head)
head = inset_node_begin(head , node0)
print_node(head)
head = delete_start(head)
print_node(head)
delete_end(head)
print_node(head)
delete_by_val(head , 20)
print_node(head)
insert_by_val(head,30,node35)
print_node(head)
