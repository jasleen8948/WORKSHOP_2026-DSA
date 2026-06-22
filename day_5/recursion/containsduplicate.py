# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))
    
def containsDuplicate(nums):
    return len(nums) != len(set(nums))