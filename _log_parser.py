import re
log = "error from 192.168.1.1"
pattern = r'\b\d{1,3}\.\d{1,3}\. \d{1,3}\b'
ips = re.findall(pattern, log)
print("found ips 192.168.1.1:", ips)