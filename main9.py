# Question 1  Increase the level of CAR Game program and make the changes explained in class.
help = '''
start : Start the car
stop : Stop the car
help : Help menu
quit : Quit the game
'''
start = False
print(help)
while True:
    command = input("Command: ")
    if command == "start":
        if not start:
            print("Car has been started")
        else:
            print("Car has already started")
        start = True
    elif command == "stop":
        if start:
            print("Car has been stopped")
        else:
            print("Car has not started")
        start = False
    elif command == "help":
        print(help)
    elif command == "quit":
        if start:
            print("""The car is running
Stop the car first to proceed...""")
            continue
        break
    else:
        print("Error")

# Question 2 Create a lucky draw program giving using three chances and the following prizes. Rs 1000, 500, 100, Try again
from random import randint
from time import sleep
chances = 3
print("Welcome to the game")
for a in range(3):
    print(f"{3 - a} left, press enter to use your chance")
    input()
    number = randint(1, 100)
    print("You got : ")
    if number > 90:
        print("You have won Rs 1000! Congratulations!!")
    elif number > 75:
        print("You have won Rs 500!")
    elif number > 50:
        print("You have won Rs 100!")
    else:
        print("Try again..")
print("No chances remaining..")

# Question 3 Create a magic eight ball program that answers either of the following, Yes, No, I am not sure
from random import choices
user_choice = ["Yes", "No", "I am not sure"]
print("Type 'exit' to quit the program")
while True:
    user_inp = input(": ")
    if user_inp == "exit":
        break
    print(choices(user_choice)[0])