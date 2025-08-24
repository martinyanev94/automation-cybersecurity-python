def secure_authentication(username, password):
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        credentials_username = input("Enter your username: ")
        credentials_password = input("Enter your password: ")

        result = authenticate_user(credentials_username, credentials_password)
        if result == "Access granted.":
            return result
        else:
            attempts += 1
            print(f"{result} Attempt {attempts} of {max_attempts}.")

    return "Account locked due to too many failed attempts."

print(secure_authentication("user1", "Password123"))
