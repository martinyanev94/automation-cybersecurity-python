username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "securePa55word!":
    print("Access granted.")
elif username == "admin":
    print("Incorrect password.")
else:
    print("User not found.")
