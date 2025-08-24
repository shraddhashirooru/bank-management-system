from saving_account import SavingAccount
from current_account import CurrentAccount
from tabulate import tabulate

class BankSystem:
    def __init__(self):
        self.accounts={}
        self.next_acc_num=1001
    def create_account(self,name,acc_type,password,initial_deposit):
        acc_num=self.next_acc_num
        if acc_type.lower()=="savings":
            account=SavingAccount(acc_num,name,password)
            account.deposit(initial_deposit)
            self.next_acc_num += 1

        elif acc_type.lower()=="current":
            account=CurrentAccount(acc_num,name,password)
            account.deposit(initial_deposit)

            self.next_acc_num += 1

        else:
            print(f"Invalid account type.")
            return

        self.accounts[acc_num] = account
        print(f"✅ {acc_type.capitalize()} Account created successfully! Account Number: {acc_num}")
        return acc_num

    def find_account(self, acc_num):
        return self.accounts.get(acc_num)

    def authenticate_user(self, acc_num, password):
        account = self.find_account(acc_num)
        if account and account.authenticate(password):
            return account
        print("❌ Authentication failed.")
        return None

    def deposit_to_account(self, acc_num, amount):
        account = self.find_account(acc_num)
        if account:
            account.deposit(amount)
        else:
            print("❌ Account not found.")

    def withdraw_from_account(self, acc_num,password,amount):
        account = self.find_account(acc_num)
        if account:
            if account.authenticate(password):
                account.withdraw(amount)
            else:
                print("Incorrect password.")
        else:
            print("❌ Account not found.")

    def show_account_details(self, acc_num):
        account = self.find_account(acc_num)
        if account:
            print(account)
        else:
            print("❌ Account not found.")

    def show_transactions_history(self, acc_num):
        account = self.find_account(acc_num)
        if account:
            account.log_transaction()
        else:
            print("❌ Account not found.")

    def check_balance(self, acc_num):
        account = self.find_account(acc_num)
        if account:
            account.check_balance()
        else:
            print("❌ Account not found.")

    def change_password(self, acc_num):
        account = self.find_account(acc_num)
        if account:
            account.change_password()
        else:
            print("Account not found.")

    def delete_account(self, acc_num, password):
        account = self.authenticate_user(acc_num, password)
        if account:
            del self.accounts[acc_num]
            print("🗑️ Account deleted successfully.")

    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts found!.")
            return

        data = []
        for acc_num, acc in self.accounts.items():
            acc_type = type(acc).__name__
            data.append([acc_num, acc.name, acc_type, acc.balance])

        print(tabulate(data, headers=["Account No", "Name", "Type", "Balance"], tablefmt="pretty"))
