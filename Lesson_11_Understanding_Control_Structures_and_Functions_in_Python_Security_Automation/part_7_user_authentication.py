def authenticate_user(input_username, input_password):
    correct_username = "admin"
    correct_password = "securePa55word!"
    if input_username == correct_username and input_password == correct_password:
        return "Access granted."
    else:
        log_alert(f"Failed login attempt by user: {input_username}")
        return "Access denied."

username = input("Enter your username: ")
password = input("Enter your password: ")

print(authenticate_user(username, password))
