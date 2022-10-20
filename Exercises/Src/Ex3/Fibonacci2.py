def Fibonacci(n):
    numbers = [0, 1, 1, 2]

    for i in range(4, n + 1):
        fib_2 = numbers[i - 2]
        fib_1 = numbers[i - 1]
        numbers.append(fib_1 + fib_2)
    return numbers[n]

def Fibonacci2(n):
    fib_2 = 0 # n - 2
    fib_1 = 1 # n - 1
    fib_0 = 1 # n

    if n == 0:
        return 0

    for _ in range(2, n + 1):
        fib_0 = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib_0

    return fib_0

print(f"f0: {Fibonacci(0)}")
print(f"f1: {Fibonacci(1)}")
print(f"f2: {Fibonacci(2)}")
print(f"f3: {Fibonacci(3)}")
print(f"f9: {Fibonacci(9)}")

print("\n")

print(f"f0: {Fibonacci2(0)}")
print(f"f1: {Fibonacci2(1)}")
print(f"f2: {Fibonacci2(2)}")
print(f"f3: {Fibonacci2(3)}")
print(f"f9: {Fibonacci2(9)}")
