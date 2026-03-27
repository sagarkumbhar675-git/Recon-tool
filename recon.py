import argparse
from modules.subdomain_bruteforce import brute_force

def main():
    parser = argparse.ArgumentParser(description="Recon Tool")

    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--subdomains", action="store_true", help="Run subdomain brute force")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Wordlist path")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Threads")

    args = parser.parse_args()

    print(f"\n[+] Target: {args.domain}\n")

    if args.subdomains:
        brute_force(args.domain, args.wordlist, args.threads)

if __name__ == "__main__":
    main()
