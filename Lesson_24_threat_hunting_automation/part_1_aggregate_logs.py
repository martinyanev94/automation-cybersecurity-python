import os

def aggregate_logs(log_directory):
    all_logs = []
    
    for filename in os.listdir(log_directory):
        if filename.endswith(".log"):
            with open(os.path.join(log_directory, filename), 'r') as file:
                all_logs.extend(file.readlines())
    
    return all_logs

log_dir = '/path/to/logs/'
logs = aggregate_logs(log_dir)
print("Aggregated Logs:")
for log in logs:
    print(log.strip())
