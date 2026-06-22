# swapping
# a = 10
# b = 20
# a, b = b, a
# print("a =", a)
# print("b =", b)
# sum of two numbers
# d=30
# e=20
# c=sum((d,e))
# print(c)
# #swapping
# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print("a =", a)
# print("b =", b)
x = 10   # Global variable

def show():
    y = 20   # Local variable
    print(x)
    print(y)

show()

print(x)