#=================Database connection example=================
# sqlite3
import sqlite3
# 1.connect to database
conn = sqlite3.connect('bank.db') #create file if not exist

# 2.create cursor
cur = conn.cursor()

# 3.create table
cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)")

# 4.Save changes
conn.commit()

# 5.Close connection
conn.close()