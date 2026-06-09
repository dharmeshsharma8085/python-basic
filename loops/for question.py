# list=[1,4,9,16,25,36,49,64,81,100]
# for nums in list:
#     print(nums)

tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number"))
idx = 0
for a in tup:
    if(a==x):
        print("element found",idx)
        break
    idx +=1
   