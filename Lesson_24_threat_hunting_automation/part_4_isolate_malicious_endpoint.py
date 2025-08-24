def isolate_endpoint(ip_address):
    print(f'Isolating endpoint {ip_address}...')
    # Here we would include commands to integrate with our network management API
    # e.g., api.call_to_isolate(ip_address)
    print(f'Endpoint {ip_address} has been isolated.')

for user, data in enriched_logs.items():
    if data['threat_info'] and data['threat_info']['is_malicious']:
        isolate_endpoint(extract_ip_from_user(user))
