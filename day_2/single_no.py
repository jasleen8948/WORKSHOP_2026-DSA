# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0

#         for num in nums:
#             ans ^= num

#         return ans

def singleNumber(nums):
    ans = 0

    for num in nums:
        ans ^= num

    return ans