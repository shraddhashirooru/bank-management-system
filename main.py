from bank_account import BankAccount
from saving_account import SavingAccount
from current_account import CurrentAccount
from bank_system import BankSystem
import tabulate
import datetime
import json
import os

DATA_FILE = "bank_data.json"

def save_data(bank_system):
    data = {
        "next_acc_num": bank_system.next_acc_num,
        "accounts": {}
    }

    for acc_num, account in bank_system.accounts.items():
        acc_type = type(account).__name__
        acc_data = {
            "acc_num": account.acc_num,
            "name": account.name,
            "password": account.password,
            "balance": account.balance,
            "transaction_history": account.transaction_history,
        }

        if acc_type == "SavingAccount":
            acc_data["interest_rate"] = account.interest_rate
            acc_data["min_balance"] = account.min_balance
        elif acc_type == "CurrentAccount":
            acc_data["overdraft_limit"] = account.overdraft_limit

        data["accounts"][acc_num] = {
            "type": acc_type,
            "data": acc_data
        }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return BankSystem()

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    bank_system = BankSystem()
    bank_system.next_acc_num = data.get("next_acc_num", 1001)

    for acc_num_str, acc_info in data["accounts"].items():
        acc_type = acc_info["type"]
        acc_data = acc_info["data"]
        acc_num = int(acc_num_str)

        if acc_type == "SavingAccount":
            account = SavingAccount(
                acc_num=acc_data["acc_num"],
                name=acc_data["name"],
                password=acc_data["password"],
                balance=acc_data["balance"],
                interest_rate=acc_data.get("interest_rate", 0.04),
                min_balance=acc_data.get("min_balance", 500),
            )
        elif acc_type == "CurrentAccount":
            account = CurrentAccount(
                acc_num=acc_data["acc_num"],
                name=acc_data["name"],
                password=acc_data["password"],
                balance=acc_data["balance"],
                overdraft_limit=acc_data.get("overdraft_limit", 5000),
            )
        else:
            account = BankAccount(
                acc_num=acc_data["acc_num"],
                name=acc_data["name"],
                password=acc_data["password"],
                balance=acc_data["balance"],
            )

        account.transaction_history = acc_data.get("transaction_history", [])
        bank_system.accounts[acc_num] = account

    return bank_system

if __name__=="__main__":
    print("==========   Welcome to Bank System  ==========")
    print("Please select an option from the main menu:")
    bank = load_data()

    while True:
        try:
            print("-----  Main Menu  -----")
            option=int(input("1.Customer \n2. BankStaff/Admin \n3.Exit \n Enter your choice:"))
            if option ==1:
                while True:
                    print("----- Customer Operations Menu -----")
                    print("1. Create Account \n2. Deposit Money\n3. Withdraw Money \n4. Check Balance \n5. View Account Details \n6. View Transaction History \n7. Change Password \n8. Delete Account \n9. Go to Main Menu \n0. Exit")
                    option1=int(input("Enter your choice: "))
                    if option1==1:
                        name=str(input("Please enter your full name: "))
                        acc_type=input("Select account type (Savings or Current): ").strip()
                        password=input("Set a secure password for your account: ")
                        initial_deposit=int(input("Enter initial deposit amount: "))
                        bank.create_account(name,acc_type,password,initial_deposit)
                        save_data(bank)
                    elif option1==2:
                        acc_num=int(input("Enter your account number: "))
                        amount=int(input("Enter the amount: "))
                        bank.deposit_to_account(acc_num, amount)
                        save_data(bank)
                    elif option1==3:
                        acc_num = int(input("Enter your account number: "))
                        password=input("Enter your password: ")
                        amount = int(input("Enter the amount: "))
                        bank.withdraw_from_account(acc_num, password,amount)
                        save_data(bank)
                    elif option1==4:
                        acc_num = int(input("Enter your account number: "))
                        bank.check_balance(acc_num)
                    elif option1==5:
                        acc_num = int(input("Enter your account number: "))
                        bank.show_account_details(acc_num)
                    elif option1==6:
                        acc_num = int(input("Enter your account number: "))
                        bank.show_transactions_history(acc_num)
                    elif option1==7:
                        acc_num = int(input("Enter your account number: "))
                        bank.change_password(acc_num)
                    elif option1==8:
                        acc_num = int(input("Enter your account number: "))
                        password=input("Enter your password: ")
                        bank.delete_account(acc_num,password)
                        save_data(bank)
                    elif option1==9:
                        break
                    elif option1==0:
                        print("Thank you for banking with us. Have a wonderful day!")
                        exit()
                    else:
                        print("❌Invalid option. Try again.")
                    print()
            elif option==2:
                admin_code=input("Enter admin access code: ")
                if admin_code=="Admin@123":
                    bank.list_all_accounts()
                else:
                    print("❌Access denied. Invalid code")
            else:
                print("Thank you for choosing our bank. We appreciate your trust!")
                break
        except ValueError:
            print("Please enter a valid number.")