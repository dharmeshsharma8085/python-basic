i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

    print("end of loop")



# 2nd example



nums=(1,4,9,16,25,36,49,64,81,100,)
x=int(input("enter number"))
i=0 #intilization
while i<len(nums):
    if(nums[i]==x):
        print("element found",i)
        break
    else:
        print("finding.....")
    i+=1
print("end of loop")