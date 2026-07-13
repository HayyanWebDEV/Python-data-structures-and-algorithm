MY_List = [13, 32, 53, 122, 46, 76, 89, 35]

for marks in MY_List:
    print(marks)

print("------------------------------------------------------")

for i in range(len(MY_List)):
    print(MY_List[i])

print("------------------------------------------------------")

for marks in reversed(MY_List):
    print(marks)

print("------------------------------------------------------")

for marks in MY_List[::-1]:
    print(marks)

print("------------------------------------------------------")
print("--------------------Nested List-----------------------")
print("------------------------------------------------------")

Nested_list = [[80, 90, 100],[20 , 40 , 60],[10 , 50 , 70]]
for Row in Nested_list:
    for item in Row:
        print(item , end=" ")
    print()

print("------------------------------------------------------")
print("------------------------Search------------------------")
print("------------------------------------------------------")

Array = [1,2,3,4,5,6,7]
target = 3

#Nested loops O(n2)

for i in Array:
    for j in Array:
        if i + j == target:
            print(f'{i}+{j} True ')


# Two Pointer O(n)

left_index = 0
right_index = len(Array) - 1

while left_index < right_index:

    current = Array[left_index] + Array[right_index]

    if current == target:
        print(f"{Array[left_index]} + {Array[right_index]} = {target}")
        break

    elif current > target:
        right_index -= 1

    elif current < target:
        left_index += 1

    else:
        print("target is not in range")

#Search and Remove Duplicates by two Pointer
def find_duplicates(list):
    left = 0
    for right in range(1 ,len(list)):
        if list[left] != list[right]:
            left += 1
            list[left] = list[right]

    return left + 1

numbers = [1,2,3,3,4,5,5,6,7,7,7,8,8,9,10,10,11]
clean_list = find_duplicates(numbers)
print(numbers[:clean_list])


