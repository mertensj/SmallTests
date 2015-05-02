#! /usr/bin/python
#
#

import subprocess
import ip_link


# ------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------
interfaceName = ip_link.getActiveInterface()
if interfaceName:
       print(".. InterfaceName UP =", interfaceName)
else:
       print(".. No Active Interface found")

