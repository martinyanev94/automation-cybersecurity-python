def analyze_logs(logs):
    for log in logs:
        if "Unauthorized access" in log:
            respond_to_incident(log)

def respond_to_incident(log):
    print(f"Automated Response: Investigating incident - {log}")

if __name__ == "__main__":
    system_logs = [
        "User login from authorized IP",
        "Unauthorized access attempt detected",
        "Data access request from IP 192.168.1.100"
    ]

    analyze_logs(system_logs)
