#======== Mini Bank ========#
import sqlite3

# create connection
conn = sqlite3.connect('bank.db')

# create cursor
cur = conn.cursor()

# create table
cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            balance REAL
            )
            """)

# insert data
name = input ("Enter customer name: ")
balance = float(input("Enter initial balance: "))
cur.execute("INSERT INTO customers (name, balance) VALUES (?, ?)", (name, balance))

# save changes
conn.commit()

# display
cur.execute("SELECT * FROM customers")
for row in cur.fetchall():
    print(row)

# close connection
conn.close()