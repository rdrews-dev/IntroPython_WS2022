def Fibonacci(n):
    if n < 0:
        print("Negative numbers are not allowed.")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(f"F0: {Fibonacci(0)}")
print(f"F1: {Fibonacci(1)}")
print(f"F2: {Fibonacci(2)}")
print(f"F3: {Fibonacci(3)}")
print(f"F9: {Fibonacci(9)}")
