# if(condn):
#     statements
# else:
#    statements
num=int(input("enter any number:"))
if(num%2==0):
    print("even")
else:
    print("odd")
 
# cases
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")

# for loop (initialize; condition; increment/decrement)
for i in range(1, 6):
    print(i)

# palindrome using for loop
num = int(input("Enter a number: "))
temp = num
reverse = 0

for _ in range(len(str(num))):
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


#palindrome using while loop
num = int(input("Enter a number: ")) 
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
