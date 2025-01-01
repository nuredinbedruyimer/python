from account import Account

class SavingAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
    
    def add_interest(self, rate):
        interest = self.balance * rate
        self.balance += interest
        
        print(f"{self.owner} Your Balance After Interest : {self.balance}")