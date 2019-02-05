'''
Sci-Hub Downloader
----
Description:

This script takes input URL/DOI and tries
to download the paper from Sci-Hub.

Version : 2.1
Date    : 16th July, 2018
Author  : Gadila Shashank Reddy
'''
from __future__ import print_function
import argparse
import os
import platform
import re
import time
import webbrowser as wbb

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 sci_hub.py\n")
    quit()

# Warning for any platform other than *NIX
if platform.system() not in ['Linux', 'Darwin']:
    print("\nYOU HAVE BEEN WARNED")
    print("Looks like you are not running on GNU/Linux or a Mac")
    print("This program is not guarenteed to work on Windows\n")

from bs4 import BeautifulSoup as bs  # noqa: E402
import requests  # noqa: E402

# Define command line arguments
parser = argparse.ArgumentParser(description="Sci-Hub downloader: Utility to \
                                             download from Sci-Hub")
parser.add_argument("target",
                    help="URL/DOI to download PDF", type=str)
parser.add_argument('--proxy',
                    default='socks5://127.0.0.1:1080',
                    type=str,
                    help='requests proxy support. default:' +
                    'socks5://127.0.0.1:1080')
parser.add_argument('--proxy_enable',
                    action='store_true')
parser.add_argument("--view", help="Open article in browser for reading",
                    action="store_true")
args = parser.parse_args()
proxies = {
    "http": "socks5://127.0.0.1:1080",
    "https": "socks5://127.0.0.1:1080",
}


# Get Sci-Hub URL from Google
def get_url():
    print("Trying primary method.")
    # Query Google and create soup object.
    if args.proxy_enable:
        global proxies
        response = requests.get("https://www.google.com/search?&q=sci-hub",
                                proxies=proxies)
    else:
        response = requests.get("https://www.google.com/search?&q=sci-hub")
    soup = bs(response.content, "lxml")
    # Target url is inside a cite tag.
    url = soup.cite.text
    # Regex check for URL. Returns empty string if
    # no match
    if re.match('(https?://)?sci-hub.[a-z]{2,}', url):
        if not url.startswith('http://') and not url.startswith('https://'):
            # if url has no proto prefix, add 'http://' by default
            url = 'http://' + url
        if url[-1] != '/':
            url += '/'
        print("url from primary method is: " + url + "\n")
        return url
    else:
        print("URL from primary method not found.\n")
        return ''


# Alterane URL from Twitter
def try_alternate():
    print("Trying alternate method.")
    # Query twitter page of Sci-Hub
    # and create soup object
    global proxies
    if args.proxy_enable:
        response = requests.get("https://twitter.com/Sci_Hub", proxies=proxies)
    else:
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
    if url == "":
        print("URL not valid")
        return ""
    # Send request to given url
    # and compare title tags
    if args.proxy_enable:
        global proxies
        response = requests.get(url, proxies=proxies)
    else:
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
    if args.proxy_enable:
        global proxies
        response = requests.get(target, proxies=proxies)
    else:
        response = requests.get(target)
    soup = bs(response.content, "lxml")
    # Extract DOI
    try:
        mirror = soup.find("iframe", attrs={"id": "pdf"})['src'].split("#")[0]
        if mirror.startswith('//'):
            mirror = mirror[2:]
            mirror = 'https://' + mirror
    except Exception:
        print("Mirror not found")
        mirror = ""
    try:
        doi = soup.title.text.split("|")[2].strip()
    except Exception:
        print("DOI not found")
        doi = ""
    # Extract download link
    return doi, mirror


# Download paper
def download_paper(mirror, args):
    # Response from mirror link
    print("Sending request")
    if args.proxy_enable:
        global proxies
        response = requests.get(mirror, proxies=proxies)
    else:
        response = requests.get(mirror)
    print("Response received. Analyzing...\n")
    # If header states PDF then write
    # content to file
    if args.view:
        print("Firing up your browser...")
        wbb.open_new(mirror)
        quit()
    elif response.headers['content-type'] == "application/pdf":
        size = round(int(response.headers['Content-Length'])/1000000, 2)
        print("Downloaded {} MB\n".format(size))
        with open("./Downloads/wuieobgefn.pdf", "wb") as f:
            f.write(response.content)
        f.close()
    # Check if firefox exists and open download link
    # in firefox
    elif re.match("text/html", response.headers['content-type']):
        print("Looks like captcha encountered.")
        print("Download link is \n" + mirror + "\n")
        time.sleep(2)
        wbb.open_new(mirror)
        quit()


# Rename and move
def move_file(doi, args):
    if doi:
        name = doi.replace("/", "_") + ".pdf"
        if os.path.exists("./Downloads/wuieobgefn.pdf"):
            os.rename("./Downloads/wuieobgefn.pdf", "./Downloads/" + name)
            print("Files saved at ./Downloads/" + name)
    else:
        print("Files saved at ./Downloads/wuieobgefn.pdf")


# Main function
def main():
    if args.proxy_enable:
        if len(args.proxy) != 0:
            global proxies
            proxies['http'] = args.proxy
            proxies['https'] = args.proxy
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
            print("\nAlso try prepending ' http://dx.doi.org/' to input")
            print("If it still doesn't work raise an issue at " +
                  "https://github.com/gadilashashank/Sci-Hub/issues")
            time.sleep(10)
            quit()
        else:
            print("Downloading paper...")
            download_paper(mirror, args)
            move_file(doi, args)


main()
print("\nThanks for using.\n")
quit()
