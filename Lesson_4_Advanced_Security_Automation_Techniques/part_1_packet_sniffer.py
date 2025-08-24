from scapy.all import sniff

def packet_callback(packet):
    print(f"Packet captured: {packet.summary()}")

if __name__ == "__main__":
    print("Starting packet capture... Press CTRL+C to stop.")
    sniff(prn=packet_callback, count=10)  # Capture 10 packets
