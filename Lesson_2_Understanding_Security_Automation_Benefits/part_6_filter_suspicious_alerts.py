def is_suspicious(alert):
    # Simple filtering logic that takes into account known patterns
    return "alert" in alert.lower()  # Example condition for filtering

if __name__ == "__main__":
    alerts = ["Unauthorized access attempt", "Normal user login", "Potential threat detected", "User logged out normally"]

    filtered_alerts = [alert for alert in alerts if is_suspicious(alert)]
    print("Suspicious alerts:", filtered_alerts)
