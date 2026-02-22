# #=========exception handling=========
# balance = 1000
# try:
#     withdraw = int(input("Enter the amount to withdraw: "))
#     if withdraw > balance:
#         raise Exception("Insufficient balance")
#     balance -= withdraw
#     print(f"Withdrawal successful. Remaining balance: {balance}")
# except ValueError:
#     print("Invalid input. Please enter a numeric value.")
# except Exception as e:
#     print("Errror: ", e)

# print("Program continues...")

#=======index error===========

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Error: ", e)


#=======key error===========
try:
    data = {"Name": "John"}
    print(data["Age"])
except KeyError as e:
    print("Error: ", e)


#=======file not found error===========
try:
    file = open("test.txt", "r")
except FileNotFoundError as e:
    print("Error: ", e)

#=======AttributError=================
try:
    num = 10
    num.append(5)
except AttributeError as e:
    print("Error: ", e)

#=======NameError=================
try:
    print(x)
except NameError as e:
    print("Error: ", e)

#=======importError=================
try:
    import sdk
except ImportError as e:
    print("Error: ", e)

#========RuntimeError=================
try:
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print("Error: ", e)