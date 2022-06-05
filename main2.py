# Question 1

user_age = input("Enter the age = ")
rem_age = 18 - int(user_age)
if int(user_age) >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote,vote after",(rem_age), "years kid.")


#Question 2

user_inp = input("Enter any word that is atleast 3 letters long = ")
count = (len(user_inp))
if count > 2:
    if user_inp[-3:] == 'ing':
      final_word = user_inp[: count-3]
      print(final_word)
    else:
      user_inp+='ly'
      print(user_inp)

#Question 3

string = input("Enter the string : ")
w1 = string.find('not')
w2 = string.find('poor')
if w2 > w1 & w1 > 0 & w1 > 0:
    string = string.replace(string[w1:(w2 +4)], 'good')
    print(string)
else:
    print(string)

#result needed is not satisfied..


#Question 4

W1 = input("Enter the first word ")
W2 = input("Enter the second word ")
W3 = input("Enter the third word ")
len1 = len(W1)
len2 = len(W2)
len3 = len(W3)
if (W1 > W2) & (W1 > W3):
    print("The longest word is", (W1))
elif (W2 > W1) & (W2 > W3):
    print("The longest word is", (W2))
elif (W3 > W1 ) & (W3 > W2):
    print("The shortest word is", (W3))
else:
    print("All the words are equal in size")

if W1 <= W2 and W1 <= W3:
        print("The longest word is", (W1))
elif W2 <= W1 and W2 <= W3:
        print("The longest word is", (W2))
elif W3 <= W2 and W3 <= W1:
        print("The longest word is", (W3))
else:
    print("All the words are equal in size")

# confusion in findind difference between the shortest and the longest word