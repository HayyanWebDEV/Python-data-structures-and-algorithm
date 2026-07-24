from graphviz import Digraph

dot = Digraph()

def add_nodes(node):
    if node is None:
        return

    dot.node(str(id(node)), str(node.value))

    if node.left:
        dot.edge(str(id(node)), str(id(node.left)))
        add_nodes(node.left)

    if node.right:
        dot.edge(str(id(node)), str(id(node.right)))
        add_nodes(node.right)

