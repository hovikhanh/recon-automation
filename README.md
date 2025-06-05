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
python scripts/subdomain_enum.py --domain example.com --apikey YOUR_KEY

python scripts/ip_resolver.py --input data/subdomains.csv

python scripts/port_scanner.py --input data/ips.csv
