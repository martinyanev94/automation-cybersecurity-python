import requests

def check_threat_intelligence(ip_address):
    api_url = f'https://threat-intel-api.com/ip/{ip_address}'
    response = requests.get(api_url)
    return response.json() if response.status_code == 200 else None

def enrich_suspicious_logins(suspicious_logins):
    enriched_data = {}
    
    for user, count in suspicious_logins.items():
        ip_address = extract_ip_from_user(user)
        threat_info = check_threat_intelligence(ip_address)
        enriched_data[user] = {'count': count, 'threat_info': threat_info}
    
    return enriched_data

def extract_ip_from_user(user):
    # Placeholder for a method to extract associated IPs for the user
    return "192.168.1.10"  # Example IP

enriched_logs = enrich_suspicious_logins(suspicious_logins)
print("Enriched Suspicious Logins:")
for user, data in enriched_logs.items():
    print(f"User: {user}, Info: {data}")
