# search insert position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def search_insert(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
arr = [1, 3, 5, 6]
target = 5
print(search_insert(arr, target))

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left

# second approach

# if(l==r && nums[l] != target):
#   if (nums[l] < target):
#        return l+1;