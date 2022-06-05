# Question 1
inpnum = int(input("Enter any number: "))
def odd():
    print("IT IS ODD!!")
def even():
    print("IT IS EVEN!!")
if inpnum % 2 == 0:
    even()
else:
   odd()

# Question 2
user_inp = int(input("Enter the value in Kilometer: "))
def convert():
    mile = user_inp / 1.609
    print("The conversion of KM to mile is ", mile)
convert()

#Question 3
for x in range(1, 6):
  for y in range(1, x + 1):
    print(y, end="")
  print('')

# Question 4
for x in range(1, 6):
  for y in range(x):
    print(x, end="")
  print('')