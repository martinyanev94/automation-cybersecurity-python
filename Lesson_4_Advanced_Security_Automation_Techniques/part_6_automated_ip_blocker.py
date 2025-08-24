import os

def block_ip(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")
    print(f"Blocked IP: {ip}")

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        connection_attempts[src_ip] += 1

        if connection_attempts[src_ip] > 5:
            block_ip(src_ip)  # Automatically block the IP
            connection_attempts[src_ip] = 0

if __name__ == "__main__":
    print("Starting automated actions for network monitoring... Press CTRL+C to stop.")
    sniff(prn=packet_callback)
