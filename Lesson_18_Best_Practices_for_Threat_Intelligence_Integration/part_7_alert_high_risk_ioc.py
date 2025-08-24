def alert_security_team(enriched_data):
    for item in enriched_data:
        if item['risk_level'] == "High":
            print(f"ALERT: High-risk IOC detected - {item['ioc'].display_info()}. Immediate action required!")
