# Question 1

count = 1
while count <= 10:
    print(count)
    count = count + 1

# Question 2

count = 1
while count <= 10:
    count = count + 1
    if count % 2 == 0:
      print(count)
else:
    print("Closed")

# Question 3

num =int(input(" Enter a number "))
while num != 69420:
    num = int(input(" Enter a number "))
else:
    print("You've won!!!!!")

# Question 4

num1 = 9
chance = 5
guess = int(input("Enter a number "))
while guess != num1:
    print(f'you have {chance} left')
    chance = chance - 1
    if chance == 0:
        print("Wrong, pls try again...")
        break
    guess = int(input("Enter a number : "))
else:
    print("You guessed it bro!!1")

# Question 5

num2 = 10
chance = 5
guess = int(input("Enter a number between 1 to 20 "))
while guess != num2:
    chance = chance - 1
    if chance == 0:
        print("Wrong")
        break
    if guess > number:
        print("The number is smaller")
    elif guess < number:
        print("The number is bigger")
    guess = int(input("Enter a number between 1 to 20 "))
else:
    print("You guessed it right")