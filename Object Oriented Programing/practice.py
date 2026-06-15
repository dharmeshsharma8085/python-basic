amount=0
class Account:
    def __init__(self,acc_no,balance=0):
        self.balance=balance
        self.acc_no=acc_no 
    def debit(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print("RS",amount,"was debited from your acc_no 1")
            print("total balance", self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was credited to your acc_no 1")
        print("total balance", self.get_balance())

    def get_balance(self):
        return self.balance    
        
        
    
    
acc1=Account(1, 100000)
print(acc1.balance)
acc1.credit(700)
acc1.debit(1456)
acc1.get_balance()