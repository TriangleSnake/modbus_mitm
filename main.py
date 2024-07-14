import time
TIMEOUT = 0.5
#select interface
print("please choose an interface:")
print(get_interfaces())

interface = get_interface(input())

#scan
ips = scan_ip(interface)

print("please choose an ip address:")

#choose target
target1 = input("target1:")
target2 = input("target2:")




#perform mitm
mitm_attack(target1,target2)

#read modbus
#write modbus
