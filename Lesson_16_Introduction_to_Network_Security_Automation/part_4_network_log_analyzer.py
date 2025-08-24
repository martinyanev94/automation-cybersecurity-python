import logging
import re

# Configure the logger
logging.basicConfig(filename='network_activity.log', level=logging.INFO)

def analyze_logs(log_entry):
    if re.search(r'failed login', log_entry):
        alert_security_team()
        
    logging.info(log_entry)

def log_activity(activity):
    analyze_logs(activity)

# Simulating log entries
log_activity("User admin failed login attempt from 192.168.1.10")
log_activity("User admin successfully logged in from 192.168.1.15")
