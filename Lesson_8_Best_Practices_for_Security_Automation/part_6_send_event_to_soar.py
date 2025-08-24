def send_event_to_soar(soar_api_url, api_token, event):
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.post(f"{soar_api_url}/events", json=event, headers=headers)

    if response.status_code == 200:
        print("Event sent to SOAR successfully.")
    else:
        print("Error sending event:", response.status_code)
