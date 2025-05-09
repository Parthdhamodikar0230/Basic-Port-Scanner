import socket
import nmap

def socket_scan(ip, ports):
    print(f"[+] Socket Port Scan on {ip}")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"    [OPEN] Port {port} (Socket)")
            s.close()
        except Exception as e:
            print(f"    Error on port {port}: {e}")

def nmap_scan(ip):
    print(f"[+] Nmap Scan on {ip}")
    scanner = nmap.PortScanner()
    scanner.scan(ip, '1-1000')
    for proto in scanner[ip].all_protocols():
        ports = scanner[ip][proto].keys()
        for port in sorted(ports):
            state = scanner[ip][proto][port]['state']
            print(f"    [NMAP] Port {port} is {state}")

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")

    print("\n=== Starting Port Scans ===\n")
    socket_scan(target_ip, [22, 80, 443, 9999])  # Add 9999 for testing with netcat
    nmap_scan(target_ip)
