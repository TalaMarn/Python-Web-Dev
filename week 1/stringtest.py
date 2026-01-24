# Python Development
#--------------------------
# string test
#--------------------------
# example 1

name = "Aung Aung"
title = 'Software Engineer'

# example 2
email_template = """Dear Student,

Your Python class starts tomorrow at 9:00 AM.
Please be on time.

Regards,
Training Team
"""

# example 3
text = "python"
print(type(text))

# example 4
language = "python"
language = "J" + language[1:]

# string[start:end:step]

# f-string example
user = "Htet Min"
role = "Student"

message = f"Hello {user}, your role is {role}."
print(message)

# login validation example
def validate_login(username, password):
    username = username.strip().lower()

    if not username:
        return "Username required"

    if len(password) < 8:
        return "Password too short"

    if not password.isalnum():
        return "Password must be alphanumeric"

    return "Login successful"


print(validate_login(" Admin ", "Python123"))

