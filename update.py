import os
import json
import requests

cur_version = "2.2"
url = "https://raw.githubusercontent.com/gadilashashank/Sci-Hub/master/"
url = url + "package.json"


def check_update():
    print("\nChecking for updates...")
    response = requests.get(url)
    j = json.loads(response.content)
    if j['version'] > cur_version:
        print("\nNew version " + j['version'] + " released on "
              + j["release date"] + "\n")
        return True
    else:
        return False
