#1
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
newlist = [list1[i] + list2[i] for i in range(len(list1))]
print(newlist)

#2
qlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
mulofthree = [num for num in qlist if num % 3 == 0]
sum = sum(mulofthree)
print(sum)