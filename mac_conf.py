'''
Configuration file for MacOS
to run sci_hub.py
'''
from __future__ import print_function
import os
import platform

# Non MacOS warning
if platform.system() != 'Darwin':
    print("Looks like you are not running on a Mac.")
    print("If this is a mistake please report here:")
    print("https://github.com/gadilashashank/Sci-Hub/issues")
    quit()


# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 mac_conf.py\n")
    quit()

# Install dependencies
os.system("pip3 install requests BeautifulSoup4 lxml")

# Success
print()
print("*"*70)
print("\tYour Mac is ready for Sci-Hub Downloader!")
print("*"*70)
print()

quit()
