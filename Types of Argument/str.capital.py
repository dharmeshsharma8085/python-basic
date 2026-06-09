# def myfunc(str):
#     result=""
#     for i in range(len(str)):
#         if i%2==0:

#             result+=str[i].upper()
#         else:
#             result+=str[i]
#     return result

# print(myfunc("wdughifhofkhm"))
def old_macdonald(name):
    first=name[0].upper()
    middle=name[1:3]
    last=name[3].upper()
    rest=name[4:]
    return first+middle+last+rest

print(old_macdonald("macdonald"))