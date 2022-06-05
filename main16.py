#magic 8 ball game
import random
outcome=["Yes", "No", "Maybe", "It is certain", "Certainly not"]
n = random.randint(0,len(outcome))
input("Enter a question: ")
print(outcome[n])

x = [10, 20 ,30]
y = x
x.append(5)
print(x)
print(y)

x = [10, 20 ,30 ,40]
y = x
print(y)
print(id(x) == id(y))

import copy
y = copy.copy(x)

my_dict={
    "Apurva":"29th Dec",
    "Shubham":"7th Nove",
    "Ishu":"5th Dec",
    "Prayush":"1st July"
}
r=my_dict["Ishu"]
print(r)

#SAFAL GAUTAM