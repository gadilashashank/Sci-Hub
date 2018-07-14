'''
Configuration file for GNU/Linux machines
to run sci_hub.py
'''
from __future__ import print_function
import os
import platform
import re

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 linux_conf.py\n")
    quit()

# Warning for non linux host
if platform.system() != 'Linux':
    print("Looks like you are not running a linux machine.")
    print("If this is a mistake please report here:")
    print("https://github.com/gadilashashank/Sci-Hub/issues")
    quit()

print("\nsudo password is required to install any missing packages.\n")

# Apt as Package Manager
if not os.system("command -v apt > /dev/null 2>&1"):
    print("Package Manager is apt\n")
    os.system("sudo apt update")
    os.system("sudo apt install python3-pip")
# dnf as Package Manager
elif not os.system("command -v dnf > /dev/null 2>&1"):
    print("Package Manager is dnf\n")
    os.system("sudo dnf install python3-pip")
# pacman as Package Manager
elif not os.system("command -v pacman > /dev/null 2>&1"):
    print("Package Manager is pacman\n")
    os.system("sudo pacman -S --needed python-pip")
# slackpkg as Package Manager
elif not os.system("command -v slackpkg > /dev/null 2>&1"):
    print("Package Manager is slackpkg\n")
    os.system("sudo slackpkg update")
    os.system("sudo slackpkg install python3-pip")
# Package Manager not mentioned here
else:
    print("Looks like your package manager is" +
          " not covered by the setup file\n")
    print("Make sure all packages and dependencies mentioned" +
          " in REQUIREMENTS.md are installed\n\n")
    quit()

# Install dependencies
os.system("sudo pip3 install BeautifulSoup4 requests lxml")
# Success
print()
print("*"*70)
print("\tSystem ready for Sci-Hub Downloader!")
print("*"*70)
print()

quit()
