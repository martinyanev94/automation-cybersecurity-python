def validate_user_details(user_details):
    if not validate_email(user_details.get('email')):
        return "Invalid email format."
    
    if not validate_age(user_details.get('age')):
        return "Invalid age."

    # Add more fields and their validations here

    return "All user details are valid."

# Example user data
user_data = {
    "email": "test@domain.com",
    "age": 30
}

print(validate_user_details(user_data))  # Should return "All user details are valid."
