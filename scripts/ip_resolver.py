import socket
import csv
import argparse

def resolve_ips(input_file):
    ip_results = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row["subdomain"]
            try:
                ip = socket.gethostbyname(domain)
                ip_results.append({"domain": domain, "ip": ip})
                print(f"[+] {domain} -> {ip}")
            except Exception as e:
                print(f"[-] Failed to resolve {domain}: {e}")
    return ip_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV file with subdomains")
    args = parser.parse_args()

    results = resolve_ips(args.input)

    with open("data/ips.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["domain", "ip"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"[✓] Saved {len(results)} IPs to data/ips.csv")
