# Recon Automation Scripts

Automated scripts for reconnaissance phase in web pentesting.

## 📂 Scripts

- `subdomain_enum.py`: Get subdomains using VirusTotal API.
- `ip_resolver.sh`: Resolve IPs from subdomains.
- `port_scanner.py`: Scan top 1000 ports using Nmap.

## 🛠 Requirements
- Python 3
- VirusTotal API key
- nmap

## 🚀 Usage

```bash
python3 scripts/subdomain_enum.py --domain example.com
bash scripts/ip_resolver.sh subdomains.csv
python3 scripts/port_scanner.py --input ips.csv
