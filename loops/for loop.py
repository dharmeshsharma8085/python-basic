#sequencial traversal

list=[1,2,3,4,5,6,7,8,9]
for nums in list:
    print(nums)

veg=["potato","tomato","lady finger","caulyfloewr","chilly"]
for eat in veg:
    print(eat)

# work on tuple also

tup= (1,2,3,4,5,6,7,8,9,)
for nums in tup:
    print(nums)

str="Dharmesh sharma"
for a in str:
    print(a)
else:
    print("End")

# why we use else statement it use in break 

str="Dharmesh shamra is hero"
for a in str:
    if(a=='a'):
        print("a found",a)
        break

    print(a)
else:
    print("end")
