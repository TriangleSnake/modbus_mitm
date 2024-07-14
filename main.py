import time
from network_sniff import get_interfaces, scan_ip
TIMEOUT = 0.5


#select interface

interfaces = get_interfaces()
for id,info in interfaces.items():
    print(f"{id}: {info}")
interface = int(input("please choose an interface id:"))
interface = interfaces[interface]
print("choosed :",interface)


#scan

print("scanning mask...")
ips = scan_ip(interface[1])
for id,info in ips.items():
    print(f"{id}: {info}")
print("please choose ip addresses:")


#choose target

target1 = int(input("target1:"))
target1 = ips[target1]

target2 = int(input("target2:"))
target2 = ips[target2]

print(f"target1:{target1}")
print(f"target2:{target2}")
exit()

#perform mitm
mitm_attack(target1,target2)

#read modbus
#write modbus
