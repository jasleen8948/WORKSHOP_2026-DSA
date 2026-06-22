# insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
# It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))