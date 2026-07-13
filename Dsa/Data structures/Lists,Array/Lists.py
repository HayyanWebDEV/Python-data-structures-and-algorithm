# ==========================
# Python List Big-O Examples
# ==========================

arr = [10, 20, 30, 40, 50]
arr2 = [60, 70, 80]


# --------------------------
# O(1) Operations
# --------------------------

# Access by index
print(arr[2])

# Update by index
arr[2] = 100
print(arr)

# Length
print(len(arr))

# Append (Amortized O(1))
arr.append(60)
print(arr)

# Pop last
arr.pop()
print(arr)


# --------------------------
# O(n) Operations
# --------------------------

# Insert at beginning
arr.insert(0, 5)

# Insert in middle
arr.insert(3, 25)

# Pop from beginning
arr.pop(0)

# Pop from middle
arr.pop(2)

# Remove by value
arr.remove(40)

# Search
print(100 in arr)

# Find index
print(arr.index(10))

# Count occurrences
print(arr.count(100))

# Reverse
arr.reverse()

# Copy
copy_arr = arr.copy()

# Clear
copy_arr.clear()

# Iterate
for item in arr:
    print(item)

# Sum
print(sum(arr))

# Maximum
print(max(arr))

# Minimum
print(min(arr))


# --------------------------
# O(k) Operations
# --------------------------

# Slice
slice_arr = arr[1:4]

# Extend
arr.extend(arr2)


# --------------------------
# O(n + m) Operations
# --------------------------

combined = arr + arr2


# --------------------------
# O(n log n) Operations
# --------------------------

arr.sort()

