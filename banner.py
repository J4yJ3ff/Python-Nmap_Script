import nmap

def banner_grabbing(target_ip, target_ports):
    # Create a new Nmap PortScanner object
    nm = nmap.PortScanner()

    # Perform a simple banner grabbing scan on the specified ports
    for port in target_ports:
        nm.scan(target_ip, str(port), arguments='-sV')

    # Extract and print banner information
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            if proto == 'tcp':
                print(f"Banner information for {host}:")

                for port, port_info in nm[host][proto].items():
                    if 'product' in port_info:
                        print(f"  Port {port}/{proto}:")
                        print(f"    Service: {port_info['name']} ({port_info['product']})")
                        print(f"    Version: {port_info['version']}")

if __name__ == "__main__":
    target_ip = "195.201.179.80"  # Replace with the target IP address
    target_ports = [80, 443, 22]  # Specify the target ports for banner grabbing

    banner_grabbing(target_ip, target_ports)

