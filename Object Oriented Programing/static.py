class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def average(self):
        sum=0
        for val in self.marks:
            sum += val
            
        print(self.name,sum/3)
    @staticmethod # conert normal class to static class    
    def college():
        print("BKIET")
        
s=student("Dharmesh",[56,56,45])
s.average()
s.name="Lucky"
s.average()
s.college()