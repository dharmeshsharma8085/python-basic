nums=[2,5,8,12,15]
idx=0
total=0
for idx in range(idx,len(nums),1):
    total=nums[idx]+total
    idx+=1

print("Total of list is ",total)

avg=total/5
print("Average of list is",avg)