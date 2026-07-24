def find_factorial(num : int):
    if num <= 0:
        return  1

    fact = num * find_factorial(num - 1)
    return fact

result = find_factorial(10)
print(len(str(result)))
print(result)