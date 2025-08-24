python -m venv opencti-env
source opencti-env/bin/activate  # For Linux or Mac
opencti-env\Scripts\activate     # For Windows
pip install requests
import requests

def get_latest_observables(api_url, api_token):
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(f"{api_url}/observables", headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns the latest observables as JSON
    else:
        print("Error retrieving observables:", response.status_code)
