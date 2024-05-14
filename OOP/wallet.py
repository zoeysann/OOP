
class wallet():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def add(self, money):
        if money >= 0:
            self.balance = self.balance + money
        else:
            print("Money is invalid")
    
    def minus(self, money):
        if money > self.balance:
            print("You don't have enough money :(")
        else:
            self.balance = self.balance - money

    def balance(self):
        print(f"You have {self.balance} money")

