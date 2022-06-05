#turn element of list into a square
num = [10, 20, 30, 40]
sqnum = [num ** 2 for num in num]
print(sqnum)

#yes
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)

#yes2
listt1 = [5, 10, 20, 20, 50, 60]
pos_list = []
for i in range(len(listt1)):
    if listt1[i] == 20:
        pos_list.append(i)
x = pos_list[:1]
listt1[x[0]]=200
print(listt1)

n = int(input("enter any number: "))
try:
    res = 5/n
    print(res)
except exception as e:
    print("error" + e)
print("end")