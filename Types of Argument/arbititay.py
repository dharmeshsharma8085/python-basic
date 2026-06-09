#args = we use this when we dont know thw len of args
def myfunc(*args):
    print(args)
    print(sum(args)*0.05)

myfunc(45,45656,8)

#**kwargs = it beahve like a dict that give ot n key value pair
def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My favorite friut is",kwargs["fruit"])
    else:
        print("there are no fruit")
        
myfunc(fruit="Apple",veggie="Onion")
#it will ignore veggie beaucse of if condition

# we can use both keyword together
def myfunc(*args,**kwargs):
    print(args,kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))
    
    
myfunc(2,4,5,6,7,8,9,fruit="grapes",animal="dog",food="Vadapav")

#we have to follow postion order that first if pass args as paramtr than 1st argumet should be args then kwargs
