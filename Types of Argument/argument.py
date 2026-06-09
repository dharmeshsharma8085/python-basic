def myfunc(name,age,phone,rollno,branch,college="BKbiet"):
    print("hi",name)
    print(f'I am {age} year old ')
    print("My phone number is",phone)
    print("My current Rollno are",rollno)
    print("my branch is btech",branch)
    print("My college is",college)
    
    
myfunc("Dharmesh",19, 7558439066, "24Ebkai050",branch="Artifical Intillegence")

#There are 4 types of argument
# 1 postional that follow there postion here name age rollno and phone are postional argument
#2 keyword= when we now thw parameters but nott there order or postion then we use keyword argument example branch
#3 default= this argument have alrady some default value that is predefined in function by there parameter

#note always complier follow this order first poational then keyworf then default
#we can't write keyword before postional 

#4 is arbitiary of varible length 
