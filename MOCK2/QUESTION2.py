list=[1,2,3,4,5,6,7,8]
idx=0
total=0
while idx<len(list):
    if(list[idx]%2==0):
        total=total+list[idx]
        idx+=1


        print(total)
    