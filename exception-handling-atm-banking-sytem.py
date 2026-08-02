# Banking ATM System
# Author: Takyi Ekow Daniels
# ID: FOE.41.006.152.25

# Custom Exception
class InsufficientFundsError(Exception):
    pass


# BankAccount Class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Deposit Method
    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError("Negative deposit not allowed!")
            self.balance += amount
            print(f"GHS {amount} deposited successfully!")
            print(f"New Balance: GHS {self.balance}")

        except ValueError as e:
            print(f"Deposit Error: {e}")

    # Withdraw Method
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Invalid withdrawal amount!")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds!")
            self.balance -= amount
            print(f"GHS {amount} withdrawn successfully!")
            print(f"Remaining Balance: GHS {self.balance}")

        except ValueError as e:
            print(f"Withdrawal Error: {e}")

        except InsufficientFundsError as e:
            print(f"Transaction Failed: {e}")

    # Check Balance Method
    def check_balance(self):
        print(f"Account Owner : {self.owner}")
        print(f"Balance       : GHS {self.balance}")


# ---- Menu ----
account = BankAccount("Ekow Daniels", 500)

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice!")