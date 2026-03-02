#==================== Read data ====================
import sqlite3

# 1.connect to database
conn = sqlite3.connect('bank.db')

# 2.create cursor
cur = conn.cursor()

# 3.read data
cur.execute("SELECT * FROM accounts")

# 4.fetch data
rows = cur.fetchall()

for row in rows:
    print(row)

# # Update data
# cur.execute("UPDATE accounts SET balance = ? WHERE name = ?", (15000, 'Alice'))

# # Delete data
# cur.execute("DELETE FROM accounts WHERE name = ?", ('Alice',))
# # 4.Save changes
# conn.commit()

# 5.Close connection
conn.close() 

'''
cursor.execute()        => run sql
cursor.fetchall()       => get all data
cursor.fetchone()       => get one data
cursor.fetchmany(n)    => get n data
'''