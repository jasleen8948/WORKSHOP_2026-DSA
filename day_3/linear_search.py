def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
key = 3
linear_search(arr, key)