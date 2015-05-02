#! /usr/bin/python
#
#

import subprocess

#subprocess.call('ls -l', shell=True)

proc = subprocess.Popen('ls -l', 
                            shell = True,
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE
                        )

(out, err) = proc.communicate()

print(out)


