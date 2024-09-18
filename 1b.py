num = int(input("Enter a Number"))
val=str(num)
rev = val[::-1]
if(val==rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
for i in range(10):
    if(val.count(str(i))>0):
        print(str(i), "appears", val.count(str(i))," times")
