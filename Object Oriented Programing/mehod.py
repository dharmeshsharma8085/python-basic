class Student:
    def __init__(self,fullname):
        self.fullname=fullname
        
    def hello(self):
        print("hello",self.fullname) # method
    
s1=Student("Dharmesh")
s1.hello() # obj.attr


# class is a combination of data and method