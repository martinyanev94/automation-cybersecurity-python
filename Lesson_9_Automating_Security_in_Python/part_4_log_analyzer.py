import os
import re

# Configuration
log_directory = '/var/log/security'
alert_keywords = ['unauthorized', 'failed login', 'error']

def analyze_logs(directory):
    alert_patterns = [re.compile(keyword, re.IGNORECASE) for keyword in alert_keywords]

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line in f:
                    for pattern in alert_patterns:
                        if pattern.search(line):
                            print(f"Alert: {line.strip()} in file {file_path}")

if __name__ == "__main__":
    analyze_logs(log_directory)
