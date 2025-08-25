# 🏦 Bank Management System (Python Project)

A simple yet functional **Bank Management System** built using Python and Object-Oriented Programming (OOP) concepts. This CLI-based application allows users to manage their bank accounts with features like deposits, withdrawals, transaction history, and admin access.

**Key Highlight:**  
All account and transaction data are stored persistently in a local `bank_data.json` file using JSON serialization.  
This means that data is preserved even after closing the program, making the system more realistic and practical than many beginner-level banking simulations.

---

##  Features:

#### Customer Functionalities:
- Create **Savings** or **Current** account
- Deposit and withdraw money
- View balance and transaction history
- Change account password
- Delete account

#### Admin Functionalities:
- View all customer accounts (admin access protected)

#### Security:
- Password-protected accounts
- Admin access requires a secret code

---

## Technologies & Libraries:

- **Python 3.x**
- `tabulate` — for neat tabular formatting
- `json` — to persist data across runs
- `datetime` — for transaction timestamps

---

## OOP Concepts Used:

| Concept                 | How it's used                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| **Class & Object**     | BankAccount, SavingAccount, CurrentAccount, and BankSystem classes            |
| **Encapsulation**      | Attributes like `password`, `balance` are protected via methods               |
| **Inheritance**        | SavingAccount and CurrentAccount inherit from `BankAccount`                   |
| **Polymorphism**       | `withdraw()` overridden in child classes                                      |
| **Abstraction**        | `deposit()`, `withdraw()` hide implementation details                         |

---

## How to Run

1. Clone the repo:

```
    git clone https://github.com/shraddhashirooru/bank-management-system.git    
    cd bank-management-system
```
2. Install dependencies:
```
    pip install -r requirements.txt
```
3. Run the program:
```
    python main.py
 ```  
---
## Sample output:

- Only one example per operation is shown for brevity.
- Menus repeat as needed for multiple operations.

### Welcome Screen:

```
==========   Welcome to Bank System  ==========
Please select an option from the main menu:
-----  Main Menu  -----
1.Customer 
2. BankStaff/Admin 
3.Exit
 Enter your choice:
```

### Customer operations menu:

```
 Enter your choice:1
----- Customer Operations Menu -----
1. Create Account 
2. Deposit Money
3. Withdraw Money 
4. Check Balance 
5. View Account Details 
6. View Transaction History 
7. Change Password 
8. Delete Account 
9. Go to Main Menu 
0. Exit
```
### Creating Account:

```
Enter your choice: 1
Please enter your full name: Savitri
Select account type (Savings or Current): Savings
Set a secure password for your account: S@678
Enter initial deposit amount: 3800
Rs.3800 deposited successfully
✅ Savings Account created successfully! Account Number: 1007
```

### Deposit Money:

```
----- Customer Operations Menu -----
...
Enter your choice: 2
Enter your account number: 1007
Enter the amount: 2000
Rs.2000 deposited successfully
```

### Withdraw Money:

 ```
----- Customer Operations Menu -----
...
Enter your choice: 3
Enter your account number: 1007
Enter your password: S@678
Enter the amount: 4800
✅Rs.4800 withdrawn successfully
```

### Check Balance:
```
----- Customer Operations Menu -----
...
Enter your choice: 4
Enter your account number: 1007
Account balance: 1000
```
### Account Details:

```
----- Customer Operations Menu -----
...
Enter your choice: 5
Enter your account number: 1007
Account No: 1007, Name: Savitri, Balance: ₹1000
```

### Transaction History:
```
----- Customer Operations Menu -----
...
Enter your choice: 6
Enter your account number: 1007
+---------------------+------------+---------+-----------+---------+
|        Date         | Account No | Deposit | Withdrawn | Balance |
+---------------------+------------+---------+-----------+---------+
| 2025-08-25 07:00:55 |    1007    |  3800   |     -     |  3800   |
| 2025-08-25 07:11:04 |    1007    |  2000   |     -     |  5800   |
| 2025-08-25 07:13:37 |    1007    |    -    |   4800    |  1000   |
+---------------------+------------+---------+-----------+---------+
```
### Change Password:

```
----- Customer Operations Menu -----
...
Enter your choice: 7
Enter your account number: 1007
Enter your old password: S@678
Enter new password: S.123
Your password changed successfully!
```

### Delete Account:

```
----- Customer Operations Menu -----
...
Enter your choice: 8
Enter your account number: 1007
Enter your password: S.123
🗑️ Account deleted successfully.
```
### All Accounts (Admin Access):

```
----- Customer Operations Menu -----
...
Enter your choice: 9
-----  Main Menu  -----
1.Customer 
2. BankStaff/Admin 
3.Exit 
 Enter your choice:2
Enter admin access code: Admin@123
+------------+----------+----------------+---------+
| Account No |   Name   |      Type      | Balance |
+------------+----------+----------------+---------+
|    1001    | shraddha | SavingAccount  |  7000   |
|    1002    |   Hari   | SavingAccount  |  8300   |
|    1003    | Pallavi  | CurrentAccount |  6000   |
|    1005    |  Pavan   | CurrentAccount |  6500   |
|    1006    |  Gaurav  | SavingAccount  |  2000   |
+------------+----------+----------------+---------+
```
## Admin Access:
To view all accounts as a bank staff, select the Admin option and use the following code:

Access Code: Admin@123

## Dependencies:

Listed in requirements.txt:

tabulate

## Future Improvements:

GUI integration (Tkinter or PyQt)

Interest auto-calculation for savings accounts

Password hashing for better security

Account statements export (PDF/CSV)

Unit testing
