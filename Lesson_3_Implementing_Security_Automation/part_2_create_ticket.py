import requests

def create_ticket(incident_details):
    url = "https://your-ticketing-system.com/api/tickets"
    headers = {"Authorization": "Bearer YOUR_API_TOKEN", "Content-Type": "application/json"}
    data = {"title": incident_details['title'], "description": incident_details['description']}
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print("Ticket created successfully.")
    else:
        print("Failed to create ticket:", response.content)

if __name__ == "__main__":
    incident = {"title": "Malware detected", "description": "Detected malware on server."}
    create_ticket(incident)
