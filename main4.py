# Question 1

usr_inp = int(input("Enter any number: "))
if usr_inp % 2 == 0:
    print('The given number is even')
else:
    print('The given number is odd')

# Question 2

a = int(input("Enter a: "))
for i in range(1, a):
    if (i % 3) == 0 and (i % 5) == 0:
        print('FizzBuzz')
    elif (i % 3) == 0:
        print('Fizz')
    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)
# done by finding how to loop in pyhton

# Question 3

usr_ut = int(input("Enter the power consumption in unit: "))
if (usr_ut > 0) and (usr_ut < 100):
    print("No recharge needed!!")
elif (usr_ut >= 100) and (usr_ut < 200):
    total = usr_ut * 5
    print("Your total amount is ", total)
elif usr_ut >= 200:
    total = usr_ut * 10
    print("Your total amount is ",total)
else:
    print("Error...Try Again")

#Question 4

x = input("Enter any number ")
last_inp = x[-1]
if int(last_inp) % 3 == 0:
    print("The number is divisible by 3 ")
else:
    print("The number is not divisible by 3 ")

#Question 5

one = int(input("Enter the first side "))
two = int(input("Enter the second side "))
three = int(input("Enter the third side "))

if one == two == three:
    print(" It is Equilateral Triangle")
elif one == two or two == three or one == three:
    print("It is an Isosceles Triangle")
else:
    print("It is a Scaler Triangle")