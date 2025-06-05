import requests
import argparse
import csv

def get_subdomains(domain, apikey):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}/subdomains"
    headers = {"x-apikey": apikey}
    subdomains = []

    while url:
        r = requests.get(url, headers=headers)
        data = r.json()
        for item in data.get("data", []):
            subdomains.append(item["id"])
        url = data.get("links", {}).get("next", None)

    return subdomains

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--apikey", required=True)
    args = parser.parse_args()

    subdomains = get_subdomains(args.domain, args.apikey)

    with open("data/subdomains.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["subdomain"])
        for sub in subdomains:
            writer.writerow([sub])

    print(f"[+] Saved {len(subdomains)} subdomains to data/subdomains.csv")