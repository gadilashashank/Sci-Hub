'''
Sci-Hub Downloader - 1.0
----
Description:

This script takes input URL/DOI and tries
to download the paper from Sci-Hub.

Author : Gadila Shashank Reddy
Date : 24th June, 2018
'''
from __future__ import print_function
from bs4 import BeautifulSoup as bs
import os
import re
import requests
import sys

# Python 2.x incompatibility
if re.match("^2.", sys.version.split("(")[0].strip()):
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 sci_hub.py\n")
    quit()


'''
Parameters : None
Function   : Query Google for sci-hub url
Returns    : URL/empty string
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
Parameters : URL (string)
Function   : Checks title tag and validates
             if url is a sci-hub site
Returns    : Input Parameter/Empty string
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
Parameters : URL (string)
Function   : Alternate to get_url()
Returns    : Alternate url/empty string
extra      : Queries twitter page of sci-hub
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
Parameters : URL, user input (string, string)
Function   : Request sci-hub and download input paper
Return     : DOI of reqeusted paper/ empty string
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
Parameter  : DOI
Function   : Extract metadata given DOI
Return     : Nothing
Side-effect: Text file created
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
Parameter  : DOI
Function   : Rename and move downloaded files to separate dir.
Returns    : Nothing
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
