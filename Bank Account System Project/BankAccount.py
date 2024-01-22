import Login, os
from datetime import datetime


class Account:
    def __init__(self,  balance: float, date_created: str, account_holder: str, account_id: int):
        self.account_holder = account_holder
        self.balance = balance
        self.date_created = date_created
        self.transaction_history = []
        self.account_id = account_id
    

    def transaction_details(self):
        print("TRANSACTION DETAILS".center(50, "-"))
        if self.transaction_history:
            for index, transaction in enumerate(self.transaction_history, start=1):
                print(f"{index}. {transaction.transaction_type}")
                print(f"Transaction Amount    : {transaction.transaction_amount}")
                print(f"Date Transaction Made : {transaction.date_transaction_made}")
                print(f"Time Transaction Made : {transaction.time_transaction_made}")
                print()
        
        else:
            print("No transactions history.")


    def deposit(self, amount: float):
        current_date_time = datetime.now()
        print("DEPOSIT".center(50, "-"))
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ₹{amount} was successful!\nBalance now: ₹{self.balance}")
            date, time = current_date_time.strftime("%d-%m-%Y"), current_date_time.time().strftime("%I:%M:%S %p")
            transaction = Transaction("Deposit", date, amount, time)
            self.transaction_history.append(transaction)
        
        else:
            print("Enter a positive value!")


    def withdrawl(self, amount: float):
        current_date_time = datetime.now()
        print("WITHDRAWL".center(50, "-"))
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                date, time = current_date_time.strftime("%d-%m-%Y"), current_date_time.time().strftime("%I:%M:%S %p")
                transaction = Transaction("Withdrawl", date, amount, time)

                self.transaction_history.append(transaction)
                print(f"Withdrawl of ₹{amount} was successful!")
                print(f"Balance now: ₹{self.balance}")
            else:
                print("Insufficient Funds!")
        
        else:
            print("Enter a Positive Value.")


    def print_account_details(self):
        print(f"Account Holder       : {self.account_holder}")
        print(f"Account Balance      : {self.balance}")
        print(f"Date Account Created : {self.date_created}")
        print(f"Account ID           : {self.account_id}")
        print(f"Transactions made    : {len(self.transaction_history)}")


class Transaction:
    def __init__(self, transaction_type: str, date_transaction_made: str, transaction_amount: float, time_transaction_made: str):
        self.transaction_type = transaction_type
        self.date_transaction_made = date_transaction_made
        self.time_transaction_made = time_transaction_made
        self.transaction_amount = transaction_amount
 
 
account = Account(balance=2000, date_created="20-10-2023", account_holder="Udaya", account_id=1)
accounts = {"udaya": {"password": "123", "account": account, "logged_in": True}}


def create_account():
    print("CREATE ACCOUNT".center(50, "-"))

    username = input("Enter your username: ")
    if username not in accounts:
        users = Login.create_account()
        accounts[username] = users

    else:
        print(f"Customer with {username} already exists!")
    

def create_bank_account():
    print("BANK ACCOUNT CREATION".center(50, "-"))
    print("Note: Bank Account Creation requires Customer Account.")
    current_date_time = datetime.now()
    username = input("Enter your username: ")
    if username in accounts and accounts[username]["logged_in"]:
        date = current_date_time.strftime("%d-%m-%Y")
        account_holder = input("Enter your Name: ")
        account_id = len(accounts) + 1
        while True:
            try: 
                balance = float(input("Enter your initial balance: "))
                print("Account Creation Successful!")
                account = Account(balance=balance, account_holder=account_holder, account_id=account_id, date_created=date)
                accounts[username]["account"] = account
                break
            except ValueError:
                print("Enter a valid input!") 
    
    elif username in accounts and not accounts[username]["logged_in"]:
        print("Log In is required to created Bank Account!")

    elif username not in accounts:
        print(f"No Customer was found with '{username}' username")
       

def make_transcation():
    print("TRANSACTION".center(50, "-"))

    username = input("Enter your username: ")

    if username in accounts and accounts[username]["logged_in"] and accounts[username]["account"]:
        try:
            transaction_type = int(input("DEPOSIT(1) or WITHDRAWL(2): "))
            amount = float(input("Enter the amount: "))
            match transaction_type:
                case 1:
                    accounts[username]["account"].deposit(amount=amount)
                case 2:
                    accounts[username]["account"].withdrawl(amount=amount)
                case _:
                    print("Invalid Input!")

        except ValueError:
            print("Invalid Input!")

    elif username in accounts and accounts[username]["account"] == None:
        print("You have not made the Bank Account yet")
    
    elif username in accounts and accounts[username]["account"] and not accounts[username]["logged_in"]:
        print("Log in is required to make a transaction.")
    
    elif username not in accounts:
        print(f"No Customer was found with '{username}' username")
    

def delete_customer():
    print("ACCOUNT DELETION".center(50, "-"))

    username = input("Enter your username: ")
    if username in accounts and accounts[username]["logged_in"]:
        sure = input("Are you sure you want to delete your account ?(y/n)").lower()
        match sure:
            case "y":
                print("Account deletion was successful!")
                del accounts[username]
            case "n":
                print("Goodbye! :)")
            case _:
                print("Invalid Input!")
    elif username not in accounts:
        print(f"Already there's no account with '{username}' username.")
    
    if username in accounts and accounts[username]["logged_in"] == False:
        print("Log In is required to delete the account.")


def print_transaction_details():
    username = input("Enter your username: ")
    if username in accounts and accounts[username]["logged_in"] and accounts[username]["account"] != None:
        accounts[username]["account"].transaction_details()
    elif username not in accounts:
        print(f"No Customer with '{username}' was found.")
    elif username in accounts and not accounts[username]["logged_in"]:
        print("Log in is required!")
    elif username in accounts and accounts[username]["account"] == None:
        print("No Bank Account was found.")




while True:
    os.system("cls")

    print("BANK ACCOUNT SYSTEM".center(50, "-"))
    print("1. CREATE CUSTOMER")
    print("2. CREATE BANK ACCOUNT")
    print("3. MAKE TRANSACTION")
    print("4. DELETE CUSTOMER")
    print("5. LOG IN")
    print("6. TRANSACTION DETAILS")
    print("7. EXIT")
    print("BANK ACCOUNT SYSTEM".center(50, "-"))

    try:
        choice = int(input("Enter you choice(1-7): "))
        match choice:
            case 1:
                create_account()
                input("Press enter to continue...")
            case 2:
                create_bank_account()
                input("Press enter to continue...")
            case 3:
                make_transcation()
                input("Press enter to continue...")
            case 4:
                delete_customer()
                input("Press enter to continue...")
            case 5:
                ask_username = input("Enter your username: ")
                Login.login(ask_username, accounts)
                input("Press enter to continue...")
            case 6:
                print_transaction_details()
                input("Press enter to continue...")
            case 7:
                print("Goodbye!")
                break
            case _:
                print("Invalid! Please enter a number between 1-7.")
                input("Press enter to continue...")
    
    except ValueError:
        print("Invalid! Please enter a integer value.")
        input("Press enter to continue...")
