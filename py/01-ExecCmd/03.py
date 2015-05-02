#! /usr/bin/python
#
#
#  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#  return_code = proc.wait()
#  return return_code, proc.stdout.read(), proc.stderr.read()

import sys
import subprocess

cmdping = "ping -c4 www.google.com"

p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    outString = str(out)   ## convert byte to string
    ##if outString == '' and p.poll() != None:
    if p.poll() != None:
        break
    if outString != '':
        sys.stdout.write(outString)
        sys.stdout.flush()
