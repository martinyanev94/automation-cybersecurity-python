import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sS')
    
    for host in nm.all_hosts():
        print(f"Scanning host: {host}" )
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port} is {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target = '192.168.1.0/24'  # Specify the network to scan
    scan_network(target)
