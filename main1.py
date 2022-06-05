#demo

entered_name = "SHYAM"

if entered_name.lower() == "ram":
    print("K Cha")
else:
    print("Ja uta")

# 1

age = int(input("Enter your age : "))

if age >= 18:
    print("Allowed to vote")
else:
    print("Not allowed to vote, Please Go Away...")

# 2

stud_age = int(input("Enter your age : "))
stud_section = input("Enter your section : ")
stud_section = stud_section.lower()

if stud_age > 18 and stud_section == "saipal":
    print("Allowed to vote")
else:
    print("Go Left there is a candy store, Buy some chocolate kid...")

# 3

user = "boss"
psw = "bosslol"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == psw:
    print("You have sucessfully logged in, Enjoy!")
else:
    print("Kripaya Puna Prayas Garnu Hola...")


# Extra

s1 = input("Enter a string : ")
s2 = input("Enter another string : ")

first = s1[0] + s1[(len(s1) - 1) // 2] + s1[len(s1) - 1]
second = s2[0] + s2[(len(s1) - 1) // 2] + s2[len(s1) - 1]

final_str = first + second

print(f"Final string is {final_str}")