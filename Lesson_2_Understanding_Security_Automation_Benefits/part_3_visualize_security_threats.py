import matplotlib.pyplot as plt

# Sample data
threat_types = ['Malware', 'Phishing', 'Unauthorized Access', 'Insider Threat']
threat_counts = [120, 200, 90, 30]

def visualize_threats(threat_types, threat_counts):
    plt.bar(threat_types, threat_counts, color='blue')
    plt.xlabel('Threat Types')
    plt.ylabel('Number of Incidents')
    plt.title('Security Incident Overview')
    plt.show()

if __name__ == "__main__":
    visualize_threats(threat_types, threat_counts)
