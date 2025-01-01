class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
        print(f"{self.owner} Deposit {amount}, New Balance : {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner} Withdraw {amount}, Remaining Balance : {self.balance}")
        else:
            print(f"{self.owner} your balance is insufficient")