import dns.resolver
import re
import os.path
import sys
import getopt
import argparse
import time 

class Scanner:
    def __init__(self):
        self.domain = ""
        self.wordlist = ""
        self.output_file = ""
        self.delay = 0
        self.skip_duplicates = False
        self.combine = False
        self.combine_values = []

    
    def validate_domain(self, domain):
        try:
            validation = re.search(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]", domain).group()
        except:
            print("Domain is not valid!")
            validation = False
        return validation

    def validate_wordlist_exists(self, wordlist_path):
        if os.path.isfile(wordlist_path):
            return True
        else:
            print("Wordlist file not exists...\nClosing!")
            return False

    def check_dns_entry(self, domain_to_check):
        try:
            result = dns.resolver.resolve(domain_to_check, 'A')
            for ipval in result:
                return ipval.to_text()
        except:
            print("Error - domain does not exists")
            sys.exit()

    def f_word(self, path):
        try:
            o_file = open(path, "r")
        except:
            print("Error while opening file")
            sys.exit()
        return o_file

def main():
    parser = argparse.ArgumentParser()
    scanner = Scanner()

    required_group = parser.add_argument_group(title='Required arguments')
    required_group.add_argument('-d', '--domain', help="Target domain to scan", required=True)
    required_group.add_argument('-w', '--wordlist', help="Absolute path to dictionary", required=True)
    
    parser.add_argument('-o', '--output', help="Path to output file for storing results")
    parser.add_argument('-s', '--skip', help="Skip duplicates (like same IP as wildcard one)", action="store_true")
    #parser.add_argument('-c', '--combine', help="Combine words from dictionary for results like qa.ftp.domain.com", action="store_true")
    parser.add_argument('-t', '--timedelay', help="Set delay in seconds for limiting reqesting")

    args = parser.parse_args()

    if scanner.validate_domain(args.domain) != False:
        scanner.domain = args.domain
    else:
        sys.exit()

    if scanner.validate_wordlist_exists(args.wordlist) != False:
        scanner.wordlist = args.wordlist
    else:
        sys.exit()

    if args.output:
        scanner.output_file = args.output

    if args.skip:
        scanner.skip_duplicates = True

    if args.timedelay:
        scanner.delay = args.timedelay
        
    #if args.combine:
    #    scanner.combine = True

    print("Starting querying to DNS...\n")
    print(scanner.domain)
    first_result = scanner.check_dns_entry(scanner.domain)
    print(first_result + "\n")

    f_word = scanner.f_word(scanner.wordlist)
    
    num_lines = f_word.readlines()

    for line in num_lines:
        line = line.strip()
        conc_domain = line + "." + scanner.domain

        #if scanner.combine == True:
        #    scanner.combine_values.append(line)

        if scanner.delay != 0:
            time.sleep(int(scanner.delay))
            
        result = scanner.check_dns_entry("*." + conc_domain)

        if result == first_result:
            if scanner.skip_duplicates != True:
                print(conc_domain + "\n" + result + " [!] SAME IP AS " + scanner.domain)
        else:
            print(conc_domain + "\n" + result + "\n")

    f_word.close()
    #print(scanner.combine_values)

if __name__ == "__main__":
    main()