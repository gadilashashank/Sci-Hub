'''
Configuration file for Linux machines
to run sci_hub.py
'''
from __future__ import print_function
import os
import sys

# Python 2.x incompatibility
if "2." in sys.version:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 linux_conf.py\n")
    quit()

print("\nsudo password is required to install any missing packages.\n")

# Apt as Package Manager
if not os.system("command -v apt > /dev/null 2>&1"):
    print("Package Manager is apt\n")
    os.system("sudo apt update")
    os.system("sudo apt install python3-pip wget")
# dnf as Package Manager
elif not os.system("command -v dnf > /dev/null 2>&1"):
    print("Package Manager is dnf\n")
    os.system("sudo dnf install python3-pip wget")
# pacman as Package Manager
elif not os.system("command -v pacman > /dev/null 2>&1"):
    print("Package Manager is pacman\n")
    os.system("sudo pacman -S python3-pip wget")
# slackpkg as Package Manager
elif not os.system("command -v slackpkg > /dev/null 2>&1"):
    print("Package Manager is slackpkg\n")
    os.system("sudo slackpkg update")
    os.system("sudo slackpkg install python3-pip wget")
# Package Manager not mentioned here
else:
    print("Looks like your package manager is" +
          " not covered by the setup file\n")
    print("You would need to install the following packages:\n")
    print("python3-pip requests beautifulsoup4\n\n")
    quit()

# Install dependencies
os.system("sudo pip3 install BeautifulSoup4 requests")
# Success
print()
print("*"*70)
print("\tSystem ready for Sci-Hub Downloader!")
print("*"*70)
print()

quit()
