#Question 1 Build a car game

hint_str = ''' 
start - Start the car
stop - Stop the car
help - Help request
quit - Quit the game
'''
start = False
while True:
    user_inp = input("Enter here : ")
    if user_inp == "start":
        if start:
            print("Car has started")
        else:
            print("Car has already started")
        started = True
    elif user_inp == "stop":
        if user_inp != start:
            print("Car has stopped")
        else:
            print("Car has not started")
        start = False
    elif user_inp == "help":
        print(hint_str)
    elif user_inp == "quit":
        break
    else:
        print("It seems there is a problem!!")

#Question 2 Sum of odd and even numbers from 1 to 20 and greater from them
a = 1
osum= 0
esum = 0
while a != 21:
    if a % 2 == 0:
        print(f"{a} is even")
        esum = esum + a
    else:
        print(f"{a} is odd")
    osum = osum + a
    a = a + 1

if esum > osum:
    print("Even sum is greater ")
elif osum > esum:
    print("Sum of odd is greater")
else:
    print("Both might be equal or error")

#Question 3 Demonstrate your phones pin checker

pin = 1234
userinp = 0
while userinp != pin:
    userinp = int(input("Enter the pin : "))
    if len(str(userinp)) != 4:
        print("The pin should be of 4 digits only ")
        continue
else:
    print("Welcome")

#Question 4 fizz buzz

i = 50
for x in range(1, i + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

