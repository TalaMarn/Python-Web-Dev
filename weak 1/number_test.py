#===========================
# Python Number Tests
#===========================
laptops = 150
tablet = 75
phone = 30
total_devices = laptops + tablet + phone
print(f"Initial Stock - Laptops:{laptops}, Tablets:{tablet}, Phones:{phone}, Total:{total_devices}")
# User Input
new_laptops = int(input("Enter number of new laptops received: "))
new_tablets = int(input("Enter number of new tablets received: "))
new_phones = int(input("Enter number of new phones received: "))
# Update Stock
laptops += new_laptops
tablet += new_tablets
phone += new_phones
total_devices = laptops + tablet + phone
print(f"Updated Stock - Laptops:{laptops}, Tablets:{tablet}, Phones:{phone}, Total:{total_devices}")

# Price
laptop_price = 999.99
tablet_price = 499.50
phone_price = 299.75

# Ask user
customer_laptops = int(input("How many laptops does the customer buy? "))
customer_tablets = int(input("How many tablets does the customer buy? "))
customer_phones = int(input("How many phones does the customer buy? "))
total_revenue = (customer_laptops * laptop_price) + (customer_tablets * tablet_price) + (customer_phones * phone_price)
print(f"Total Revenue: {total_revenue}")