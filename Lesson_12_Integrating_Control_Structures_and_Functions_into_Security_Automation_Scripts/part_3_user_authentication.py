users_db = {}

def add_user(username, password):
    valid, message = is_strong_password(password)
    if valid:
        users_db[username] = password
        return f"User '{username}' added successfully."
    else:
        return message

def authenticate_user(username, password):
    if username in users_db and users_db[username] == password:
        return "Access granted."
    return "Access denied."

print(add_user("user1", "Password123"))
print(authenticate_user("user1", "Password123"))
