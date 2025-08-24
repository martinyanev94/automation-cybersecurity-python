def log_alert(alert_message):
    with open("security_alerts.txt", "a") as file:
        file.write(f"{alert_message}\n")

log_alert("Failed login attempt detected.")
log_alert("Unauthorized access attempt on admin panel.")
