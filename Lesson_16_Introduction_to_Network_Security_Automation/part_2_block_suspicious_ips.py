import ipaddress
import subprocess

def block_ip(ip):
    try:
        # Blocking the suspicious IP
        subprocess.run(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        print(f"IP {ip} has been blocked.")
    except Exception as e:
        print(f"Error blocking IP {ip}: {e}")

def detect_and_block():
    suspicious_ips = ["192.168.1.10", "10.0.0.5"]  # Example suspicious IPs
    for ip in suspicious_ips:
        block_ip(ip)

detect_and_block()
