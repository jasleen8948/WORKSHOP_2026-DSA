# sorting is a process of arranging items in a particular order, such as ascending or descending order.
#  It is an essential concept in computer science and is used in various applications, including searching, data analysis, and optimization.

# sorting algorithms in Python
# selection sort, bubble sort, insertion sort, merge sort, quick sort, heap sort, counting sort, radix sort, bucket sort, shell sort

# | Algorithm      | Time Complexity (Best)     | Average     | Worst       | Space    | Stable  |
# | -------------- | -------------------------- | ----------- | ----------- | -------- | ------- |
# | Selection Sort | O(n²)                      | O(n²)       | O(n²)       | O(1)     | No      |
# | Bubble Sort    | O(n)                       | O(n²)       | O(n²)       | O(1)     | Yes     |
# | Insertion Sort | O(n)                       | O(n²)       | O(n²)       | O(1)     | Yes     |
# | Merge Sort     | O(n log n)                 | O(n log n)  | O(n log n)  | O(n)     | Yes     |
# | Quick Sort     | O(n log n)                 | O(n log n)  | O(n²)       | O(log n) | No      |
# | Heap Sort      | O(n log n)                 | O(n log n)  | O(n log n)  | O(1)     | No      |
# | Counting Sort  | O(n + k)                   | O(n + k)    | O(n + k)    | O(k)     | Yes     |
# | Radix Sort     | O(d(n + k))                | O(d(n + k)) | O(d(n + k)) | O(n + k) | Yes     |
# | Bucket Sort    | O(n + k)                   | O(n + k)    | O(n²)       | O(n + k) | Depends |
# | Shell Sort     | O(n log n) (gap dependent) | ~O(n^1.5)   | O(n²)       | O(1)     | No      |

# selection sort - Find the minimum element and place it at the beginning.
# def selection_sort(a):
#     n = len(a)
#     for i in range(n):
#         m = i
#         for j in range(i + 1, n):
#             if a[j] < a[m]:
#                 m = j
#         a[i], a[m] = a[m], a[i]
#     return a
# a = [64, 25, 12, 22, 11]
# print(selection_sort(a))

min=float('inf')
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
