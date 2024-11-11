
import nmap
import pyfiglet

title = pyfiglet.figlet_format("PORT-SCANER")
print(title)


print("=" * 8)  # Adds a visual line for emphasis


scanner = nmap.PortScanner()


target_ip = input("Enter the target IP address: ")
port_range = input("Enter the port range (e.g., 1-1000): ")


print(f"Scanning {target_ip} for open ports in range {port_range}...")
scanner.scan(target_ip, port_range)


for host in scanner.all_hosts():
    print(f"\nHost: {host} ({scanner[host].hostname()})")
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"Port: {port}, State: {scanner[host][proto][port]['state']}")
