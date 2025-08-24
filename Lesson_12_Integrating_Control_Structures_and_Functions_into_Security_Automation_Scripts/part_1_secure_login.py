def secure_login():
    correct_username = "admin"
    correct_password = "securePa55word!"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            input_username = input("Enter your username: ")
            input_password = input("Enter your password: ")

            if not isinstance(input_username, str) or not isinstance(input_password, str):
                raise ValueError("Username and password must be strings.")

            if input_username == correct_username and input_password == correct_password:
                return "Access granted."
            else:
                attempts += 1
                print(f"Access denied. Attempt {attempts} of {max_attempts}.")
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
    
    return "Account locked due to too many failed attempts."

print(secure_login())
