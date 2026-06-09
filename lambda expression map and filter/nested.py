# x=25
# def printer():
#     x=50
#     return x

# print(x) # 25

# print(printer()) #50

x=50
def fun():
    global x
    
    x=56
    print("X is ",x)
    
print(x)  