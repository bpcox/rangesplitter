#! /usr/bin/env python3.4

import ipaddress
import math

toSplit=False
while not toSplit:

	inputRange = input('Input the IP range you would like to split into subranges: ')
	try:
		toSplit =ipaddress.ip_network(inputRange)
	except:
		ValueError

rangeSize = False
default = False
while (not rangeSize and not default):
	rawSize = input ('Input the size of the CIDR range you would calculate. Must be a larger or equal number compared to the suffix of the input range ('+str(toSplit.prefixlen)+') :')

	if not rawSize:
		default=True
	
	if int(rawSize)<toSplit.prefixlen:
		print('Invalid input')
		continue
	else:
		rangeSize = int(rawSize)

if not default:
	print(list(toSplit.subnets(new_prefix=rangeSize)))
if default:
	if toSplit.version==4:
		print(list(toSplit.subnets(new_prefix=16)))
	if toSplit.version==6:
		print(list(toSplit.subnets(new_prefix=48)))
	print('default')
