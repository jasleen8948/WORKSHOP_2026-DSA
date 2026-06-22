# fibonacci
# O(2^n) - exponential time complexity
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)