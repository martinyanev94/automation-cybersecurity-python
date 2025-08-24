def is_password_strong(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

user_password = input("Set your password: ")
if is_password_strong(user_password):
    print("Password is strong.")
else:
    print("Password is weak; consider using at least 8 characters with upper letters and numbers.")
