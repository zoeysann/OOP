
class BankAccount:
    def __init__(self, balance, owner , iban):
        self.balance = balance
        self.owner = owner
        self.iban = iban
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Current balance: ${self.balance}")


account = BankAccount(100)
account.display_balance()
account.deposit(50) 
account.withdraw(30)
account.withdraw(200)
account.display_balance() 
