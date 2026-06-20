# factorial
def factorial(n):
    if n == 0 return 1
    return n * factorial(n - 1)
n = 5
print(factorial(n))  # 120

# recursion is used to reduce the complexity of code
# recursion is a programming technique where a function calls itself in order to solve a problem.

