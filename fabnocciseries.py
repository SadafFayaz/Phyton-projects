number=int(input("numer upto which you have to calculate"))
first=0
second=1
print(first)
print(" ",second)
for i in range(1,number+1):
    
    next=first+second
    first=second
    second=next
    print(" ",next)