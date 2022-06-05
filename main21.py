import re
text="The Hands of Death could not defeat me, The Sisters of Fate could not hold me, And you will not see the end of this day, I will Have my Revenge!"
res=re.findall("could", text)
ress=re.search("could", text)
print(res)
print(ress)
print(ress.span())
ab=re.split("\s", text, -1)
ad=re.sub("\s","-", text)
print(ab)
print(ad)
text1="Hello my name is slim shady"
#re_n='[a-j]|[A-S]'
#re_n="\w"
re_n="H.*llo"
ko=re.findall(re_n, text1)
print(ko)
bob= input("enter: ")
rob='ab+\w'
ok=re.findall(rob, bob)
print(ok)

