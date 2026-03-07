import psycopg2
import tkinter as tk
from tkinter import messagebox

#
conn = psycopg2.connect(
    host="localhost",
    database = "library_db",
    user = "postgres",
    password = "9102004",
    port = "5432"
)

cursor = conn.cursor()
#================Function================

def add_book():
    title = title_entry.get()
    author  = author_entry.get()
    year = year_entry.get()

    if title=="" or author=="" or year =="":
        messagebox.showerror("Error", "All fields are required")
        return
    
    cursor.execute("INSERT INTO books(title, author, year) VALUES(%s, %s, %s)", (title, author, year))
    conn.commit()
    messagebox.showinfo("Success", "Book Added")
    clear_fields()
    view_books()

def view_books():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)

def search_books():
    listbox.delete(0, tk.END)
    title = title_entry.get()
    
    cursor.execute("SELECT * FROM books WHERE title ILIKE %s", ('%'+title+'%',))
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)

def delete_book():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return
    book_id = selected[0]
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    messagebox.showinfo("Deleted", "Book removed")

    view_books()

def clear_fields():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

#====================GUI======================


window = tk.Tk()
window.title("Library Management System")
window.geometry("600x400")

# labels
tk.Label(window, text="Title").grid(row=0, column=0)
tk.Label(window, text="Author").grid(row=1, column=0)
tk.Label(window, text="Year").grid(row=2, column=0)

# Entry Fields
title_entry = tk.Entry(window)
title_entry.grid(row=0, column=1)
author_entry = tk.Entry(window)
author_entry.grid(row=1, column=1)
year_entry = tk.Entry(window)
year_entry.grid(row=2, column=1)

# Buttons
tk.Button(window, text="Add Book", width=12, command=add_book).grid(row=3, column=0)
tk.Button(window, text="View Books", width=12, command=view_books).grid(row=3, column=1)
tk.Button(window, text="Search Books", width=12, command=search_books).grid(row=3, column=2)
tk.Button(window, text="Delete Book", width=12, command=delete_book).grid(row=3, column=3)

# Listbox
listbox = tk.Listbox(window, width=80)
listbox.grid(row=4, column=0, columnspan=4)

window.mainloop()

cursor.close()
conn.close()
#================================================