class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_number=acc
    
    def debit(self,amount):
        self.balance -= amount
        print("RS",amount,"was debited from your acc_no 1")
        print("total balance", self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was credited from your acc_no 1")
        print("total balance", self.get_balance())
    
    
    def get_balance(self):
        return self.balance    
        
        
    
    
acc1=Account(1000000, 1)
print(acc1.balance)
acc1.credit(700)
acc1.debit(1456)
acc1.get_balance()