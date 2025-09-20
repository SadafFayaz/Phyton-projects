nums=list(map(int,input("enter").split()))
smallest=nums[0]
sortlist=[]
length=len(nums)
for i in range(length):
    if (smallest>nums[i]):
      smallest = nums[i]
      
for j in nums:
         sortlist.append(smallest)
print(sortlist)
       
           
    
      