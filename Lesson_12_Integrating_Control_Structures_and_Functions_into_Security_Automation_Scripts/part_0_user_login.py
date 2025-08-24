def login(username, password):
    correct_username = "admin"
    correct_password = "securePa55word!"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        
        if input_username == correct_username and input_password == correct_password:
            return "Access granted."
        else:
            attempts += 1
            print(f"Access denied. Attempt {attempts} of {max_attempts}.")
    
    return "Account locked due to too many failed attempts."

print(login("admin", "wrongPassword"))
