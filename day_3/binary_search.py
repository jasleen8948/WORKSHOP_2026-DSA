# binary search algorithm iterative implementation
def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5]
key = 3
binary_search(arr, key)


# binary search algorithm recursive implementation
def binary_search_rec(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_rec(arr, mid + 1, high, key)
    else:
        return binary_search_rec(arr, low, mid - 1, key)