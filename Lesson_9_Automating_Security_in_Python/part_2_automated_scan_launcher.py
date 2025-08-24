# Create and launch a scan
scan_payload = {
    "uuid": "YOUR_SCAN_TEMPLATE_UUID",  # Replace with your scan template UUID
    "settings": {
        "name": "Automated Scan",
        "text_targets": "192.168.1.1,192.168.1.2",
    }
}
scan_response = session.post(f"{api_url}/scans", headers=headers, json=scan_payload)

# Check if the scan was created successfully
if scan_response.status_code == 200:
    print("Scan created successfully!")
    scan_id = scan_response.json()["scan"]["id"]
else:
    print(f"Failed to create scan: {scan_response.status_code}")
