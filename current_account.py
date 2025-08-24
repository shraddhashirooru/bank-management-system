from bank_account import BankAccount
from datetime import datetime

class CurrentAccount(BankAccount):
    def __init__(self,acc_num,name,password,balance=0,overdraft_limit=5000):
        super().__init__(acc_num,name,password,balance)
        self.overdraft_limit=overdraft_limit

    def check_overdraft_limit(self):
        if self.balance<0:
            print(f"Available overdraft limit is {self.overdraft_limit+self.balance}")
        else:
            print(f"Available overdraft limit is {self.overdraft_limit}")
    def withdraw(self,amount):
        if amount<0:
            print("❌Invalid amount!")
        elif self.balance+self.overdraft_limit>=amount:
            self.balance-=amount
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transaction_history.append([timestamp, self.acc_num, "-", amount, self.balance])
            print(f"Withdrawal of Rs.{amount} is successful. Overdraft used: {abs(min(self.balance,0))}")
        else:
            print(f"Withdrawal denied. Overdraft limit exceeded.")
