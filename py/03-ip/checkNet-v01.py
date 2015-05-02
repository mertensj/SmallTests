#! /usr/bin/python
#
#

import subprocess
interfaceName = ''
apName = ''
ipAddress = ''
defaultGateway = ''
interfaceUP = False

# ------------------------------------------------------------------------
def checkInterfaces():
# ------------------------------------------------------------------------
	##print("Check Interfaces:")
	interfaceUP=0
	outputByte = subprocess.check_output('ip link', shell=True)
	outputString = outputByte.decode()
	##print(outStr)

	ipLinkString=outputString.split('\n')

	for line in ipLinkString:
		##print(line)
		wordList=line.split()
		if len(wordList) > 7:
			if wordList[8] == "UP":
				interfaceName = wordList[1].replace(':','')
				print("..",interfaceName, " is active")
				interfaceUP=1
				return(interfaceName,interfaceUP)

	if not interfaceUP:
		print(".. No Interface UP")
		exit(0)


# ------------------------------------------------------------------------
def checkapName():
# ------------------------------------------------------------------------
	outputByte = subprocess.check_output('iwconfig', 
       		             stderr=subprocess.STDOUT,
       		             shell=True)
	outputString = outputByte.decode()
	iwConfigString = outputString.split('\n')
	apNameFound = 0

	for line in iwConfigString:
		wordList=line.split()
		if len(wordList) > 0:
			if wordList[0] == interfaceName:
				apName = wordList[3]
				print("..", interfaceName, " connected to ", apName)
				apNameFound = 1
			if apNameFound and line.find('Bit Rate') > 0:
				print(line)
			if apNameFound and line.find('Link Quality') > 0:
				print(line)
	if(apNameFound): 
		return(apName,apNameFound)
	else:
		print(".. No Access Point Found")
		exit(0)


# ------------------------------------------------------------------------
def checkIpAddress():
# ------------------------------------------------------------------------
	outputByte = subprocess.check_output('ifconfig -a', 
      	 	             stderr=subprocess.STDOUT,
       		             shell=True)
	outputString = outputByte.decode()
	ifConfigString = outputString.split('\n')
	for line in ifConfigString:
		wordList=line.split()
		if len(wordList) > 0:
			if interfaceName == wordList[0].replace(':',''):
				##print(line)
				position = ifConfigString.index(line)
				##print(ifConfigString[position+1])
				inetLine=ifConfigString[position+1]
				if inetLine.find('inet') > 0:
					inetList=inetLine.split()
					print(".. IP address : ", inetList[1])
					return(inetList[1])			

# ------------------------------------------------------------------------
def checkDefaultGateway():
# ------------------------------------------------------------------------
	outputByte = subprocess.check_output('ip route', 
       	          	   stderr=subprocess.STDOUT,
       	          	   shell=True)
	outputString = outputByte.decode()
	ifConfigString = outputString.split('\n')
	for line in ifConfigString:
		if interfaceUP and line.find(interfaceName) > 0:
			##print(line)
			wordList=line.split()
			if wordList[0] == 'default':
				##print(line)
				defaultGateway = wordList[2]
				print(".. Gateway    : ", defaultGateway)
				return(defaultGateway)

# ------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------
(interfaceName,interfaceUP) = checkInterfaces()
if interfaceUP: (apName,apNameFound) = checkapName()
if apNameFound: ipAddress = checkIpAddress()
defaultGateway = checkDefaultGateway()

