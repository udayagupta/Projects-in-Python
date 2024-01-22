from PasswordStrenght import *


def create_account():

    print_password_parameters()

    while True:
        password = input("Enter you password: ").strip()

        if password_checker(password):
            print("Password Accepted!")
            print("Account Created!")
            return {"password": password, "account": None, "logged_in": False}

        else:
            print("Invalid! Password must match above conditions.")


def login(username: str, accounts: dict):
    if username in accounts:
        password = input("Enter your password: ")

        if accounts[username]["password"] == password:
            print("Login was successful!")
            accounts[username]["logged_in"] = True
            return True
        else:
            print("Wrong Password!")
    else:
        print(f"No Customer with '{username}' username was found.")
        return False

        
