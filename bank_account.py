from tabulate import tabulate
from datetime import datetime

class BankAccount:

    def __init__(self,acc_num,name,password,balance=0):
        self.acc_num=acc_num
        self.name=name
        self.password=password
        self.balance=balance
        self.transaction_history=[]

    def __str__(self):
        return f"Account No: {self.acc_num}, Name: {self.name}, Balance: ₹{self.balance}"

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transaction_history.append([timestamp, self.acc_num, amount,"-",self.balance])
            print(f"Rs.{amount} deposited successfully")
        else:
            print(f"❌Invalid deposit amount!")

    def withdraw(self,amount):
        if amount<0:
            print("❌Invalid amount!.")
        elif self.balance>=amount:
            self.balance-=amount
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transaction_history.append([timestamp, self.acc_num, "-", amount, self.balance])
            print(f"✅Rs.{amount} withdrawn successfully")
        else:
            print("⚠️Insufficient balance.")


    def check_balance(self):
        print(f"Account balance: {self.balance}")


    def log_transaction(self):
        if not self.transaction_history:
            print(f"No transactions found!")
        else:
            headers = ["Date", "Account No", "Deposit", "Withdrawn", "Balance"]
            print(tabulate(self.transaction_history, headers=headers, tablefmt="pretty"))
    def show_details(self):
        return {"Account Number": self.acc_num, "Name": self.name, "Balance": self.balance}

    def authenticate(self,password):
        return self.password==password

    def change_password(self):
        count=0
        while count<3:
            old_password=input("Enter your old password: ").strip()
            if old_password:
                while self.password==old_password:
                    new_password=input("Enter new password: ").strip()
                    if self.password!=new_password:
                        self.password = new_password
                        print("Your password changed successfully!")
                        return
                    else:
                        print("New password cannot be same as the old password.")
                else:
                    count += 1
                    print("Your password is incorrect, try again!")
            else:
                print("Password cannot be empty.")
        print("You reached the maximum number of tries. Try after 24 hours!")



