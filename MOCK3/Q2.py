nums=[11,4,19,7,2,25,8]
idx=0
max=nums[idx]
while idx<len(nums):
    if(nums[idx]>max):
        max=nums[idx]
        
    idx+=1
    
print("maximun number is ",max)