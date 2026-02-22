#=========exception handling=========
balance = 1000
try:
    withdraw = int(input("Enter the amount to withdraw: "))
    if withdraw > balance:
        raise Exception("Insufficient balance")
    balance -= withdraw
    print(f"Withdrawal successful. Remaining balance: {balance}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except Exception as e:
    print("Errror: ", e)

print("Program continues...")