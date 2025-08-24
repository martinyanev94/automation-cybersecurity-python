import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    else:
        return False

# Test the function
print(validate_email("example@domain.com"))  # Should return True
print(validate_email("invalid-email.com"))    # Should return False
