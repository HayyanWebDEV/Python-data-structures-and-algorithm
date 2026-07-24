bleh = [1,2,3,4,5,6,7,8,10,21,6,3,91,25,11]

import heapq
heapq.heapify(bleh) #O (n)

print(bleh)

heapq.heappush( bleh,-4) # O(log n)

print(bleh)

heapq.heappop(bleh) # O(logn)

print(bleh)

#heapsort

def heapsort(arr):
    sorted_list = []
    heapq.heapify(arr)

    for i in range(len(arr)):
        min = heapq.heappop(arr)
        sorted_list.append(min)

    return sorted_list

lll = heapsort(bleh)
print(lll)