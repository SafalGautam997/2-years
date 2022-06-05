# calculate the cost of all the items in a shopping cart
total = 0
cart = [69,11,22,33,44,55,66,77,88,99]
for x in cart:
    total = x + total
print(total)

#palindrome or not
text = input("Enter your text: ")
reverse = ""
for char in text:
    reverse = char + reverse
if (text == reverse):
    print("It is palindrome!")
else:
    print("It is not palindrome...")

####
for x in range (2):
    for y in range (2):
        print(str(x)+"-"+str(y))

####
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

####
names = ["RAM","SHYAM","GOPAL"]
for n in names:
    x = 0
    while (x <= 5):
        print(n, end=" ")
        x = x + 1
    print()

#function
def greet():
    print("Hello")
def sum(x,y):
    return x+y
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Sum of the given two numbers is: ", sum(x,y))
greet()

#assignment
#multiplication table
for x in range(1,11):
    for y in range (13):
        print(f'{x} * {y} = {x*y}')
    print("--------------------------------------")

#number is palindrome or not
number=int(input("Enter any number :"))
temp=number
reverse_num=0
while(number>0):
    digit=number%10
    reverse_num=reverse_num*10+digit
    number=number//10
if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

#pattern
for i in range(11):
    for j in range(i):
        print('*', end='')
print('')

#WAP to print 13 X 15 rectangle using "=" python
#.....

#sum of two numbers using function
#without params
def sum():
    sum = 4 + 5
    print(sum)
sum()

#with return and params
def sum(x,y):
    return x+y
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Sum of the given two numbers is: ", sum(x,y))
greet()