import subprocess as sub
from color import print_error, print_good, print_line, print_status


# first, get a list of the hardware ports
print_status("Gathering a list of hardware ports...")
hardware_ports = sub.run(["networksetup", "-listallhardwareports"], stdout=sub.PIPE)
hardware_ports = hardware_ports.stdout.decode().splitlines()
ports_found = []

for port in hardware_ports:
    if port.startswith("Hardware"):
        ports_found.append(port.split(":")[-1].strip())
    else:
        continue

print_good("\tFound {}".format(len(ports_found)))




print_status("Determining the WiFi device name...")

found = False

# for every entry found, find out if one of them is a wireless interface
for entry in range(len(hardware_ports)):
    # the find method will return the index of the lowest position the subtring was found
    # it will return a -1 if not found
    #
    if hardware_ports[entry].find("Wi-Fi") > 0:
        # print_good("got one " + entry)
        found = True
        device_name = hardware_ports[entry + 1].split(":")[-1].strip()
    else:
        continue

if found:
    # print_good("Found a Wi-Fi hardware port!")
    print_good("\t{}".format(device_name))
elif not found:
    print_error("No Wi-Fi interfaces found!")


print_status("Gathering any preferred wireless networks...")
preferred = sub.run(["networksetup","-listpreferredwirelessnetworks", device_name], stdout=sub.PIPE)
preferred = preferred.stdout.decode()
print_status(preferred)




###
#
# TO DO
#
# remove a preferred wireless network
# sub.run(["networksetup", "-removepreferredwirelessnetwork"], stdout=sub.PIPE)
#
# remove all preferred wireless networks
# sub.run(["networksetup", "-removeallpreferredwirelessnetworks"], stdout=sub.PIPE)
#
###
