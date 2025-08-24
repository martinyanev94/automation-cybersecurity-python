import requests

def check_failed_login_attempts(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        logins = response.json()
        for attempt in logins:
            if attempt['status'] == 'failed':
                handle_failed_login(attempt)

def handle_failed_login(attempt):
    print(f"Failed login attempt detected from IP: {attempt['ip_address']}")
    # Trigger an alert or block the IP as a response
    block_ip(attempt['ip_address'])

def block_ip(ip_address):
    print(f"Blocking IP address: {ip_address}")
    # Here you would add the logic to block the IP address

if __name__ == "__main__":
    api_url = 'http://your-sever/api/login-attempts'
    check_failed_login_attempts(api_url)
