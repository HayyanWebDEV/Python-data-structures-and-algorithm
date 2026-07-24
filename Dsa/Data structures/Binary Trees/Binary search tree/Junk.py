from NODE import Node

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
chai = Node("chai")
coffee = Node("coffee")
fanta = Node("fanta")
cola = Node("cola")

drinks.left = hot
drinks.right = cold
hot.left = chai
hot.right = coffee
cold.left = fanta
cold.right = cola

print(drinks.value)
print(drinks.left.right.value)