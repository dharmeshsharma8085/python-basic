def splicer(my_string):
    if len(my_string)%2==0:
        return "Even"
    else:
        return my_string[0]
    
names=["ankit","Dharmesh","sahil"]
list(map(splicer,names))
