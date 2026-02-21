### Encasulation
 ### Hide internal Detail and restrict access to directly access some of the object's components.
 ### access only from methods (getter and setter)
 ### protect data and control 

# Syntax
# 1. Public  x => accessible from anywhere
# 2. Protected _x => accessible within class and subclasses
# 3. Private __x => accessible only within class

## Example
class BankAcc:
    def __init__(self, owner, balance):
        self.owner = owner # public
        self.__balance = balance # private

    # getter method for balance
    def get_balance(self):
        return self.__balance
    
    # setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

acc = BankAcc("Alice", 1000)
print(acc.owner) # Accessing public attribute
print(acc.get_balance()) # Accessing private attribute via getter method
acc.deposit(500) # Accessing private attribute via setter method
acc.withdraw(200) # Accessing private attribute via setter method