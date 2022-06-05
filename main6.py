#1 to print the following text in format given
txt1 = '''Hello Prayush, 

    It was nice seeing you. Call me when you get here. I hope you are well. 
          
Regards, Ayush'''
print (txt1)

#2 to find radius from given area
area = 150
rad = (area/3.14)*0.5
print (rad)

#3 occurrence of a string
txt = '''
Hola amigos, I am in america. I am flying right now. 
Drank alchohol last j=night still having a hangover. Anyway good bye and thank you.
'''
usrtxt = input("Enter any string : ")
if txt.find(usrtxt) != -1:
    occur = txt.find(usrtxt)
    print(f"Your searched word is at {occur}")
else:
    print("String not found!")

#4 discarding the negative sign while differentiating
inp1 = int(input("Enter any number: "))
inp2 = int(input("Enter another number: "))
diff = abs(inp1-inp2)
print(diff)

#5 new string in third person
string = input("Enter a string : ")
if string[-3] == "boy":
    string = string.replace("I am",)

#6 number is even or odd
nm = int(input("Enter a number: "))
if nm%2==0:
    print("The number you have entered is even.")
else:
    print("It seems the number you have entered is odd.")

#7 simple calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
userinp = input("Enter your desired calcalution: ")
if userinp == "add":
    calc = int(num1)+int(num2)
    print(calc)
elif userinp == "sub":
    calc = int(num1)-int(num2)
    print(calc)
elif userinp == "mul":
    calc = int(num1)*int(num2)
    print(calc)
elif userinp == "div":
    calc = int(num1)/int(num2)
    print(calc)
else:
    print("error")

#8 guessing game
cor_ans = '24'
usr_inp = input("Enter any number : ")
while usr_inp != cor_ans:
    print("You guessed it wrong! ")
    usr_inp = input("Enter any number ")
    if usr_inp == 24 or usr_inp == 'stop':
        break
else:
    print(f"{cor_ans} is the correct answer")


