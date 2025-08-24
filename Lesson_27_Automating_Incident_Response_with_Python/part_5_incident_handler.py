def handle_incident(ip_address, file_path):
    # Step 1: Send Alert
    send_alert('security_team@example.com', 'Suspicious activity detected!')
    
    # Step 2: Isolate System
    isolate_system(ip_address)
    
    # Step 3: Delete Malicious File
    delete_malicious_file(file_path)
    
    # Step 4: Generate Incident Report
    generate_incident_report('incident_log.csv')

# Example usage
handle_incident('192.168.1.10', 'C:\\path_to_malicious_file.exe')
