num_list = [1,3,2,4,7,5,15,19,10,11,18,30,0                  ]
num_list.sort()
for item in range(len(num_list) - 1):
    num_list.pop(0)
max_num = num_list
print(max_num[0])