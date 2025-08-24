import requests

def enrich_alert(ip_address):
    url = f"https://api.threatintelligenceplatform.com/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return enriched data
    else:
        return {"error": "Enrichment failed"}
