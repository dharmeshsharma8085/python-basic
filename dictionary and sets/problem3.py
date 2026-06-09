#WAP to enter a mark of 3 subject from 
# the user and store thrm in a dictionary
#  . Start with an empty dictionary &ass
#  one by one . use subject name as key 
# &marks as value

marks={}
x=int(input("Enter your marks:"))
marks.update({"phy":x})

y=int(input("Enter your marks:"))
marks.update({"chem":y})
z=int(input("Enter your marks:"))
marks.update({"math":z})
print(marks)
