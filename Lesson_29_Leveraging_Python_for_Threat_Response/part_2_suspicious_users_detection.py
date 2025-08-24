import pandas as pd

# Load security logs into a DataFrame
logs = pd.read_csv("security_logs.csv")

# Filter for failed login attempts
failed_logins = logs[logs['status'] == 'failed']

# Identifying users with multiple failures
potential_attackers = failed_logins['username'].value_counts()
suspicious_users = potential_attackers[potential_attackers > 5]

print("Suspicious users:", suspicious_users.index.tolist())
