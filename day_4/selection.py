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
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min=j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
