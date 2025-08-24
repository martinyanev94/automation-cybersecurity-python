import logging

# Configure logging
logging.basicConfig(filename='security_automation_log.txt', level=logging.INFO)

def log_action(action):
    logging.info(f"Action performed: {action}")

def change_security_policy(policy):
    log_action(f"Changed security policy: {policy}")
    print(f"Security policy changed to: {policy}")

if __name__ == "__main__":
    new_policy = "Require MFA for all users"
    change_security_policy(new_policy)
