#x = 2
#y = 3
#z = 5
#sum = x+y+z
#print(f'The sum is {sum}')

#l = 2
#b = 3
#h = 6
#vol = l*b*h
#print(f'The volume is {vol}')

#r =10
#area = 3.14*r*r
#print(f'The area is {area}')

#p = 1000
#r = 10
#t = 2
#si = (p*t*r)/100
#print(f'The SI is {si}')

#x = 1
#y = 5
#diff = abs(x-y)---discards the negative sign
#print(f'The DIfference is {diff}')

#le = int(input("Enter any number: "))
#br = int(input("Enter any number: "))
#peri = 2*(le+br)
#print(f'The perimeter is {peri}')

#do as stated
#import math as m
#p = 3500
#r = 3.15
#t = 2.5
#si = (p*t*r)/100
#roundvalue = round(si)----decimel is rounded
#ceilvalue = m.ceil(si)----gives largest integer not greater than the given integer
#floorvalue = m.floor(si)----largest integer not greater than given integer
#print(f'The Round value is {roundvalue}')
#print(f'The Ceiling value is {ceilvalue}')
#print(f'The Floor Vlaue is {floorvalue}')

#do as stated
#user_inp = "python IS powerful"
#print (len(user_inp))---finds length of string
#print(user_inp.lower())---lowers every letter in string
#print(user_inp.upper())---capitalizes every letter in string
#print(user_inp.capitalize())---capitalizes the first letter in the string
#print(user_inp.title())---capitalizes first lettter of every word in string
#new_var = "python IS easy"
#print(user_inp.replace(user_inp,new_var))----replaces the old string with new string
#x = user_inp.find('I')---finds the first occurence in string
#y = user_inp.find('o')---finds the first occurence in string
#print("The first occurence of I in string is " + str(x))
#print("The first occurence of o in string is " + str(y))

#find the given word in the sample text
#sample_txt = '''Python is an interpreted,high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a 'batteries included'language due to its comprehensive standard library.Python was created in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.'''
#user_inp = input("Enter the word to find: ")
#if (user_inp in sample_txt):---finds the user inputed word in the given text
#    index = sample_txt.find(user_inp)---finds the index of the given word
#    print(f"{user_inp} is on index {index}!")---prints the index of the given word
#else:
#    print(f"{user_inp} not found !")---prints if the word is not found in the text

#wap to check if the user is eligible to vote or not, if not how many years left
#user_age = input("Enter the age = ")
#rem_age = 18 - int(user_age)
#if int(user_age) >=18:
#    print("You are eligible to vote")
#else:
#    print("You are not eligible to vote,vote after",(rem_age), "years kid.")

#do as given
#user_inp = input("Enter any word that is atleast 3 letters long = ")
#count = (len(user_inp))
#if count > 2:---to check if the word count exceeds 2
#    if user_inp[-3:] == 'ing':---to check if the last 3 words are 'ing' or not
#      final_word = user_inp[: count-3]---to remove the last three words 'ing' if there is
#      print(final_word)
#    else:
#      user_inp+='ly'---if no 'ing' in word, add 'ly' instead
#      print(user_inp)

#do as stated
#string = input("Enter the string : ")
#w1 = string.find('not')
#w2 = string.find('poor')
#if w2 > w1 & w1 > 0 & w2 > 0:
#    string = string.replace(string[w1:(w2 +4)], 'good')
#    print(string)
#else:
#    print(string)
#aayena

#do as instructed
#W1 = input("Enter the First word: ")
#W2 = input("Enter the Second word: ")
#W3 = input("Enter the Third word: ")
#len1 = len(W1)
#len2 = len(W2)
#len3 = len(W3)
#sr_wrd = 0
#l_wrd = 0
#if (len1 > len2) & (len1 > len3):
#    print("The longest word is", (W1))
#elif (len2 > len1) & (len2 > len3):
#    print("The longest word is", (W2))
#elif (len3 > len1 ) & (len3 > len2):
#    print("The longest word is", (W3))
#else:
#    print("All the words are equal in size")
#if len1 < len2 and len1 < len3:
#        print("The shortest word is", (W1))
#elif len2 < len1 and len2 < len3:
#        print("The shortest word is", (W2))
#elif len3 < len2 and len3 < len1:
#        print("The shortest word is", (W3))
#else:
#    print("All the words are equal in size")
#if len1<len3 & len1<len2:
#    sr_wrd = len1
#elif len2<len3 & len2<len1:
#    sr_wrd = len2
#elif len3<len1 & len3<len2:
#    sr_wrd = len3
#else:
#    print("error")
#if len1>len3 & len1>len2:
#    l_wrd = len1
#elif len2>len3 & len2>len1:
#    l_wrd = len2
#elif len3>len1 & len3>len2:
#    l_wrd = len3
#else:
#    print("error")
#diff = l_wrd - sr_wrd
#print("Difference between the shortest and the longest word = " + diff)
#difference niklana aayena

# simple password checker
#usr = "Balram"
#psw = "dalbhattrai"
#usrname = input("Enter your username : ")
#passwrd = input("Enter your password : ")
#if usrname == usr and passwrd == psw:
#    print("You have sucessfully logged in, Enjoy!")
#else:
#    print("Tapaile Khojeko Account bhetiyena, Kripaya Puna Prayas Garnu Hola...")

# either vowel or consonant
#user_wrd = input("Enter the string: ")
#middle_index = round(len(user_wrd) / 2) - 1
#middle_letter = user_wrd[middle_index]
#if (middle_letter == 'A' or middle_letter == 'a' or middle_letter == 'E' or middle_letter == 'e' or middle_letter == 'I'
#        or middle_letter == 'i' or middle_letter == 'O' or middle_letter == 'o' or middle_letter == 'U' or middle_letter == 'u'):
#    print(middle_letter, "is a Vowel")
#else:
#    print(middle_letter, "is a Consonant")

# greatest number
#num1 = input("Enter a number: ")
#num2 = input("Enter a number: ")
#num3 = input("Enter a number: ")
#if num1 > num2 and num1 > num3:
#    print(num1, "is greater")
#elif num2 > num1 and num2 > num3:
#    print(num2, "is Greater")
#else:
#    print(num3, "Is greater")

# converting weight
#usr_input = input("Enter the Weight : ")
#unit = input("Enter the unit (kg/pound) : ")
#convpound = int(usr_input) * 2.2
#convkg = int(usr_input) / 2.2
#if unit == "kg" or unit == "KG":
#    print("The result in pound is : ", convpound)
#elif unit == "pound" or unit == "POUND":
#    print("The result in Kg is : ", convkg)
#else:
#    print("Invalid! Input")

# limited words
#usr_input = input("Enter you name ")
#usr_len = len(usr_input)
#if usr_len <= 5:
#    print("Your name is too short, insert a longer name")
#elif (usr_len >= 5) and (usr_len <= 20):
#    print("Welcome to the club, ", usr_input)
#elif usr_len >= 20:
#    print("Your name is too large, insert a smaller name")
#else:
#    print("Invalid!")

# marks
#mark1 = int(input("Enter marks obtained: "))
#mark2 = int(input("Enter marks obtained: "))
#mark3 = int(input("Enter marks obtained: "))
#if mark1 > mark2 and mark1 > mark3:
#    print(mark1, " is highest marks")
#elif mark2 > mark1 and mark2 > mark3:
#    print(mark2, " is highest marks")
#else:
#    print(mark3, " is highest marks")
#totalmrks = mark1 + mark2 + mark3
#avg = totalmrks / 3
#per = (totalmrks / 300) * 100
#print("The percentage secured is ", per)
#if avg < 50:
#    print("Grade: E")
#elif avg >= 50 and avg < 60:
#    print("Grade: D")
#elif avg >= 60 and avg < 70:
#    print("Grade: C")
#elif avg >= 70 and avg < 80:
#    print("Grade: B")
#elif avg >= 80 and avg < 90:
#    print("Grade: A")
#elif avg >= 90 and avg <= 100:
#    print("Grade: A+")
#else:
#    print("Invalid Input!")

#usr_inp = int(input("Enter any number: "))
#if usr_inp % 2 == 0:
#    print('The given number is even')
#else:
#    print('The given number is odd')

#a = int(input("Enter a: "))
#for i in range(1, a):
#    if (i % 3) == 0 and (i % 5) == 0:
#        print('FizzBuzz')
#    elif (i % 3) == 0:
#        print('Fizz')
#    elif (i % 5) == 0:
#        print('Buzz')
#    else:
#        print(i)

#usr_ut = int(input("Enter the power consumption in unit: "))
#if (usr_ut > 0) and (usr_ut < 100):
#    print("No recharge needed!!")
#elif (usr_ut >= 100) and (usr_ut < 200):
#    total = usr_ut * 5
#    print("Your total amount is ", total)
#elif usr_ut >= 200:
#    total = usr_ut * 10
#    print("Your total amount is ",total)
#else:
#    print("Error...Try Again")

#x = input("Enter any number ")
#last_inp = x[-1]
#if int(last_inp) % 3 == 0:
#    print("The number is divisible by 3 ")
#else:
#    print("The number is not divisible by 3 ")

#one = int(input("Enter the first side "))
#two = int(input("Enter the second side "))
#three = int(input("Enter the third side "))
#if one == two == three:
#    print(" It is Equilateral Triangle")
#elif one == two or two == three or one == three:
#    print("It is an Isosceles Triangle")
#else:
#    print("It is a Scaler Triangle")

# extra
#time = int(input("Enter the time : "))
#if time == 12:
#    print("Good afternoon")
#elif (time >0) and (time <= 10):
#    print("Good morning")
#elif (time >= 11) and (time < 18):
#    print("Good day")
#elif (time >= 18) and (time < 20):
#    print("Good evening")
#elif (time >= 20) and (time <= 24):
#    print("Good night")
#else:
#    print("Error")

#from 0 to 6
#for z in range(6):---defines numbers from 0 to 6 to z
#    if (z == 3 or z == 6):---removes 3 and 6 from the range from 0 to 6 in z
#        continue
#    print(z)

#vowels and consonant
#txt = " I am Safal and I like to play Online Games "
#vowel = 0
#consonant = 0
#for k in txt:---defines the necessary terms in txt
#    if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
#        vowel = vowel + 1---for each vowels, adds the numbers together
#    else:
#        consonant = consonant + 1
#print(vowel)
#print(consonant)

# upper case and lower case
#text = " I am Safal and I like to play Online Games "
#capital_count = 0
#small_count = 0
#for i in text:
#    if i.upper():
#        capital_count = capital_count + 1
#    elif i.lower():
#        small_count = small_count + 1

# reverse string
#str = input("Enter any word: ")
#print ("The original string  is: ",str)
#reverse_String = ""
#count = len(str)
#while count > 0:
#    reverse_String += str[count - 1]
#    count = count - 1
#print ("The reversed string is: ",reverse_String)

#inpnum = int(input("Enter any number: "))
#def odd():
#    print("IT IS ODD!!")
#def even():
#    print("IT IS EVEN!!")
#if inpnum % 2 == 0:
#    even()
#else:
#   odd()

#user_inp = int(input("Enter the value in Kilometer: "))
#def convert():
#    mile = user_inp / 1.609
#    print("The conversion of KM to mile is ", mile)
#convert()

#for x in range(1, 6):
#  for y in range(1, x + 1):
#    print(y, end="")---end makes the print method ends with a newline.
#  print('')

#for x in range(1, 6):
#  for y in range(x):
#    print(x, end="")
#  print('')

# calculate the cost of all the items in a shopping cart
#total = 0
#cart = [69,11,22,33,44,55,66,77,88,99]
#for x in cart:
#   total = x + total
#print(total)

#palindrome or not
#text = input("Enter your text: ")
#reverse = ""
#for char in text:
#    reverse = char + reverse
#if (text == reverse):
#    print("It is palindrome!")
#else:
#    print("It is not palindrome...")

####
#for x in range (2):
#   for y in range (2):
#        print(str(x)+"-"+str(y))

####
#adj = ["red","big","tasty"]
#fruits = ["apple","banana","cherry"]
#for x in adj:
#    for y in fruits:
#        print(x,y)

####
#names = ["RAM","SHYAM","GOPAL"]
#for n in names:
#    x = 0
#    while (x < 5):
#        print(n, end=" ")
#        x = x + 1
#    print()

#function
#def greet():
#    print("Hello")
#def sum(x,y):
#    return x+y
#x = int(input("Enter first number:"))
#y = int(input("Enter second number:"))
#print("Sum of the given two numbers is: ", sum(x,y))
#greet()

#assignment
#multiplication table
#for x in range(1,11):
#    for y in range (13):
#        print(f'{x} * {y} = {x*y}')
#    print("--------------------------------------")

#number is palindrome or not
#number=int(input("Enter any number :"))
#temp=number
#reverse_num=0
#while(number>0):
#    digit=number%10
#    reverse_num=reverse_num*10+digit
#    number=number//10
#if(temp==reverse_num):
#    print("The number is palindrome!")
#else:
#    print("Not a palindrome!")

#pattern
#for i in range(0, 5):
#   for j in range(0, i + 1):
#        print("*", end=' ')
#   print("")


#WAP to print 13 X 5 rectangle using "=" python
#for i in range(6):
#    for j in range(14):
#        print('=', end='')
#    print()

#sum of two numbers using function
#without params
#def sum():
#    sum = 4 + 5
#    print(sum)
#sum()

#with return and params
#def sum(x,y):
#    return x+y
#x = int(input("Enter first number:"))
#y = int(input("Enter second number:"))
#print("Sum of the given two numbers is: ", sum(x,y))

#final string
#s1 = input("Enter a string : ")
#s2 = input("Enter another string : ")
#first = s1[0] + s1[(len(s1) - 1) // 2] + s1[len(s1) - 1]
#second = s2[0] + s2[(len(s1) - 1) // 2] + s2[len(s1) - 1]
#final_str = first + second
#print(f"Final string is {final_str}")

#from 1 to 10
#count = 1
#while count <= 10:
#    print(count)
#    count = count + 1

# even numbers only from 1 to 10
#count = 1
#while count <= 10:
#    count = count + 1
#    if count % 2 == 0:
#      print(count)
#else:
#   print("Closed")

# infinite try guessing game
#num =int(input(" Enter a number "))
#while num != 69420:
#    num = int(input(" Enter a number "))
#else:
#    print("You've won!!!!!")

#5 try guessing game
#num1 = 9
#chance = 5
#guess = int(input("Enter a number "))
#while guess != num1:
#    print(f'you have {chance} left')
#    chance = chance - 1
#    if chance == 0:
#        print("Wrong, pls try again...")
#        break
#    guess = int(input("Enter a number : "))
#else:
#   print("You guessed it bro!!!")

#guessing game with hints and 5 tries
#num2 = 10
#chance = 5
#guess = int(input("Enter a number between 1 to 20 "))
#while guess != num2:
#    chance = chance - 1
#    if chance == 0:
#        print("Wrong")
#        break
#    if guess > number:
#        print("The number is smaller")
#    elif guess < number:
#        print("The number is bigger")
#    guess = int(input("Enter a number between 1 to 20 "))
#else:
#    print("You guessed it right")

# to print the following text in format given
#txt1 = '''Hello Prayush,
#
#    It was nice seeing you. Call me when you get here. I hope you are well.
#
#Regards, Ayush'''
#print(txt1)

# to find radius from given area
#area = 150
#rad = (area / 3.14) * 0.5
#print(rad)

# occurrence of a string
#txt = '''
#Hola amigos, I am in america. I am flying right now.
#Drank alchohol last j=night still having a hangover. Anyway good bye and thank you.
#'''
#usrtxt = input("Enter any string : ")
#if txt.find(usrtxt) != -1:
#    occur = txt.find(usrtxt)
#    print(f"Your searched word is at {occur}")
#else:
#    print("String not found!")

# new string in third person
# give up..........

#simple calculator
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#userinp = input("Enter your desired calcalution: ")
#if userinp == "add":
#    calc = int(num1) + int(num2)
#    print(calc)
#elif userinp == "sub":
#    calc = int(num1) - int(num2)
#    print(calc)
#elif userinp == "mul":
#    calc = int(num1) * int(num2)
#    print(calc)
#elif userinp == "div":
#    calc = int(num1) / int(num2)
#    print(calc)
#else:
#    print("error")

# guessing game
#cor_ans = '24'
#usr_inp = input("Enter any number : ")
#while usr_inp != cor_ans:
#    print("You guessed it wrong! ")
#    usr_inp = input("Enter any number ")
#    if usr_inp == 24 or usr_inp == 'stop':
#        break
#else:
#    print(f"{cor_ans} is the correct answer")

#Build a car game
#hint_str = '''
#start - Start the car
#stop - Stop the car
#help - Help request
#quit - Quit the game
#'''
#start = False
#while True:
#    user_inp = input("Enter here : ")
#    if user_inp == "start":
#        if start:
#            print("Car has started")
#        else:
#            print("Car has already started")
#        started = True
#    elif user_inp == "stop":
#        if user_inp != start:
#            print("Car has stopped")
#        else:
#            print("Car has not started")
#        start = False
#    elif user_inp == "help":
#        print(hint_str)
#   elif user_inp == "quit":
#        break
#    else:
#        print("It seems there is a problem!!")

#Sum of odd and even numbers from 1 to 20 and greater from them
#a = 1
#osum= 0
#esum = 0
#while a != 21:
#    if a % 2 == 0:
#        print(f"{a} is even")
#        esum = esum + a
#    else:
#        print(f"{a} is odd")
#    osum = osum + a
#    a = a + 1
#if esum > osum:
#    print("Even sum is greater ")
#elif osum > esum:
#    print("Sum of odd is greater")
#else:
#    print("Both might be equal or error")

#Demonstrate your phones pin checker
#pin = 1234
#userinp = 0
#while userinp != pin:
#    userinp = int(input("Enter the pin : "))
#    if len(str(userinp)) != 4:
#        print("The pin should be of 4 digits only ")
#        continue
#else:
#    print("Welcome")

# Increase the level of CAR Game program and make the changes explained in class.
# if car has not started and user enters stop than tell the user the car has not started
# if the has already started and the user enters start, tell the user the car ahs already started
#if the user wants to quit and the car has not been stopped, warn the user to stop the car first before quiting
#provide help menu at the beginning
#help = '''
#start : Start the car
#stop : Stop the car
#help : Help menu
#quit : Quit the game
#'''
#start = False
#print(help)
#while True:
#    command = input("Command: ")
#    if command == "start":
#        if not start:
#            print("Car has been started")
#        else:
#            print("Car has already started")
#        start = True
#   elif command == "stop":
#       if start:
#           print("Car has been stopped")
#       else:
#           print("Car has not started")
#       start = False
#   elif command == "help":
#       print(help)
#   elif command == "quit":
#       if start:
#           print("""The car is running
#Stop the car first to proceed...""")
#           continue
#       break
#   else:
#       print("Error")

#Create a lucky draw program giving using three chances and the following prizes. Rs 1000, 500, 100, Try again
#from random import randint
#from time import sleep
#chances = 3
#print("Welcome to the game")
#for a in range(3):
#    print(f"{3 - a} left, press enter to use your chance")
#    input()
#    number = randint(1, 100)
#    print("You got : ")
#    if number > 90:
#        print("You have won Rs 1000! Congratulations!!")
#    elif number > 75:
#        print("You have won Rs 500!")
#    elif number > 50:
#        print("You have won Rs 100!")
#    else:
#        print("Try again..")
#print("No chances remaining..")

#Create a magic eight ball program that answers either of the following, Yes, No, I am not sure
#from random import choices
#user_choice = ["Yes", "No", "I am not sure"]
#print("Type 'exit' to quit the program")
#while True:
#    user_inp = input(": ")
#    if user_inp == "exit":
#        break
#    print(choices(user_choice)[0])