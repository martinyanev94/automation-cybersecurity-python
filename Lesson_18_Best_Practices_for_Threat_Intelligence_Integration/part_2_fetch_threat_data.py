import requests

def fetch_threat_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()  # Returns the response as a JSON object
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
