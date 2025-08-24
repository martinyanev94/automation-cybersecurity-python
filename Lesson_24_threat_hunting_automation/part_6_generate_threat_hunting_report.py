import csv

def generate_report(data, filename='threat_hunting_report.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['User', 'Threat Count', 'Threat Info'])
        for user, info in data.items():
            writer.writerow([user, info['count'], info['threat_info']])

generate_report(enriched_logs)
print("Report generated and saved.")
