# subfinder
Python script to find subdomains omitting wildcard and for some programming practice

## Goal
Primary goal was to have handy tool which using wordlists and asking DNS for entries omitting wildcards in DNS entries by moving "*" one level left.

*EXAMPLE*\
If domain has entry like *.google.com then every DNS query will be pointing to same IP, but if we create query like this *.old.google.com then it will provide IP that is actually pointing where we want to (in this example we'll get old.google.com IP address)

## USAGE

todo