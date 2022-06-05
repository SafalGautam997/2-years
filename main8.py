# extra
time = int(input("Enter the time : "))
if time == 12:
    print("Good afternoon")
elif (time >0) and (time <= 10):
    print("Good morning")
elif (time >= 11) and (time < 18):
    print("Good day")
elif (time >= 18) and (time < 20):
    print("Good evening")
elif (time >= 20) and (time <= 24):
    print("Good night")
else:
    print("Error")


# 1 from 0 to 6
for z in range(6):
    if (z == 3 or z == 6):
        continue
    print(z)


#2 vowels and consonant
txt = " I am Safal and I like to play Online Games "
vowel = 0
consonant = 0
for k in txt:
    if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
        vowel = vowel + 1
    else:
        consonant = consonant + 1
print(vowel)
print(consonant)

#3 upper case and lower case
text = " I am Safal and I like to play Online Games "
capital_count = 0
small_count = 0
for i in text:
    if i.upper():
        capital_count = capital_count + 1
    elif i.lower():
        small_count = small_count + 1


# 4 reverse string
str = input("Enter any word : ")
reversestr = ""
for i in range(len(str) - 1, -1, -1):
    reverse_str = reversestr + str[i]
print(reverse_str)
#the final answer did not come