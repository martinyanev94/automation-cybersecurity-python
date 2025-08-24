def process_user_data(user_details):
    try:
        if not validate_email(user_details['email']):
            raise ValueError("Invalid email format.")
        if not validate_age(user_details['age']):
            raise ValueError("Invalid age.")
        
        # Process the valid data
        print("Processing user data...")

    except ValueError as e:
        print(f"Error: {e}")

# Example user data
user_data_invalid = {
    "email": "invalidemail",
    "age": 130
}

process_user_data(user_data_invalid)
