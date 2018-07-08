'''
Configuration file for Linux machines
to run sci_hub.py
'''
from __future__ import print_function
import os
import re
import sys

# Python 2.x incompatibility
if re.match("^2.", sys.version.split("(")[0].strip()):
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 mac_conf.py\n")
    quit()

# Install dependencies
os.system("pip3 install requests BeautifulSoup4")

# Success
print()
print("*"*70)
print("\tYour Mac is ready for Sci-Hub Downloader!")
print("*"*70)
print()

quit()
