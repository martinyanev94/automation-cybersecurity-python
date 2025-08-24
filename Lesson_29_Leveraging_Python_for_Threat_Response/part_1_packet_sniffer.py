from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"Source: {ip_src}, Destination: {ip_dst}")
        if is_suspicious(ip_src):  # Hypothetical function to check for suspicious IPs
            block_ip(ip_src)  # Block IP if suspicious

sniff(filter="ip", prn=packet_callback, store=0)
