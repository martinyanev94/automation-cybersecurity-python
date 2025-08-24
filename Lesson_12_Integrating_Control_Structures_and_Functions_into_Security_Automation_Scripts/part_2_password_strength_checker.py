def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return False, "Password must include at least one digit."
    if not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."
    return True, "Password is strong."

password_input = input("Set your password: ")
strength_check, message = is_strong_password(password_input)
print(message)
