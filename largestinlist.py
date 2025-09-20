list1=list(map(int,input("enter").split()))
largest=list1[0]
length=len(list)
for i in range(length):
    if (list1[i]>largest[i]):
      largest=list1[i]
      
print(largest)