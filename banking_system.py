import string
import random

# Account creation or logging in
class Account:
    def __init__(self):
        choice = int(input("Enter 1 to create an account, 2 to log in to an existing one: "))
        # Choice validation
        while choice not in (1, 2):
            choice = int(input("Invalid choice. Enter 1 to create an account, 2 to log in to an existing one: "))

        # Account creation
        if choice == 1:
            print("----CREATE ACCOUNT----")

            # Read existing usernames
            try:
                with open("accounts.txt", "r") as f:
                    accounts = f.readlines()
                existing_usernames = [line.strip().split(",")[1] for line in accounts]
            except FileNotFoundError:
                existing_usernames = []  # File doesn't exist yet

            # Username + validation + uniqueness
            username = input("enter a username with letters only (eg. someone): ")
            while not username.isalpha() or username in existing_usernames:
                if not username.isalpha():
                    username = input("letters only, enter another username: ")
                else:
                    username = input("username already exists, choose another one: ")

            # Password + validation 
            password = input("Enter your password: ")
            while (not any(c.isdigit() for c in password)) or (not any(c.isupper() for c in password)):
                password = input("Enter a stronger password: ")
                

            # Generate unique account number
            def generate_account_number(existing_numbers):
                while True:
                    num = random.randint(10000000, 99999999)  # 8-digit account number
                    if num not in existing_numbers:
                        return num

            # Read existing account numbers
            try:
                with open("accounts.txt", "r") as f:
                    accounts = f.readlines()
                existing_numbers = [int(line.strip().split(",")[0]) for line in accounts]
            except FileNotFoundError:
                existing_numbers = []

            # Generate new account number
            num = generate_account_number(existing_numbers)

            # Save credentials with initial balance 0
            with open("accounts.txt", "a") as f:
                f.write(f"{num},{username},{password},0\n")


            print("Account created successfully!")
            self.username = username
            self.password = password

        # Login
        else:
            print("----LOG IN----")
            username = input("enter your username: ")

            with open("accounts.txt", "r") as f:
                accounts = f.readlines()

            usernames = [line.strip().split(",")[1] for line in accounts]

            while username not in usernames:
                username = input("username not found, try again: ")

            
            password = input("Enter your password: ")

            correct_password = [
                line.strip().split(",")[2]
                for line in accounts
                if line.strip().split(",")[1] == username
            ][0]

            while password != correct_password:
                password = input("Incorrect password, try again: ")

            print("Logged in successfully!")
        self.username = username
        self.password = password
        self.choice = choice
    def show_balance(self):
        with open("accounts.txt", "r") as f:
            for line in f:
                account_number, username, password, balance = line.strip().split(",")
                if username == self.username:
                    print(f"Account Number: {account_number}")
                    print(f"Username: {username}")
                    print(f"Balance: ${balance}")
                    return  # stop after finding the logged-in user
            print("Account not found.")

                    

            

        
    

acc = Account()
acc.show_balance()
#the main banking methods:
class Bank:
    def __init__(self, account):
        self.account = account  # pass the logged-in Account object

    def menu(self):
        while True:
            print("1-deposit")
            print("2-withdraw")
            print("3-show balance")
            print("4-exit")
            option = int(input("Choose an action: "))
            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.account.show_balance()
            else:
                break

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        while amount <= 0:
            amount = float(input("Invalid. Enter a positive amount: "))

        # update balance in accounts.txt
        with open("accounts.txt", "r") as f:
            lines = f.readlines()

        with open("accounts.txt", "w") as f:
            for line in lines:
                acc_num, username, pwd, balance = line.strip().split(",")
                if username == self.account.username:
                    balance = str(float(balance) + amount)
                f.write(f"{acc_num},{username},{pwd},{balance}\n")

        print(f"${amount} deposited successfully!")
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        while amount <= 0:
            amount = float(input("Invalid. Enter a positive amount: "))
       


        # update balance in accounts.txt
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
           

        with open("accounts.txt", "w") as f:
            for line in lines:
                acc_num, username, pwd, balance = line.strip().split(",")
                balance = float(balance)
                while amount>balance:
                    amount = float(input("Invalid. Not enough funds, try another amount: "))
                if username == self.account.username:
                    balance = str(float(balance) - amount)
            
                    
                f.write(f"{acc_num},{username},{pwd},{balance}\n")

        print(f"${amount} withdrawed successfully!")
bank_system = Bank(acc)  # pass the logged-in account
bank_system.menu()       # start the interactive menu
