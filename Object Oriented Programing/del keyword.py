class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    
s=Student("Ankit",67)
print(s.name,s.age)
#let use del keyword to delete name
del s.name
del s
print(s.name) #show error becuase no our s.name is not defined