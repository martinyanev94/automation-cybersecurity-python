bad_ips = ["192.0.2.1", "203.0.113.5"]

def packet_callback(packet):
    if IP in packet and packet[IP].dst in bad_ips:
        print(f"Alert! Packet to bad IP: {packet.summary()}")
    else:
        print(f"Packet captured: {packet.summary()}")
