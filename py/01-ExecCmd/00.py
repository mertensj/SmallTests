#! /usr/bin/python
#
#

import subprocess

test=1
print("===> Test ", test," <=================")
subprocess.call(["ls", "-l"])

test=test+1
print("===> Test ", test," <=================")
subprocess.call('ls -l', shell=True)

test=test+1
print("===> Test ", test," test return value <=================")
subprocess.check_call('ls -l', shell=True)

test=test+1
print("===> Test ", test," capture output <=================")
outByteStream=subprocess.check_output('ls -l', shell=True)
print(outByteStream)

test=test+1
print("===> Test ", test," capture output AND decode <=================")
outByteStream=subprocess.check_output('ls -l', shell=True)
outString=outByteStream.decode()
print(outString)

