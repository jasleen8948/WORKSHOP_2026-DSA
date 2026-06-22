# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]

def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]