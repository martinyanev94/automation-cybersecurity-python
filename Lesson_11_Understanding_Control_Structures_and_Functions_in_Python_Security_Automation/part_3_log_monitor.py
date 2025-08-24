for line in log_lines:
    if "logged in" in line:
        continue  # Skip lines that show a user has logged in
    for keyword in suspicious_keywords:
        if keyword in line:
            print(f"Alert: {keyword} found in log: {line}")
