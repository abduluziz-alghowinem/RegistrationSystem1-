import re
def passCheck():
    password = input("enter pass")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
        return True
    else:
        print("\npassword must contain A-Z,a-z,0-9 ... ")
        return False
print(passCheck())