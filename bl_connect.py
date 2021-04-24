import bluetooth, subprocess
nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                            flush_cache=True, lookup_class=False)

addr = 'F0:18:98:BA:C3:D1'
port = 1

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((addr,port))

s.recv(1024)
s.send("Hello World!")

