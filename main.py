from bank_system import BankSystem
if __name__=="__main__":
    print("==========   Welcome to Bank System  ==========")
    print("Please select an option from the main menu:")
    bank = BankSystem()

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
                    elif option1==2:
                        acc_num=int(input("Enter your account number: "))
                        amount=int(input("Enter the amount: "))
                        bank.deposit_to_account(acc_num, amount)
                    elif option1==3:
                        acc_num = int(input("Enter your account number: "))
                        password=input("Enter your password: ")
                        amount = int(input("Enter the amount: "))
                        bank.withdraw_from_account(acc_num, password,amount)
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