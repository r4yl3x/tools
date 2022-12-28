import argparse
import socket

# Define a function to resolve the IP addresses for a list of domain names
def get_ip_addresses(domains):
    # Create a list to store the results
    results = []
    # Iterate over the list of domain names
    for domain in domains:
        # Try to resolve the IP address for the domain name
        try:
            ip = socket.gethostbyname(domain)
            # Add the domain name and IP address to the results list
            results.append((domain, ip))
        except socket.gaierror:
            # If the domain name could not be resolved, add an error message to the results list
            results.append((domain, 'ERROR'))
    return results

# Create a parser object to handle command-line arguments
parser = argparse.ArgumentParser(description='Resolve IP addresses for a list of domain names')

# Add arguments to the parser
parser.add_argument('-f', '--file', help='a file containing a list of domain names, one per line')
parser.add_argument('-d', '--domains', nargs='+', help='a list of domain names')

# Parse the command-line arguments
args = parser.parse_args()

# Check if the user specified a file or a list of domain names
if args.file:
    # Read in the list of domain names from the specified file
    with open(args.file, 'r') as f:
        domains = f.read().splitlines()
else:
    # Use the list of domain names provided as an argument
    domains = args.domains

# Resolve the IP addresses for the list of domain names
results = get_ip_addresses(domains)

# Open the output file for writing
with open('iplist.txt', 'w') as f:
    # Iterate over the results and write them to the output file
    for domain, ip in results:
        f.write(f'{domain},{ip}\n')

# Print the results to the console
for domain, ip in results:
    print(f'{domain}: {ip}')
