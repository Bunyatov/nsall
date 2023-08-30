import sys
import ipaddress
import socket
import argparse

def generate_hostname_list(cidr, verbose=False):
    try:
        ip_network = ipaddress.IPv4Network(cidr, strict=False)
        for ip in ip_network:
            try:
                hostname, _, _ = socket.gethostbyaddr(str(ip))
                if verbose:
                    print(f"{ip} {hostname}")
                else:
                    print(hostname)
            except socket.herror:
                # If the lookup fails, continue to the next IP address
                continue
    except ValueError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Resolve and print unique hostnames from a CIDR block")
    parser.add_argument("cidr", help="CIDR block to scan for hostnames")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print IP address along with hostname")
    args = parser.parse_args()

    generate_hostname_list(args.cidr, args.verbose)

if __name__ == "__main__":
    main()