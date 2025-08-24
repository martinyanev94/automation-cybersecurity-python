import re

def parse_logs(log_file):
    alerts = []
    with open(log_file, 'r') as file:
        for line in file:
            if "ERROR" in line:
                match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)', line)
                if match:
                    timestamp, error_message = match.groups()
                    alerts.append((timestamp, error_message))
    return alerts

def alert_security_team(alerts):
    for alert in alerts:
        print(f"Alert: {alert[1]} detected at {alert[0]}")
        
log_file_path = 'system_logs.txt'
detected_alerts = parse_logs(log_file_path)
if detected_alerts:
    alert_security_team(detected_alerts)
