from account import Account
from saving_account import SavingAccount




acc1 = Account("Nuredin Bedru", 20000)

acc1.deposit(50000)
acc1.withdraw(100000)

acc1.balance_inquery()

sacc1 = SavingAccount("Nuredin", 20000)
sacc1.add_interest(0.015)


