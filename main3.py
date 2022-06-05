# simple passwrod checker
usr = "Balram"
psw = "dalbhattarkari"

usrname = input("Enter your username : ")
passwrd = input("Enter your password : ")

if usrname == usr and passwrd == psw:
    print("You have sucessfully logged in, Enjoy!")
else:
    print("Tapaile Khojeko Account bhetiyena, Kripaya Puna Prayas Garnu Hola...")

#either vowel or consonant
user_wrd = input("Enter the string: ")
middle_index = round(len(user_wrd)/2)-1
middle_letter = user_wrd[middle_index]

if(middle_letter=='A' or middle_letter=='a' or middle_letter=='E' or middle_letter =='e' or middle_letter=='I'
 or middle_letter=='i' or middle_letter=='O' or middle_letter=='o' or middle_letter=='U' or middle_letter=='u'):
    print(middle_letter, "is a Vowel")
else:
    print(middle_letter, "is a Consonant")
    
# greatest number

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")
if num1>num2 and num1>num3:
    print(num1, "is greater")
elif num2>num1 and num2>num3:
    print(num2, "is Greater")
else:
    print(num3,"Is greater")

# converting weight
usr_input = input("Enter the Weight : ")
unit = input("Enter the unit (kg/pound) : ")
convpound = int(usr_input) * 2.2
convkg = int(usr_input) / 2.2
if unit == "kg" or unit == "KG":
    print("The result in pound is : ", convpound)
elif unit == "pound" or unit == "POUND":
    print("The result in Kg is : ", convkg)
else:
    print("Invalid! Input")

# limited words
usr_input = input("Enter you name ")
usr_len = len(usr_input)
if usr_len <= 5:
    print("Your name is too short, insert a longer name")
elif (usr_len >= 5) and (usr_len <= 20):
    print("Welcome to the club, ", usr_input)
elif usr_len >= 20:
    print("Your name is too large, insert a smaller name")
else:
    print("Invalid!")

# marks
mark1 = int(input("Enter marks obtained: "))
mark2 = int(input("Enter marks obtained: "))
mark3 = int(input("Enter marks obtained: "))

if mark1>mark2 and mark1>mark3:
    print(mark1, " is highest marks")
elif mark2>mark1 and mark2>mark3:
    print(mark2, " is highest marks")
else:
    print(mark3, " is highest marks")

totalmrks = mark1+mark2+mark3
avg = totalmrks/3
per = (totalmrks/300)*100
print("The percentage secured is ", per)

if avg<50:
    print("Grade: E")
elif avg>=50 and avg<60:
    print("Grade: D")
elif avg>=60 and avg<70:
    print("Grade: C")
elif avg>=70 and avg<80:
    print("Grade: B")
elif avg>=80 and avg<90:
    print("Grade: A")
elif avg>=90 and avg<=100:
    print("Grade: A+")
else:
    print("Invalid Input!")

