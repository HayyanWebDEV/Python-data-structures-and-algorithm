def find_duplicate(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False

numbers = [23, 43, 34 ,54 ,12 ,23 ,21]

result= find_duplicate(numbers)

if result:
    print("duplicate found")
else:
    print("no duplicate")