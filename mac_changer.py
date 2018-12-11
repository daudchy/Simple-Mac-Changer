#!/usr/bin/env python

import subprocess

interface = raw_input("Interface-> ")
mac_address = raw_input("New MAC-> ")

print("[+] Changing MAC Address for "+interface+" to "+mac_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw","ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
