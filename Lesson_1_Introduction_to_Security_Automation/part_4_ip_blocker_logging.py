import logging

# Configure logging
logging.basicConfig(filename='automation_log.txt', level=logging.INFO)

def log_action(action):
    logging.info(f"Action performed: {action}")

def block_ip(ip_address):
    # Log blocking action
    log_action(f"Blocking IP address: {ip_address}")
    # Here you would add the logic to block the IP address

if __name__ == "__main__":
    # Example use
    block_ip("192.168.1.15")
