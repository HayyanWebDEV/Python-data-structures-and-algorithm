num_list = [1,2,3,4,5,6,7,8,9,12,32,23,41,19,80]
target_num = int(input("enter a number:"))

def two_sum(number , target):
    seen = {}

    for i, nums in enumerate(number):
        sum_target = target
        need = sum_target - nums

        if need in seen:
            return [seen[need], i]

        else:
            seen[nums] = i
            
    return 'not found'

result_list = two_sum(num_list , target_num)
print(result_list)