import time
from network_sniff import get_interfaces, scan_ip
from mitm import mitm_attack
from GUI import GUI
TIMEOUT = 0.5

# Create gui

gui = GUI()

#select interface

interfaces = get_interfaces()
interfaces_item = []
print(interfaces)
for id,info in interfaces.items():
    print(f"{id}: {info}")
    interfaces_item.append(f"{info[0]} {info[1]}")
gui.interface_combo["values"] = interfaces_item
gui.mainloop()
"""
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
# exit()

#perform mitm
mitm_attack(target1,target2)
"""
#read modbus
#write modbus
