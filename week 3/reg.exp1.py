import re
"""
re.search()
re.match()
re.findall()
re.finditer()
re.sub()
re.split()
"""

# Extract HTML tags (Lazy vs Greedy)
text = "<b>Hello</b> <i>World</i>"

print(re.findall(r"<.*?>", text))  # Lazy matching
print(re.findall(r"<.*>", text))   # Greedy matching

# Extract IP Addresses
text = "Server IPs: 192.168.1.1, 10.0.0.1, 10.0.0.5"
ips = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", text)
print(ips)

# text = "marks: 45, 78, 89, 90"
# #result = re.search(r"Python", text)
# result = re.findall(r"\d+", text)
# print(result)









# text = " apple, banana; orange"
# # new_text = re.sub("\d", "*", text)
# new_text2 = re.split("[,;]", text)
# pattern = r"(09\d{8})"
# match = re.search(pattern, text)
# print(new_text2)

### [abc]
### [a-z]
### [A-Z]
### [0-9]
### \d = ([0-9])
### \D = Non-digit character
### \w = letter, digit, underscore
### \W = Non-word character
### \s = space, tab, newline
### \S = Non-space character
### . = any character except newline
# * = 0 or more
# + = 1 or more
# ? = 0 or 1
# {n} = exactly n
# {n,} = n or more
# {n,m} = between n and m
### ^ = start of string
### $ = end of string