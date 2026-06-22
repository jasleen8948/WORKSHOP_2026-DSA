# stack is  a data structure that follows LIFO (last in first out)
stack = []

stack.append(1)   # push
stack.append(2)
stack.append(3)

print(stack)      # [1, 2, 3]

stack.pop()

print(stack)      # [1, 2]
print(stack[-1])  # 2