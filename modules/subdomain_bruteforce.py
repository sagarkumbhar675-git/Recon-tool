import socket
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return (full_domain, ip)
    except:
        return None

def brute_force(domain, wordlist_path, threads=50):
    print(f"[+] Starting subdomain brute force on {domain}")
    
    found = []

    try:
        with open(wordlist_path, "r") as f:
            subdomains = [line.strip() for line in f]
    except:
        print("[-] Wordlist not found!")
        return

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda sub: check_subdomain(sub, domain), subdomains)

    for result in results:
        if result:
            print(f"[FOUND] {result[0]} -> {result[1]}")
            found.append({"subdomain": result[0], "ip": result[1]})

    print(f"[+] Total Found: {len(found)}")
