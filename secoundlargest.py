nums=list(map(int,input("enter").split()))
largest=nums[0]
length=len(nums)
for i in range(length):
    if (nums[i]>largest[i]):
      largest=nums[i]
      
print(largest)