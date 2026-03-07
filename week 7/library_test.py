#=========================================
# Library DB (PostgreSQL)
#=========================================
import psycopg2
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database = "library_db",
    user = "postgres",
    password = "9102004"
)

# create cursor
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS book(
#                id SERIAL PRIMARY KEY, 
#                title VARCHAR(100),
#                aurthor VARCHAR(100),
#                price NUMERIC
#                )""")



# print("Table created successfully")

# cursor.execute("INSERT INTO book(title, aurthor, price) VALUES(%s, %s, %s)",
#                ("Python Basic", "John", 20))

#Update data 
cursor.execute("UPDATE book SET price = %s where id = %s", (234,2))

# delet data
cursor.execute("DELETE FROM book WHERE id = %s", (2,))
conn.commit()
# read data
cursor.execute("SELECT * FROM book")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()