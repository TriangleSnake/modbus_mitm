import subprocess


def get_interfaces():
    command = "ip -o -f inet addr show | awk '/scope global/ {print $1,$2,$4}'"
    output = subprocess.check_output(command,shell=True).decode()
    info = {}
    for i in output.split("\n")[:-1]:
        data = i.split(" ")
        info[int(data[0].strip(":"))] = data[1:]
    return info
def scan_ip(ip):
    command = f"nmap -sn {ip} | awk '/Nmap scan report for/ {{print $5}}'"
    output = subprocess.check_output(command,shell=True).decode().split("\n")[:-1]
    ips = dict(zip(range(1,len(output)+1),output))
    return ips
    
