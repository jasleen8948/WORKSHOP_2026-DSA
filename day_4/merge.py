# merge sort is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves.

def merge_sort(a):
    # base case
    if len(a) <= 1:
        return a
    m = len(a) // 2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
    return res + l[i:] + r[j:]
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
    
