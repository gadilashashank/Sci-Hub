'''
Sci-Hub Downloader
----
Description:

This script takes input URL/DOI and tries
to download the paper from Sci-Hub.

Version : 2.0
Date    : 14th July, 2018
Author  : Gadila Shashank Reddy
'''
from __future__ import print_function
import argparse
import os
import platform
import re

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 sci_hub.py\n")
    quit()

if platform.system() not in ['Linux', 'Darwin']:
    print("\nYOU HAVE BEEN WARNED")
    print("Looks like you are not running on GNU/Linux or a Mac")
    print("This program is not guarenteed to work on Windows\n")

from bs4 import BeautifulSoup as bs
import requests

# Define command line arguments
parser = argparse.ArgumentParser(description="Sci-Hub downloader: Utility to \
                                             download from Sci-Hub")
parser.add_argument("target",
                    help="URL/DOI to download PDF")
parser.add_argument("-p",
                    help="Absolute path to save files to\
                    (Default = ~/Downloads/sci_hub)")
parser.add_argument("-b",
                    help="Command to invoke browser")
args = parser.parse_args()


# Get Sci-Hub URL from Google
def get_url():
    print("Trying primary method.")
    # Query Google and create soup object.
    response = requests.get("https://www.google.com/search?&q=sci-hub")
    soup = bs(response.content, "lxml")
    # Target url is inside a cite tag.
    url = soup.cite.text
    # Regex check for URL. Returns empty string if
    # no match
    if re.match('http[s]?://sci-hub.[a-z]{2,}', url):
        print("URL from primary method is: " + url + "\n")
        return url
    else:
        print("URL from primary method not found.\n")
        return ''


# Alterane URL from Twitter
def try_alternate():
    print("Trying alternate method.")
    # Query twitter page of Sci-Hub
    # and create soup object
    response = requests.get("https://twitter.com/Sci_Hub")
    soup = bs(response.content, "lxml")
    # Try to extract the URL present
    # in the side panel as alt_url
    for i in soup.find_all("a", attrs={"class": "u-textUserColor"}):
        # Regex check
        if re.match('[http://[s]?]?sci-hub.[a-z]{2,}', i.text.strip()):
            alt_url = i.text.strip()
            # Append transfer protocol
            # if not present
            if "://" not in alt_url:
                alt_url = "https://" + alt_url
            print("Alternate URL is: " + alt_url + "\n")
            return alt_url + "/"
        else:
            return ""


# Validate URL by checking title
def validate_url(url):
    print("Validating {}".format(url))
    # Send request to given url
    # and compare title tags
    response = requests.get(url)
    soup = bs(response.content, "lxml")
    if soup.title.text == "Sci-Hub: removing barriers in the way of science":
        print("{} validated\n".format(url))
        return url
    else:
        print("{} not valid.".format(url))
        return ""


# Extract DOI, Mirror
def get_links(target):
    # Get response of target page
    # from Sci-Hub and create soup object
    response = requests.get(target)
    soup = bs(response.content, "lxml")
    # Extract DOI
    for i in soup.find_all("div", attrs={"class": "button", "id": "reload"}):
        doi = i.p.a['href'].replace("//sci-hub.tw/reload/", "")
    # Extract download link
    for i in soup.find_all("div", attrs={"class": "button", "id": "save"}):
        mirror = i.p.a['onclick'].split("'")[1]
        return doi, mirror


# Download paper
def download_paper(mirror, args):
    # Response from mirror link
    print("Sending request")
    response = requests.get(mirror)
    print("Response received. Analyzing...\n")
    os.system("sleep 1")
    # If header states PDF then write
    # content to file
    if response.headers['content-type'] == "application/pdf":
        size = round(int(response.headers['Content-Length'])/1000000, 2)
        print("Downloaded {} MB\n".format(size))
        with open("wuieobgefn.pdf", "wb") as f:
            f.write(response.content)
        f.close()
    # Check if firefox exists and open download link
    # in firefox
    elif re.match("text/html", response.headers['content-type']):
        print("Looks like captcha encountered.")
        if not os.system("command -v firefox 1,2>/dev/null"):
            print("Opening link in firefox...")
            os.system("firefox {}".format(mirror))
    # Check for browser command line arg
        elif args.b:
            print("Opening link in browser...")
            os.system("{} {}".format(args.b, mirror))
    # Print download link
        else:
            print("Open this link in a browser.")
            print(mirror)


# Rename and move
def move_file(doi, args):
    if doi:
        name = doi.replace("/", "_") + ".pdf"
        if os.path.exists("./wuieobgefn.pdf"):
            if not args.p:
                os.system("mv ./wuieobgefn.pdf {}".format(name))
                os.system("mkdir ~/Downloads/sci_hub/ 2>/dev/null")
                os.system("mv {} ~/Downloads/sci_hub/".format(name))
                print("Files saved in ~/Downloads/sci_hub/ as {}".format(name))
            elif args.p and os.path.exists(args.p):
                os.system("mv ./wuieobgefn.pdf {}".format(name))
                os.system("mv {} {}".format(name, args.p))
                print("Files saved at {} as {}".format(args.p, name))
            else:
                print("Looks like mentioned path does not exist")
                print("Saving file at {} as {}".format(os.system("pwd"), name))
                os.system("mv ./wuieobgefn.pdf {}".format(name))
    else:
        print("File saved as wuieobgefn.pdf in current directory")

# Main function
def main():
    sci_hub = validate_url(get_url())
    if not sci_hub:
        sci_hub = validate_url(try_alternate())
        if not sci_hub:
            print("Sci-Hub mirror not found")
            print("Try after some time")
            quit()
    else:
        url = sci_hub + args.target
        print("Extracting download links...")
        doi, mirror = get_links(url)
        if not mirror:
            print("Download link not available")
            print("Please try after sometime")
            os.system("sleep 10")
            quit()
        else:
            print("Downloading paper...")
            download_paper(mirror, args)
            move_file(doi, args)


main()
print("\nThanks for using.\n")
quit()
