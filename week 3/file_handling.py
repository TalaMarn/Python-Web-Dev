# Working with file
# File Read example
#===============================

# Reading Whole File
file = open("student.txt", "r")

for line in file:
    print(line)
input("Press Enter to continue...")
file.close()

while True:
    print("This won't print")
    break
""" Open modes:
"r"  -> read
"w"  -> write (overwrite)
"a"  -> append
"x"  -> create file
"""