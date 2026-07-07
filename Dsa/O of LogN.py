def find_name(names_list , name):
    left = 0
    right = len(names_list) - 1
    while left <= right:
        middle = (left + right) // 2

        if names_list[middle] == name:
            return middle
        elif names_list[middle] < name:
            left = middle + 1
        else:
            right = middle - 1
    return -1

names = ["ali","bilai","fazal","hayyan", "hamza","iqbal","musa"]

result = find_name(names,"hayyan")

if result != -1 :
    print(f"found at {result}")

else:
    print("name not found")