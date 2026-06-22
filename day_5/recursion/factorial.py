# factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = 5
print(factorial(n))  # 120

# recursion is used to reduce the complexity of code
# recursion is a programming technique where a function calls itself in order to solve a problem.

# time complexity of factorial is O(n) - linear time complexity 
# sir ne bola O(1) - constant time complexity but that is not correct because the function calls itself n times.