# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1)) == 0


def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

print(isPowerOfTwo(1))  # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(3))  # False