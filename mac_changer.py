#!*/usr/bin/env python

import subprocess
import optparse

def get_argument():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
	parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help foe more info.")
	elif not options.new_mac:
		parser.error("[-] Please specify a new mac, use --help foe more info.")
	return options

def change_mac(interface,new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)
	subprocess.cell(["ifconfig",interface,"down"])
	subprocess.cell(["ifconfig",interface,"hw","either",new_mac])
	subprocess.cell(["ifconfig",interface,"up"])

options = get_argument()
change_mac(options.interface,options.new_mac)
