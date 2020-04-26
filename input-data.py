
# Everything recieve is string
"""
fullname = input("Enter your name:")
#Convert string to int
age = int(input("Enter your age:"))
print(fullname)
print(age+5)
"""


user = input("Enter Username:")
pwd = input("Enter Password:")
set_user = "admin"
set_pass = "1234"

# if user == "admin" and pwd == "1234":
if user == set_user and pwd == set_pass:
    print("yeh!! Login Success")
else:
    print("Opp!! Login fail")
