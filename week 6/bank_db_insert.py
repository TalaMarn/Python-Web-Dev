#=================insert data into database=================
import sqlite3

# 1.connect to database
conn = sqlite3.connect('bank.db')

# 2.create cursor
cur = conn.cursor()

# 3.insert data
cur.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ('Alice', 1000))

# 4.Save changes
conn.commit()

# 5.Close connection
conn.close()