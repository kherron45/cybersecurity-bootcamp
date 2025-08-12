import re
log = "error from 192.168.1.1"
parts = log.split(" , ")
pattern = r'\b\d{1,3}\.\d{1,3}\. \d{1,3}\b'
ips = re.findall(pattern, log)
print("found ip 192.168.1.1")