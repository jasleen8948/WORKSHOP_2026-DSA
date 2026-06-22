# # search a 2D matrix
# # O(log(m*n)) - logarithmic time complexity


# def search_matrix(matrix, target):
#     if not matrix or not matrix[0]:
#         return False

#     rows, cols = len(matrix), len(matrix[0])
#     left, right = 0, rows * cols - 1

#     while left <= right:
#         mid = left + (right - left) // 2
#         mid_value = matrix[mid // cols][mid % cols]

#         if mid_value == target:
#             return True
#         elif mid_value < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return False
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]]
# target = 3
# print(search_matrix(matrix, target))



# class solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:   
#             return False
#        rows, cols = len(matrix), len(matrix[0])
#        left, right = 0, rows * cols - 1
#        while left <= right:
#            mid = left + (right - left) // 2
#            mid_value = matrix[mid // cols][mid % cols]
#            if mid_value == target:
#                return True
#            elif mid_value < target:
#                left = mid + 1
#            else:
#                right = mid - 1
#        return False

# for i in matrix:
#     for j in i:
#         if j == target:
#             return true
# return false

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in matrix:
#             for j in i:
#                 if j == target:
#                     return True

#         return False