failed_attempts = 0

def register_failed_attempt():
    global failed_attempts
    failed_attempts += 1

# Simulating failed login attempts
for _ in range(3):
    register_failed_attempt()

print(f"Total failed login attempts: {failed_attempts}")
