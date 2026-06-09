class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy + self.chem + self.math)/3)+"%"
   # def cal(self):
    #        self.percentage=str((self.phy + self.chem + self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"
    # due to this no we dont have to make another
    # class called cal to chnage percentage
    # due to prperty it will change by it self
s1=student(45,454,45)
print(s1.percentage)

s1.phy=86
print(s1.phy) # changed
#s1.cal() # now our all percentage is change 
print(s1.percentage) # not change beauce it is set as an actual value we given before
