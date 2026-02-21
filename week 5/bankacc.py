class BankAcc:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

#===============End=================

#===============Child Class 1=================

class SavingsAcc(BankAcc):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Added interest: {interest}. New balance: {self.balance}")

#===============Child Class 2=================
class CurrentAcc(BankAcc):
    def withdraw(self, amount):
        # Allow overdraft
        if amount <= self.balance + 500:
            self.balance -= amount
            print(f"Withdrew {amount}(Overdraft allowed). New balance: {self.balance}")

        else:
            print("Overdraft limit exceeded")

#===============Testing=================

SavingsAcc = SavingsAcc("Alice", 1000)
SavingsAcc.deposit(500)
SavingsAcc.add_interest()
SavingsAcc.withdraw(1500)
SavingsAcc.add_interest()

CurrentAcc = CurrentAcc("Bob", 2000)
CurrentAcc.withdraw(2500)
CurrentAcc.withdraw(-500)

#### Types of Inheritence
# 1. Single Inheritence => one parent
# 2. Multiple Inheritence => more than one  #### class Child(Parent1, Parent2)
# 3. Multilevel Inheritence => Parent -> Child -> GrandChild
### class Parent:
###    pass
### class Child(Parent):
###    pass
### class GrandChild(Child):
###    pass
# 4. Hierarchical Inheritence => one parent -> multiple child 