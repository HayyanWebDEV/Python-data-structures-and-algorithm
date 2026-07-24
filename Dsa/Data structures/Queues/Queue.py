"""
==========================================================
                PYTHON QUEUE CHEAT SHEET
==========================================================
Built-in Queue using collections.deque
Time complexities are listed for every operation.
"""

from collections import deque

# ==========================================================
# CREATE A QUEUE
# ==========================================================

queue = deque()                      # O(1)

queue = deque([10, 20, 30])          # O(n)

queue = deque(maxlen=5)              # O(1)

print(queue)

# ==========================================================
# ENQUEUE (Add to Rear)
# Time: O(1)
# ==========================================================

queue.append(40)

print(queue)

# ==========================================================
# DEQUEUE (Remove from Front)
# Time: O(1)
# ==========================================================

item = queue.popleft()

print(item)
print(queue)

# ==========================================================
# PEEK FRONT
# Time: O(1)
# ==========================================================

front = queue[0]

print(front)

# ==========================================================
# PEEK REAR
# Time: O(1)
# ==========================================================

rear = queue[-1]

print(rear)

# ==========================================================
# SIZE
# Time: O(1)
# ==========================================================

print(len(queue))

# ==========================================================
# IS EMPTY
# Time: O(1)
# ==========================================================

print(len(queue) == 0)

# ==========================================================
# APPENDLEFT (Insert at Front)
# Time: O(1)
# ==========================================================

queue.appendleft(5)

print(queue)

# ==========================================================
# POP (Remove Rear)
# Time: O(1)
# ==========================================================

last = queue.pop()

print(last)
print(queue)

# ==========================================================
# CLEAR
# Time: O(n)
# ==========================================================

queue.clear()

print(queue)

# ==========================================================
# EXTEND
# Add multiple elements to rear
# Time: O(k)
# ==========================================================

queue.extend([1, 2, 3, 4])

print(queue)

# ==========================================================
# EXTENDLEFT
# Inserts in reverse order
# Time: O(k)
# ==========================================================

queue.extendleft([-2, -1, 0])

print(queue)

# Output:
# deque([0, -1, -2, 1, 2, 3, 4])

# ==========================================================
# ROTATE RIGHT
# Time: O(min(|n|, len(queue)))
# ==========================================================

queue.rotate(2)

print(queue)

# ==========================================================
# ROTATE LEFT
# Time: O(min(|n|, len(queue)))
# ==========================================================

queue.rotate(-2)

print(queue)

# ==========================================================
# REVERSE
# Time: O(n)
# ==========================================================

queue.reverse()

print(queue)

# ==========================================================
# COUNT
# Time: O(n)
# ==========================================================

queue.append(2)

print(queue.count(2))

# ==========================================================
# REMOVE FIRST OCCURRENCE
# Time: O(n)
# ==========================================================

queue.remove(2)

print(queue)

# ==========================================================
# INDEX OF ELEMENT
# Time: O(n)
# ==========================================================

print(queue.index(3))

# ==========================================================
# COPY
# Time: O(n)
# ==========================================================

copy_queue = queue.copy()

print(copy_queue)

# ==========================================================
# MEMBERSHIP
# Time: O(n)
# ==========================================================

print(3 in queue)

# ==========================================================
# ITERATION
# Time: O(n)
# ==========================================================

for item in queue:
    print(item)

# ==========================================================
# ENUMERATE
# Time: O(n)
# ==========================================================

for index, value in enumerate(queue):
    print(index, value)

# ==========================================================
# INDEXING
# Time:
# Ends: O(1)
# Middle: O(n)
# ==========================================================

print(queue[0])
print(queue[-1])

# ==========================================================
# CONVERT TO LIST
# Time: O(n)
# ==========================================================

lst = list(queue)

print(lst)

# ==========================================================
# LIST TO QUEUE
# Time: O(n)
# ==========================================================

queue = deque(lst)

print(queue)

# ==========================================================
# MAXLEN
# Automatically removes oldest items when full
# ==========================================================

fixed_queue = deque(maxlen=3)

fixed_queue.append(1)
fixed_queue.append(2)
fixed_queue.append(3)

print(fixed_queue)

fixed_queue.append(4)

print(fixed_queue)
# deque([2, 3, 4])

# ==========================================================
# QUEUE EXAMPLE (FIFO)
# ==========================================================

queue = deque()

# Enqueue
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print(queue)

# Peek
print(queue[0])

# Dequeue
print(queue.popleft())

print(queue)

# ==========================================================
# TIME COMPLEXITY SUMMARY
# ==========================================================

"""
append()            O(1)
appendleft()        O(1)
pop()               O(1)
popleft()           O(1)
peek front          O(1)
peek rear           O(1)
len()               O(1)
is_empty            O(1)

clear()             O(n)
extend()            O(k)
extendleft()        O(k)
rotate()            O(min(|n|, len))
reverse()           O(n)
count()             O(n)
remove()            O(n)
index()             O(n)
copy()              O(n)
membership (in)     O(n)
iteration           O(n)
list(queue)         O(n)
deque(list)         O(n)

Queue Operations
----------------
Enqueue             append()
Dequeue             popleft()
Front               queue[0]
Rear                queue[-1]
"""