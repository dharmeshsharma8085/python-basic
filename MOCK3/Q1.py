nums=[5,8,3,12,7,20,1]
idx=0
total=0
while idx<len(nums):
    if(nums[idx]%2==0):
        total=total+nums[idx]
        
    idx+=1
print(total)