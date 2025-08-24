def is_username_secure(username):
    if len(username) < 8:
        return False
    else:
        return True

print(is_username_secure("user123"))  # Returns False
print(is_username_secure("user12345"))  # Returns True
