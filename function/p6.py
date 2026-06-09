lst=[1,2,3,4,5,6]
lst_even=[]
l=len(lst)
def even_lst(lst):
    for i in range(0,l):
        if lst[i]%2==0:
            lst_even.append(lst[i])
    
    return lst_even

print(even_lst(lst))