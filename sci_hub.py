'''
Sci-Hub Downloader - 1.0

This script takes input URL/DOI and tries
to download the paper from Sci-Hub.

Gadila Shashank Reddy
24th June, 2018
'''
from __future__ import print_function
from bs4 import BeautifulSoup as bs
import os
import re
import requests
import sys

# Python 2.x incompatibility
if "2." in sys.version:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 sci_hub.py\n")
    quit()


'''
This function searches Google and tries
to extract the URL of Sci-Hub from the
search results.
'''


def get_url():
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
        print("Trying alternate method\n")
        return ''


'''
This function tries to validate if
input URL is a legit Sci-Hub site
by checking its title tag.
( Works for now might need
  improvisation later.)
'''


def validate_url(url):
    print("Validating " + url + "\n")
    # Query input URL and create
    # soup object
    if not url:
        return ''
    response = requests.get(url)
    soup = bs(response.content, "lxml")
    # Checks title and returns the input
    # Else returns empty string
    if soup.title.text == "Sci-Hub: removing barriers in the way of science":
        print(url + " validated\n")
        return url
    else:
        print(url + " found invalid.\n")
        return ''


'''
This function is meant to
be a backup function to fetch
URL incase the primary function
fails
(Better to add more alternate
 methods later.)
'''


def try_alternate(url):
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
    # If primary function returns empty
    # string, return alt_url after validating
    if not url:
        print("Alternate URL is: " + alt_url + "\n")
        return validate_url(alt_url + "/")
    # If input URL is same as alt_url then
    # return empty string. This function would have
    # been called either when the input URL is
    # empty or invalid.
    if re.match(alt_url, url) or re.match(url, alt_url):
        print("Alternate URL could not be fetched")
        return ''


'''
This function takes the Sci-Hub URL and
target URL/DOI and tries to download the
PDF.
'''


def get_paper(url, target):
    # Get response of target page
    # from Sci-Hub and create soup object
    response = requests.get(url+target)
    soup = bs(response.content, "lxml")
    # Extract DOI
    for i in soup.find_all("div", attrs={"class": "button", "id": "reload"}):
        doi = i.p.a['href'].replace("//sci-hub.tw/reload/", "")
    # Extract download link
    for i in soup.find_all("div", attrs={"class": "button", "id": "save"}):
        mirror = i.p.a['onclick'].split("'")[1]
    # Returns empty string if no download link
    # found.
        if not mirror:
            return ''
    # Download pdf and return DOI
        else:
            print("\nIf somehow the download fails visit " +
                  "this link in a browser: \n")
            print(mirror + "\n")
            os.system("wget -O {} {}".format(doi.replace("/", "_") + ".pdf",
                                             mirror))
            return doi


'''
This function extracts metadata
from DOI in JSON format and writes
it to a text file
'''


def get_metadata(doi):
    import json
    # Define header and send request
    header = {"Accept": "application/vnd.citationstyles.csl+json"}
    response = requests.get("http://dx.doi.org/" + doi, headers=header)
    # Convert response into JSON object
    data = response.json()
    # Define name of output file
    output_file = doi.replace("/", "_") + ".txt"
    # Write to output file
    with open(output_file, 'w') as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))
    f.close()
    print("\nFiles saved in {} directory\n".format(doi.replace("/", "_")))
    return


'''
This function moves the downloaded files
into a separate directory in current
working directory
'''


def move_data(doi):
    temp = doi.replace("/", "_")
    os.system("mkdir %s" % (temp))
    os.system("mv {} {}".format(temp + ".*", temp))

# Call primary method and verify URL
url = validate_url(get_url())

# If invalid try alternate method.
if not url:
    url = try_alternate(url)

print("Enter URL/DOI of paper to be fetched:")
print("URL should be complete eg: https://<some URL>/<some path>:\n")
target = input()

doi = get_paper(url, target)

ext = input("Extract metadata into a separate text file?[y/n]\n")
if re.match("[Yy]+(es)?", ext):
    get_metadata(doi)
if re.match("[Nn]+(o)?", ext):
    print("\nFile saved in {} directory\n".format(doi.replace("/", "_")))

move_data(doi)
quit()
