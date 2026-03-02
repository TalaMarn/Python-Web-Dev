import sqlite3

# 1.connect to database
def connect():
    return sqlite3.connect("app.db")

# 2.create table
def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     price REAL
            )
        """)

# 3.insert product
def insert_product(name, price):
    with connect() as conn:
        conn.execute("""
                     INSERT INTO products (name, price) VALUES (?, ?)
        """, (name, price))

# 4.get products
def get_products():
    with connect() as conn:
        return conn.execute("SELECT * FROM products").fetchall()

create_table()
insert_product("Laptop", 999.99)
print(get_products())