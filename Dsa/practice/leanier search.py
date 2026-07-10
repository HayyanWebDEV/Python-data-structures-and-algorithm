list = ['aloo','basmati','chaat','daal','egg','fish','guava']
def findfood(food_list , food):
    for i in range(len(food_list)):
        if food_list[i] == food:
            return True , i
    return False , -1

name = "chaat"
result, index = findfood(list ,name)

if result:
    print(f"found {name} at {index} index")
else:
    print(f"could not find {name}")

