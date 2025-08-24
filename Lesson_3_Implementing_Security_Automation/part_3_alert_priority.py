class Alert:
    def __init__(self, message, severity):
        self.message = message
        self.severity = severity

def filter_alerts(alerts):
    return sorted(alerts, key=lambda x: x.severity, reverse=True)

if __name__ == "__main__":
    alerts = [
        Alert("Unusual login attempt", 5),
        Alert("Malware detected", 8),
        Alert("Password change request", 2),
        Alert("Firewall breach", 9)
    ]

    prioritized_alerts = filter_alerts(alerts)

    for alert in prioritized_alerts:
        print(f"Severity: {alert.severity} - Message: {alert.message}")
