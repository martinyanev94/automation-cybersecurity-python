import time

def monitor_logs(log_file):
    with open(log_file, 'r') as file:
        # Move to the end of the file
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)  # Sleep briefly if no new line
                continue
            if "ERROR" in line or "WARNING" in line:
                print(f"Suspicious log entry detected: {line.strip()}")

if __name__ == "__main__":
    log_file_path = '/var/log/system.log'  # Adjust log file path accordingly
    monitor_logs(log_file_path)
