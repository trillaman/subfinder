# subfinder
Python script to find subdomains omitting wildcard and for some programming practice

## Goal
Primary goal was to have handy tool which using wordlists and asking DNS for entries omitting wildcards in DNS entries by moving "*" one level left.

*EXAMPLE*\
If domain has entry like *.google.com then every DNS query will be pointing to same IP, but if we create query like this *.old.google.com then it will provide IP that is actually pointing where we want to (in this example we'll get old.google.com IP address)

## USAGE

usage: main.py [-h] -d DOMAIN -w WORDLIST [-o OUTPUT] [-s] [-c] [-t TIMEDELAY]

optional arguments:\
  -h, --help            show this help message and exit\
  -o OUTPUT, --output OUTPUT\
                        Path to output file for storing results\
  -s, --skip            Skip duplicates (like same IP as wildcard one)\
  -c, --combine         Combine words from dictionary for results like qa.ftp.domain.com\
  -t TIMEDELAY, --timedelay TIMEDELAY\
                        Set delay in seconds for limiting reqesting\
\
Required arguments:\
  -d DOMAIN, --domain DOMAIN\
                        Target domain to scan\
  -w WORDLIST, --wordlist WORDLIST\
                        Absolute path to dictionary\