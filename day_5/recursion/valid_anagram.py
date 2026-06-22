# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

def isAnagram(s, t):
    return sorted(s) == sorted(t)
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         freq = {i: 0 for i in range(26)}
#         if len(s)!=len(t):
#             return false
#         for i in range(len(s)):
#             i+=1
            # freq[s[i]-'a']++(cpp)
            # freq[t[i]-'a']--
            # if i=0 to 26 
            # freq[i]==1

