# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split()
#         return len(words[-1])

def lengthOfLastWord(s):
    words = s.split()
    return len(words[-1])

s = "Hello World"
print(lengthOfLastWord(s))