nums=[5,8,3,12,7,20,1]
new_list=[]
def square_even(list):
    idx=0
    if(list[idx]%2==0):
        new_list.append(list[idx]**2)

    return new_list

print(square_even(new_list))