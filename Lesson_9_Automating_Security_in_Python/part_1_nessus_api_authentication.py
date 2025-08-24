import requests

# Configure Nessus API credentials
api_url = "https://your-nessus-server:8834"
username = "your	username"
password = "your_password"

# Create a session to authenticate
session = requests.Session()
login_payload = {"username": username, "password": password}
response = session.post(f"{api_url}/session", json=login_payload)

# Check if authentication was successful
if response.status_code == 200:
    print("Authentication successful!")
    token = response.json()["token"]
    headers = {"X-Cookie": f"token={token}"}
else:
    print(f"Failed to authenticate: {response.status_code}")
