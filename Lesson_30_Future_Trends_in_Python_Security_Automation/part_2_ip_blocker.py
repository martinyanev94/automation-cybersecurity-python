import requests

def block_ip(ip_address):
    # Hypothetical API call to block an IP
    response = requests.post('https://api.firewall.com/block', json={'ip': ip_address})
    if response.status_code == 200:
        print(f"Blocked IP: {ip_address}")
    else:
        print("Failed to block the IP.")

def automate_response(suspicious_ips):
    for ip in suspicious_ips:
        block_ip(ip)

# Example usage with previously identified suspicious IPs
suspicious_ips = ['192.168.1.10', '192.168.1.15']
automate_response(suspicious_ips)
