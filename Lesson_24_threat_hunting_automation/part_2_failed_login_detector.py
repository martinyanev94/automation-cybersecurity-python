def detect_failed_logins(logs):
    failed_login_count = {}
    
    for log in logs:
        if "failed login" in log:
            user = extract_user_from_log(log)
            if user in failed_login_count:
                failed_login_count[user] += 1
            else:
                failed_login_count[user] = 1

    return {user: count for user, count in failed_login_count.items() if count > 5}

def extract_user_from_log(log):
    # Assuming the log is in the format: "<timestamp> <user> failed login"
    return log.split()[1]

suspicious_logins = detect_failed_logins(logs)
print("Suspicious Logins Detected:")
for user, count in suspicious_logins.items():
    print(f"User: {user}, Failed Login Attempts: {count}")
