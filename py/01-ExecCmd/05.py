#! /usr/bin/python
#
#

import subprocess


##out=subprocess.call('ls -l', shell=True)
#out=subprocess.call('ip link', shell=True)

outByte = subprocess.check_output('ip link', shell=True)
out = outByte.decode()
print(out)


