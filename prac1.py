# Fibonacci Series using Recursive and Non-Recursive Methods

# Recursive Function
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-Recursive Function
def fibonacci_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Main Program
n = int(input("Enter the number of terms: "))

print("\nFibonacci Series (Recursive):", end=" ")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\nFibonacci Series (Non-Recursive):", end=" ")
fibonacci_non_recursive(n)

print()
