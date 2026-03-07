#===================================
# Python GUI Tools
#===================================
"""
Tkinter => Easy
PyQt    => Mediun => Professional apps
PySide  => Medium => Commericial apps
Kivy    => Medium => Mobile apps
wxPython=> Medium => Native destops apps
PySimpleGUI => Very Easy => Quick tools
"""
# Basic Tkinter structure
# 4. steps
# 1. Import tkinter
# 2. create main window
# 3. Add widgets (buttoms, labels, etc...)
# 4. Run application lopp

#=========== Example Tkinter =================
# step 1
import tkinter as tk

# step 2 - create window
window = tk.Tk()
window.title("My first App")
window.geometry("1000x1000")

# step 3 - widget

label = tk.Label(window, text = "Hello World!")
button = tk.Button(text="Click Me")
button.pack()
label.pack()

# step 4 - run app
window.mainloop()

# Common Tkinter wingets
"""
Label = Display text
Buttom = Clickable button
Entry = Text input
Text = Multiline Text
Frame = Container 
Checkbutton = Checkbox
Radiobutton = Option selection 
Menu = Menu Bar
"""
# Geometry Management (Layout)
"""
1. pack() - simple layout
2. grid() - rows & column  => label.grid(row=0, column=0) => button.grid(row=1, column=0)
3. place()- exact position
"""