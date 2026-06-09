class account:
    def __init__(self,ac_no,pas):
        self.ac_no=ac_no
        self.__pas=pas
    
    def reset_pass(self):
        print(self.__pas)
        
acc1=account(1244,9999)
print(acc1.ac_no)#acc1.__pas) #show error beacuse it is private now
acc1.reset_pass
        