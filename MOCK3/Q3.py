nums=[10,5,18,12,7,20,15]
idx=0
max=nums[idx]
second_largest=nums[idx+1]
while idx<len(nums):
    if(nums[idx]>max):
        second_largest=max
        max=nums[idx]
     
    elif(nums[idx]<max): 
        second_largest=nums[idx]
          
    idx+=1
    
print("largest numbe is",max)
print("second largest number is",second_largest)