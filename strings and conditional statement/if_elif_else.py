# age=input("Enter your age")
# if(age>="18"):
#     print("you are eligble for vote")#indentation proper spacing 
# elif(age=="18"):
#     print("YES you can vote under guidance")
# else:    
#     print("you are not eligble for vote")
 
 # we can use if and elif condition
 #multiple time but we use else condition
 #only one time in last if both above
 #condition is false

grade=input("Enter your grade:")
if(grade>="90"):
    print("your grade is A+")
elif("80"<= grade <="90"):
    print("your grade is A")
elif("60"<= grade <="80"):
    print("your grade is B")
elif("40"<= grade <="60"):
    print("your grade is C")
elif(grade>="40"):
    print("your grade is D")
else:
    print("something went wrong please try again")