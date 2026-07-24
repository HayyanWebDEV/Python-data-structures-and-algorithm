# ===========================
# Python Stack Cheat Sheet
# ===========================

# Create Stack
stack = []

# ---------------------------
# Push (O(1) amortized)
# ---------------------------
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
# [10, 20, 30]


# ---------------------------
# Pop (O(1))
# ---------------------------
item = stack.pop()

print(item)
# 30

print(stack)
# [10, 20]


# ---------------------------
# Peek / Top (O(1))
# ---------------------------
top = stack[-1]

print(top)
# 20


# ---------------------------
# Is Empty (O(1))
# ---------------------------
print(len(stack) == 0)

# Better Python way
print(not stack)


# ---------------------------
# Size (O(1))
# ---------------------------
print(len(stack))


# ---------------------------
# Search (O(n))
# ---------------------------
print(20 in stack)


# ---------------------------
# Index (O(n))
# ---------------------------
print(stack.index(20))


# ---------------------------
# Count (O(n))
# ---------------------------
print(stack.count(20))


# ---------------------------
# Reverse (O(n))
# ---------------------------
stack.reverse()


# ---------------------------
# Copy (O(n))
# ---------------------------
new_stack = stack.copy()


# ---------------------------
# Clear (O(n))
# ---------------------------
stack.clear()


# ---------------------------
# Iterate (O(n))
# ---------------------------
stack = [10, 20, 30]

for item in stack:
    print(item)


# ---------------------------
# Iterate from Top to Bottom
# ---------------------------
for i in range(len(stack)-1, -1, -1):
    print(stack[i])


# ---------------------------
# Push Multiple Items
# ---------------------------
stack.extend([40, 50, 60])


# ---------------------------
# Print Entire Stack
# ---------------------------
print(stack)


# ---------------------------
# Check Top Safely
# ---------------------------
if stack:
    print(stack[-1])
else:
    print("Stack is empty")


# ---------------------------
# Pop Safely
# ---------------------------
if stack:
    print(stack.pop())
else:
    print("Stack is empty")