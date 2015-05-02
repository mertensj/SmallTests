#! /usr/bin/python
#
#

import subprocess
debug=False
#debug=True
# ------------------------------------------------------------------------
def getStatusInterfaces():
# ------------------------------------------------------------------------
	if debug: print("[debug] Search for ALL Network Interfaces")
	outputByte = subprocess.check_output('ip link', shell=True)
	outputString = outputByte.decode()

	ipLinkString=outputString.split('\n')
	##if debug: print(ipLinkString)
	ipInterfaces = []
	for i in range(len(ipLinkString)):
		ipLinkString[i]=ipLinkString[i].split()
		if ( len(ipLinkString[i]) > 8 and 
                   ( ipLinkString[i][8] == 'UP' or
                     ipLinkString[i][8] == 'DOWN')):
			if debug: print(ipLinkString[i])
			##return(ipLinkString[i][1].replace(':',''))
			##return(ipLinkString[i][1][0:-1])
			ipInterfaces.append([ipLinkString[i][1][0:-1],ipLinkString[i][8]])

	# If we reach here, we have gone through all interfaces
	return(ipInterfaces)

# ------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------
#interfaceName = getActiveInterface()
#if interfaceName:
#	print(".. InterfaceName UP =", interfaceName)
#else:
#	print(".. No Active Interface found")
# ------------------------------------------------------------------------
