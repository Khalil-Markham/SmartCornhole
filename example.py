#!/usr/bin/python

import bluetooth

def connect ():
    bd_addr = "x:x:x:x:x:x"
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()

connect()