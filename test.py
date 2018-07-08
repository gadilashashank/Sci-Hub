from __future__ import print_function
import platform
import os

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 test.py\n")
    quit()
# import all dependencies and check
try:
    from bs4 import BeautifulSoup as bs
    import re
    import requests
    import json
    print("Test successful. Ready to use sci_hub.py")
except(ImportError):
    print("Looks like some dependency is missing.")
    print("Run the appropriate conf file to fix this.")
quit()
