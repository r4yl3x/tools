import argparse
import socket

def get_ip_address(domain_name):
  return socket.gethostbyname(domain_name)

def main():
  # Parse command-line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", help="file containing a list of domain names, one per line")
  parser.add_argument("-d", "--domains", nargs="+", help="list of domain names")
  parser.add_argument("-o", "--output", help="output file to save the results")
  args = parser.parse_args()

  # Get domain names from either the file or the command-line argument
  domain_names = []
  if args.file:
    # Read domain names from the file
    with open(args.file, "r") as f:
      for line in f:
        domain_names.append(line.strip())
  elif args.domains:
    # Get domain names from the command-line argument
    domain_names = args.domains

  # Get the IP addresses for each domain name
  results = {}
  for domain_name in domain_names:
    try:
      ip_address = get_ip_address(domain_name)
      results[domain_name] = ip_address
    except socket.gaierror:
      # domain_name could not be resolved
      pass

  # Print the results
  for domain_name, ip_address in results.items():
    print(f"{domain_name}: {ip_address}")

  # Save the results to the output file, if specified
  if args.output:
    with open(args.output, "w") as f:
      for domain_name, ip_address in results.items():
        f.write(f"{domain_name}: {ip_address}\n")

if __name__ == "__main__":
  main()
