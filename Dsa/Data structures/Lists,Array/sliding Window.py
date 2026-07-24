lisht = [2,3,0,4,10,9,7,5,11]
def brute_force(list):
    group_size = 3
    max_sum = float("-inf")
    start = 0

    for i in range(len(list) - (group_size - 1)):
        current_sum = list[i] + list[i + 1] + list[i + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            start = i

    return max_sum , list[start:start + group_size]

maximum_sum , group = brute_force(lisht)
print(maximum_sum , group)

def sliding_window(list , window_size):
    start = 0
    fst_sum = sum(list[:window_size])
    max_sum = fst_sum
    current_sum = fst_sum

    for i in range( window_size , len(list)):
        current_sum = current_sum - list[i - window_size] + list[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = i - window_size + 1

    return max_sum , list[start:start + window_size]

sld_maximum_sum , sld_group = sliding_window(lisht , 3)
print(sld_maximum_sum , sld_group)