import requests

def get_geolocation(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    return data.get('country', 'unknown'), data.get('city', 'unknown')

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        country, city = get_geolocation(src_ip)
        print(f"Packet from {src_ip} - Location: {city}, {country}")

if __name__ == "__main__":
    print("Starting packet capture with geolocation... Press CTRL+C to stop.")
    sniff(prn=packet_callback)
