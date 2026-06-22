# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n==0:
#             return False
#         while n%3==0:
#             n=n//3
#         return n==1
        
def isPowerOfThree(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n = n // 3
    return n == 1

n = 27
print(isPowerOfThree(n))  # True

# time complexity: O(log3(n))