import logging

# Setting up basic configuration for the logging
logging.basicConfig(filename='security_audit.log', level=logging.DEBUG)

def log_security_event(event):
    logging.info(event)

# Example event logging
log_security_event("User 'malicious_user' attempted unauthorized access.")
