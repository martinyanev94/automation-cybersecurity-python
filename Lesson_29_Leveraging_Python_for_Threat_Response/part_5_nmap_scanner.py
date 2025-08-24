import nmap

def scan_hosts(ip_range):
    nm = nmap.PortScanner()
    nm.scan(ip_range, arguments='-sV')  # Version detection
    return nm.all_hosts()

# Example: Scanning a specific IP range
hosts = scan_hosts("192.168.1.0/24")
print("Scanned hosts:", hosts)
