from bank_account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self,acc_num,name,password,balance=0,interest_rate=0.04,min_balance=500):
        super().__init__(acc_num,name,password,balance)
        self.interest_rate=interest_rate
        self.min_balance=min_balance
    def withdraw(self,amount):
        if amount<0:
            print("❌Invalid amount!")
        elif self.balance-amount<self.min_balance:
            print(f"Withdrawal denied!. Minimum balance of {self.min_balance} must be maintained.")
        else:
            super().withdraw(amount)
    def calculate_interest(self):
        interest=(self.balance*self.interest_rate)/100
        return round(interest,2)
    def show_account_type(self):
        print("Account Type: Savings")
