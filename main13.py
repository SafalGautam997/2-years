#1
list1 = [1,1,4,4,2,5,6,7,88,8,8]
list2 = []
for val in list1:
    if val not in list2:
        list2.append(val)
print(f'THe new list is : {list2}')

#2
# i)
def num(a,b,c):
    print(a,b,c)
    return
num(1,2,3)

# ii)
def f(x, *y):
    print(x)
    for z in y:
        print(z)

# iii)
f("a","b","c")
def sum(o,t):
    s = o + t
    return s
num1= int(input("enter a number: "))
num2= int(input("enter a number: "))
print(sum(num1,num2))

#3
lst= [10,20,30,40,50,5,25]
lst.insert(2,35)
lst.insert(1,15)
print(lst)
total=0
for j in range(0,len(lst)):
    total = total + lst[j]
print("the total sum is",total)
lst.pop()
print(lst)
lst.remove(20)
print(lst)
tot=0
newli=lst[-3:]
for h in range(0,len(newli)):
    tot = tot + lst[h]
print("the total sum is",tot)
