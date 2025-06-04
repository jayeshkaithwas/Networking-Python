import requests
import json

def get_subdomains(domain, timeout):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Error: {e}")
        return []

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("[!] Failed to decode JSON.")
        return []

    subdomains = set()
    for entry in data:
        name_value = entry.get('name_value', '')
        for subdomain in name_value.split('\n'):
            if subdomain.endswith(domain):
                subdomains.add(subdomain.strip())

    return sorted(subdomains)

def main():
    domain = input("Enter the domain (e.g., example.com): ").strip()
    timeout_input = input("Enter timeout in seconds (default: 10): ").strip()
    timeout = int(timeout_input) if timeout_input else 10

    print(f"[*] Fetching subdomains for: {domain} with timeout {timeout}s")
    subdomains = get_subdomains(domain, timeout)

    if subdomains:
        print(f"\n[+] Found {len(subdomains)} unique subdomains:")
        for subdomain in subdomains:
            print(subdomain)

        save_to_file = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
        if save_to_file == 'y':
            filename = input("Enter filename (e.g., subdomains.txt): ").strip()
            try:
                with open(filename, 'w') as f:
                    for subdomain in subdomains:
                        f.write(subdomain + '\n')
                print(f"[+] Subdomains saved to: {filename}")
            except IOError as e:
                print(f"[!] Error writing to file: {e}")
    else:
        print("[!] No subdomains found.")

if __name__ == "__main__":
    main()
