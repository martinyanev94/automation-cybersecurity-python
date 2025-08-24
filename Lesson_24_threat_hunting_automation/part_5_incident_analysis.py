import pandas as pd

def analyze_incident_data(incident_data):
    df = pd.DataFrame(incident_data)
    summary = df.groupby('threat_type').count()
    print(summary)

previous_incidents = [
    {'threat_type': 'malware', 'timestamp': '2023-01-01'},
    {'threat_type': 'phishing', 'timestamp': '2023-01-02'},
    {'threat_type': 'malware', 'timestamp': '2023-01-03'}
]

analyze_incident_data(previous_incidents)
