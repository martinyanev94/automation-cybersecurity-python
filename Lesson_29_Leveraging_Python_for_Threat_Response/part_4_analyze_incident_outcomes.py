incident_data = pd.read_csv("past_incidents.csv")

# Analyzing incident outcomes
successful_responses = incident_data[incident_data['outcome'] == 'success']
response_counts = successful_responses['response_type'].value_counts()

print("Most effective responses:")
print(response_counts)
