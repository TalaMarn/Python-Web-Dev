#========== transaction_handling.py ==========
import sqlite3

# create connection
conn = sqlite3.connect('bank.db')

# create cursor
cur = conn.cursor()

# create table
cur.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            balance REAL
            )
            """)

# commit changes
conn.commit()
try:
    cur.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cur.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    conn.commit()
    print("Transaction completed successfully")
except Exception as e:
    conn.rollback()
    print("Transaction failed, rolled back. Error:", e)
finally:
    conn.close()

# close connection
conn.close()