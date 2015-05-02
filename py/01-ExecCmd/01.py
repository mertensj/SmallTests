#! /usr/bin/python
#
#

import subprocess

# Simple command
print("------------ PATH ----------------")
subprocess.call('echo $PATH', shell=True)

print()
print("------------ ls   ----------------")
subprocess.call('ls -l', shell=True)
print()

