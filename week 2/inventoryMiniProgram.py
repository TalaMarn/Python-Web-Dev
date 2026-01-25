

Inventory = []
# product 1
product1 = {}
product1["name"] = input("Enter Product1 Name: ")
product1["price"] = float(input("Enter Price: "))
product1["qty"] = int(input("Enter Quantity: "))
Inventory.append(product1)

# product 2
product2 = {}
product2["name"] = input("Enter Product2 Name: ")
product2["price"] = float(input("Enter Price: "))
product2["qty"] = int(input("Enter Quantity: "))
Inventory.append(product2)

# product 3
product3 = {}
product3["name"] = input("Enter Product3 Name: ")
product3["price"] = float(input("Enter Price: "))
product3["qty"] = int(input("Enter Quantity: "))
Inventory.append(product3)
print("\n----- Inventory List -----")
print(Inventory)

# Choose a product(by index)
print("\n----- Choose a Product(by index) -----")
print("0: ", Inventory[0]["name"])
print("1: ", Inventory[1]["name"])
print("2: ", Inventory[2]["name"])

choice = int(input("Enter your choice (0-2): "))
product = Inventory[choice]
# Action
print('\n 1. View Product')
print("2. Add Product")
print("3. Sell Product")
action = int(input("Enter your action (1-3): "))
# View
if action == 1:
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["qty"])

# Add
elif action == 2:
    add_qty = int(input("Enter quantity to add: "))
    product["qty"] += add_qty
    print("Updated Quantity:", product["qty"])

# Sell
elif action == 3:
    sell_qty = int(input("Enter quantity to sell: "))
    if sell_qty <= product["qty"]:
        product["qty"] -= sell_qty
        total = sell_qty * product["price"]
        print("Total Price:", total)
        print("Remaining Quantity:", product["qty"])
    else:
        print("Insufficient stock!")

else:
    print("Invalid action!")