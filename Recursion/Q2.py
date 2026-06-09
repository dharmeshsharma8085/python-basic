def print_list(list,idx=0):
    if(idx == len(list)):
        return 0
    print(list[idx])
    print_list(list,idx+1)

nums=[1,2,3,4,5,6,7,8,9]

print_list(nums)
