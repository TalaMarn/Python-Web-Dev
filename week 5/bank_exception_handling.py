#============Bank Exception Handling======================

class InsufficientFundsError(Exception):
    "Custom exception for insufficient funds"
    pass
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")
        
    def get_balance(self):
        return self.__balance
    
# Example usage
account = BankAccount("Alice", 1000)
account.deposit(500)
try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error: {e}")

else: 
    print("Withdrawal successful")
finally:
    print("Current balance: ", account.get_balance())