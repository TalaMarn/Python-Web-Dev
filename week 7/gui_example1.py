import tkinter as tk

def say_hello():
    print("Hello!")
"""
window = tk.Tk()

button = tk.Button(window, text= "Click Me", command = say_hello)
button.pack()

window.mainloop()"""

window = tk.Tk()
window.title("Login Page")
tk.Label(window, text= "Username").pack()
user= tk.Entry(window).pack()

tk.Label(window, text="Password").pack()
tk.Entry(window, show="*").pack()

tk.Button(window, text="Login", command=say_hello).pack()

window.mainloop()