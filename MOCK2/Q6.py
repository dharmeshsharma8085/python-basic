# nums=[2,5,8,11,14]
# idx=0
# new_list=[]
# while idx<len(nums):
#     even=nums[idx]%2==0
#     new_list.append(even)
#     idx+=1

# print(new_list)

nums=[2,5,8,11,14]
idx=0
new_list=[]
while idx<len(nums):
    if(nums[idx]%2==0):
        even=nums[idx]
        new_list.append(even)

    idx+=1


print(new_list)