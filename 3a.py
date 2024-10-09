S=input("enter a sentence")
w=0
d=0
u=0
l=0
r=S.split()
w=len(r)
for i in S:
    if i.isdigit():
        d=d+1
    elif i.isupper():
        u=u+1
    else:
        l=l+1
print("Number of words:",w)
print("Number of digit:",d)
print("Number of uppercases:",u)
print("Number of lowercases:",l)

