suspicious_keywords = ["failed login", "unauthorized access", "malware detected"]
log_lines = [
    "2023-01-01 12:00:00: User admin failed login",
    "2023-01-01 12:01:00: User guest logged in",
    "2023-01-01 12:02:00: Malware detected on server",
]

for line in log_lines:
    for keyword in suspicious_keywords:
        if keyword in line:
            print(f"Alert: {keyword} found in log: {line}")
