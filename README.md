# SynScan
A simple port scanner written in python

Requirement:
python 2.6.x or 2.7.x

Usage: python port_scanner.py [host_name_or_ip] [start_of_port_range] [end_of_port_range]
- If end port isn't given the scanner scan the 'start_of_port_range' + 100 range of ports
- If only the host name or ip is given the program scan the first 100 port of the host

Planed features:
 - more and improved command line options
 - installable pip module
 - scan results save in to json
 - more scan option
 - improved speed
