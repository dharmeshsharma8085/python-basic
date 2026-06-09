nums=[4,7,12,9,20,5]
idx=0
new_list=[]
def great(list):
    for idx in range(len(list)):
        if(list[idx]>10):
        
            new_list.append(list[idx])



    return new_list
        
print(great(nums))
        
