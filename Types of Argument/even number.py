# def myfunc(*args):
#     mylist=[]
#     for i in args:
#         if i%2==0:
#             mylist=mylist.append(i)
#         else:
#             print("There are no even number")
    
#     return mylist
            

# myfunc=(1,2,3,4,5,6,7,8)
def myfunc(*args):
    return[ i for i in args if i%2==0]
print(myfunc(12,4,5,6,6,77))