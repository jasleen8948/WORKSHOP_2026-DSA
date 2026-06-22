# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)

#         expected = n * (n + 1) // 2
#         actual = sum(nums)

#         return expected - actual    


def missingNumber(nums):
    n = len(nums)

    expected = n * (n + 1) // 2
    actual = sum(nums)

    return expected - actual

nums = [3, 0, 1]
print(missingNumber(nums))