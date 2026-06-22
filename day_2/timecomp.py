# time complexity

# O(n) - linear time complexity
n = 5
for i in range(n):
    print(i)


# O(1) - constant time complexity
# time pta hota h ki constant time me khtm hojayega
for i in range(1, 6):
    print(i)

# O(log n) - logarithmic time complexity
# fraction vale ologn hote like n/2 vgera
n = 100
while n > 1:
    print(n)
    n = n / 2

# o(n^2) - quadratic time complexity
# nested loops me complexity multiply hoti h n^2 hota h, not nested me sum hota hai add hoti h complexity
n = 4

for i in range(n):
    for j in range(n):
        print(i, j)


# O(nlog n) - linearithmic time complexity
n = 8
for i in range(n):      # O(n)
    j = 1
    while j < n:        # O(log n)
        print(i, j)
        j = j * 2

# best case, worst case, average case
# best case - O(1)
# worst case - O(n)
# average case - O(n)

# finding maximum element in an array
# O(n) - linear time complexity
# O(n) - linear space complexity
arr=[1, 2, 3, 4, 5]
mx=arr[0]
for i in range(1, len(arr)):
        mx = max(mx, arr[i])
print(mx)

# count even numbers in an array
# O(n) - linear time complexity
# O(1) - constant space complexity
arr = [1, 2, 3, 4, 5]
count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1
print(count)


# nested loops
# O(n^2) - quadratic time complexity
n = 3
for i in range(n):
    for j in range(n):
        print(i, j)


# triangle loop
# O(n^2) - quadratic time complexity
n=5
for i in range(n):  
    for j in range(i+1): 
        print(j, end="")
    print()


# binary search
# O(log n) - logarithmic time complexity
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# two pointer technique
# O(n) - linear time complexity
left = 0
right = len(arr) - 1

while left < right:
    left += 1
    right -= 1


# reverse array
# O(n) - linear time complexity
arr = [1, 2, 3, 4, 5]
for i in range(len(arr) // 2):
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]

# logarithmic loop
# O(log n) - logarithmic time complexity
n = 16
while n > 1:
    n = n // 2

# doubling loop
# O(log n) - logarithmic time complexity
i = 1
while i < 16:
    i = i * 2

# nested logarithmic loop
# O(log^2 n) - logarithmic time complexity
n = 16
i = 1
while i < n:
    j = 1
    while j < n:
        print(i, j)
        j = j * 2
    i = i * 2

# prefix sum array
# O(n) - linear time complexity
arr = [1, 2, 3, 4, 5]   
prefix_sum = [0] * len(arr)
prefix_sum[0] = arr[0]
for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]


# fibonacci (naive)
# O(2^n) - exponential time complexity
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)