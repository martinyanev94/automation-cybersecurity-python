import requests

def enrich_threat(ip_address):
    response = requests.get(f'https://api.threatintel.com/{ip_address}')
    if response.status_code == 200:
        return response.json()  # Return enriched threat info
    else:
        return None

# Example usage
threat_info = enrich_threat('192.168.1.10')
if threat_info:
    print("Threat Info:", threat_info)
else:
    print("No threat data found.")
