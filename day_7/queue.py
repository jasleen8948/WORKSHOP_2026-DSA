# # queue is a data structure that follows FIFO(first in first out) principle.

# # | Operation  | Meaning                 | Time Complexity |
# # | ---------- | ----------------------- | --------------- |
# # | enqueue(x) | Element add karna       | O(1)            |
# # | dequeue()  | Front se remove karna   | O(1)            |
# # | front()    | Front element dekhna    | O(1)            |
# # | rear()     | Last element dekhna     | O(1)            |
# # | isEmpty()  | Queue empty hai ya nahi | O(1)            |

# from collections import deque

# q = deque()

# q.append(10)
# q.append(20)
# q.append(30)

# print("Front:", q[0])
# print("Rear:", q[-1])

# q.popleft()

# print(q)

# # output
# # Front: 10
# # Rear: 30
# # deque([20, 30])

# from collections import deque

# q = deque()

# def enqueue(x):
#     q.append(x)

# enqueue(10)
# enqueue(20)
# enqueue(30)

# print(q)
