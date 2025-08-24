import pandas as pd

def generate_incident_report(file_path):
    incidents = pd.read_csv(file_path)
    
    total_incidents = len(incidents)
    unresolved_incidents = incidents[incidents['resolution_status'] == 'unresolved']

    print(f"Total Incidents: {total_incidents}")
    print(f"Unresolved Incidents: {len(unresolved_incidents)}")
    print("Incident Details:")
    print(unresolved_incidents[['timestamp', 'severity', 'description']])
