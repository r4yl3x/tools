import argparse
import socket

# Set up the argument parser
parser = argparse.ArgumentParser(description='Resolve IP addresses for a list of domain names')
parser.add_argument('-f', '--file', help='input file containing a list of domain names, one per line')
parser.add_argument('-d', '--domains', nargs='+', help='list of domain names')
parser.add_argument('-o', '--output', help='output file to store the results')

# Parse the command-line arguments
args = parser.parse_args()

# Read in the list of domain names
if args.file:
    # Read the domain names from the input file
    with open(args.file, 'r') as f:
        domains = f.read().splitlines()
elif args.domains:
    # Use the list of domain names provided as an argument
    domains = args.domains
else:
    print('Error: no input provided')
    exit(1)

# Open the output file for writing
with open(args.output, 'w') as f:
    # Iterate over the list of domain names
    for domain in domains:
        # Try to resolve the IP address for the domain name
        try:
            ip = socket.gethostbyname(domain)
            # Write the domain name and IP address to the output file
            f.write(f'{domain},{ip}\n')
            print(f'{domain},{ip}')
        except socket.gaierror:
            # If the domain name could not be resolved, write an error message to the output file
            f.write(f'{domain},ERROR\n')
            print(f'{domain},ERROR')
