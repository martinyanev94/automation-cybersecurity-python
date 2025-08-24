import csv

def log_alert(src_ip, city, country):
    with open('alerts_log.csv', mode='a', newline='') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([time.ctime(), src_ip, city, country])  # Log timestamp, IP, and location

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        country, city = get_geolocation(src_ip)
        log_alert(src_ip, city, country)  # Log the alert
        print(f"Packet from {src_ip} - Location: {city}, {country}")

if __name__ == "__main__":
    print("Starting packet capture and alert logging... Press CTRL+C to stop.")
    sniff(prn=packet_callback)
