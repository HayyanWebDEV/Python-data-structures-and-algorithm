def find_fib(n: int):
    if n == 1 or n == 2:
        return 1

    sequence = find_fib(n - 1) + find_fib(n - 2)
    return sequence

print(find_fib(10))