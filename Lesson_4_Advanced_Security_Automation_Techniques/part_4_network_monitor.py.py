from collections import defaultdict
import time

connection_attempts = defaultdict(int)

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        connection_attempts[src_ip] += 1
        
        if connection_attempts[src_ip] > 5:  # Threshold for alert
            print(f"Alert! Excessive connections from: {src_ip}")
            connection_attempts[src_ip] = 0  # Reset after alerting

if __name__ == "__main__":
    print("Starting network monitoring... Press CTRL+C to stop.")
    while True:
        sniff(prn=packet_callback, count=0)  # Capture indefinitely
