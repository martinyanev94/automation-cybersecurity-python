def block_ip(ip_address):
    url = "https://api.firewall.com/block_ip"
    payload = {'ip': ip_address}
    response = requests.post(url, json=payload)
    return response.status_code == 200  # Returns True if successfully blocked

# Example usage
if predictions.count(-1) > 10:  # If there are several anomalies
    for ip in suspicious_ips:
        block_ip(ip)
