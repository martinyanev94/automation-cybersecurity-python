import requests

response = requests.get("https://api.security-service.com/logs")

if response.status_code == 200:
    logs = response.json()
    print(f"Retrieved {len(logs)} logs.")
else:
    print("Failed to retrieve logs.")
