import csv
import subprocess
import argparse

def scan_ports(ip):
    try:
        print(f"[~] Scanning {ip}...")
        result = subprocess.run(
            ["nmap", "-Pn", "--top-ports", "1000", ip],
            capture_output=True,
            text=True,
            timeout=60
        )
        open_ports = []
        for line in result.stdout.splitlines():
            if "/tcp" in line and "open" in line:
                port = line.split("/")[0].strip()
                service = line.split()[-1]
                open_ports.append((port, service))
        return open_ports
    except Exception as e:
        print(f"[-] Error scanning {ip}: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV file with IPs")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        reader = csv.DictReader(f)
        targets = [row["ip"] for row in reader]

    with open("data/scan_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "port", "service"])
        for ip in targets:
            ports = scan_ports(ip)
            for port, service in ports:
                writer.writerow([ip, port, service])

    print("[✓] Scanning complete. Results saved to data/scan_results.csv")
