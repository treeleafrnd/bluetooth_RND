# to scan bluetooth device

import bluetooth

neardevice = bluetooth.discover_devices(lookup_names=True)

for address, name in neardevice:
    print(address)
    print(name)