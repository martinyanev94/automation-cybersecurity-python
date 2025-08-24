def validate_age(age):
    if isinstance(age, int) and 0 <= age <= 120:
        return True
    else:
        return False

# Test cases
print(validate_age(25))  # Should return True
print(validate_age(-5))  # Should return False
print(validate_age(130))  # Should return False
print(validate_age("twenty-five"))  # Should return False
