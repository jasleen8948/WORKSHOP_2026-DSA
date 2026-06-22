# class Solution:
#     def fizzBuzz(self, n: int) -> list[str]:
#         result = []

#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))

#         return result

def fizzBuzz(n):
    ans = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))

    return ans

print(fizzBuzz(15))