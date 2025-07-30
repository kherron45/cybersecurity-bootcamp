def get_unique_sorted_ips(ip_list):
    return sorted(set(ip_list))
ips = {"192.168.1.1", "10.0.0.1", "192.168.1.1"}
result = get_unique_sorted_ips(ips)
print(result)