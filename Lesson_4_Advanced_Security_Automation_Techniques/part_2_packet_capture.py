if __name__ == "__main__":
    print("Starting HTTP and DNS packet capture... Press CTRL+C to stop.")
    sniff(filter="tcp port 80 or udp port 53", prn=packet_callback, count=50)
