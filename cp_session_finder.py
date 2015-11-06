#!/usr/bin/env python

"""

Check Point Session Finder

"""

__version__ = 0.1


import sys
import re


def generic_hex(value):

	'''
		Convert any passed parameter to hex
	'''

	hex_value = hex(int(value))[2:].rjust(8, '0')

	return hex_value


def ip_to_hex(ip):

	'''
		Parse an IP and convert it to hex
	'''

	hex_ip = ''
	(first_octect, second_octect, third_octect, fourth_octect) = ip.split('.')

	# Convert each octect and remove the leading 0x
	first_octect = hex(int(first_octect))[2:]
	second_octect = hex(int(second_octect))[2:]
	third_octect = hex(int(third_octect))[2:]
	fourth_octect = hex(int(fourth_octect))[2:]

	# Each octect has format xx.xx.xx.xx
	for octect in (first_octect, second_octect, third_octect, fourth_octect):
		hex_ip += octect.rjust(2, '0')

	return hex_ip


def validate_ipv4(ip):

	'''
		Validate if IPv4 address is valid
	'''

	ipv4_regex = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

	if ipv4_regex.match(ip):
		return True
	else:
		return False 


def usage():

	print "ERROR! Pass the strings you want to convert"

def main():

	if not sys.argv[1:]:
		sys.exit(usage())

	grep_pattern = []

	for arg in sys.argv[1:]:
		#print arg
		if validate_ipv4(arg):
			grep_pattern += [ip_to_hex(arg)]
		else:
			grep_pattern += [generic_hex(arg)]

	print("fw tab -t connections -u | grep -E '{0}'").format('.*'.join(grep_pattern))


if __name__ == '__main__':
	main()