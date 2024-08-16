"""
Input format: 
	* <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> 
"""

import sys
import re

pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'


for line in sys.stdin:
    line = line.strip()
    if re.match(pattern, line):
        
