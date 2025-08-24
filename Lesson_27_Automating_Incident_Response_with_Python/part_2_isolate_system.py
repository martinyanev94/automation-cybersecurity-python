import subprocess

def isolate_system(ip_address):
    command = f"netsh advfirewall firewall add rule name='Isolate System' dir=OUT action=BLOCK remoteip={ip_address}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"System with IP {ip_address} has been isolated.")
    except subprocess.CalledProcessError as e:
        print(f"Error isolating system: {e}")
