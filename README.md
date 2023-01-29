Port Scanner
This is a python-based fast port scanner that uses threads to scan a specified host's open ports. The script takes command-line arguments such as starting port, ending port, number of threads, verbose output, and version. The output shows the open ports found and the time taken to scan.

Usage
css
Copy code
python port_scanner.py [OPTIONS] IPv4
Options
-s, --start: starting port (default 1)
-e, --end: ending port (default 1023)
-t, --threads: number of threads to use (default 500)
-V, --verbose: verbose output (default False)
-v, --version: display version
Example
Copy code
python port_scanner.py -s 20 -e 65535 -t 500 -V 192.168.0.1
Requirements
pyfiglet
termcolor
argparse
socket
threading
time
datetime


Regenerate response
