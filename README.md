# Sci-Hub Downloader
---
A script to download papers from Sci-Hub.

**Version** - 1.0

**Release** - 24 June, 2018

**Author** - Gadila Shashank Reddy

---

## Disclaimer

This application is for educational purpose only. I do not take responsibility
of what you choose to do with this application.


## About

*Sci-Hub downloader* is a simple python script that attempts to automatically download papers from
sci-hub without the hassle of finding a working mirror or going through multiple sites that are not
legit sci-hub mirrors via a *Command Line Interface*.

Hope you like it!

## Requirements

### For UNIX/Linux

* Python 3.x
```md
sudo apt update
sudo apt install python3
```
The example is given for systems with apt as package manager. If your package manager is different
(say dnf or pacman), type the appropriate command to install Python 3.x

### For Mac

* Homebrew

```md
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Python 3.x

```md
brew update
brew install python3
```
pip3 is a requirement but I have no clue if the mentioned command works. A quick search should help.
* python3-pip

```md
sudo easy_install python3-pip
```

* Wget

### Windows

There is no automatic setup file written to configure your system to run the script. You would need
to have these installed.

* Python 3.x and pip3/python3-pip

* Wget

Python modules

* requests

* BeautifulSoup4

* json

These modules are in-built. Check they can be imported without problems.

* os and sys

* re

## A word

At any point either during installation or usage if any script is invoked with python version 2.x ,
a friendly warning is printed and the script automatically terminates. This is because all the
scripts are intended to be run on 3.x versions of python.

```md
$ python2 sci_hub.py
This script is NOT compatible with Python 2.x
Use this command to run the script:

python3 sci_hub.py

```

## Installation

Once the requirements have been satisfied, run either **linux_conf.py** or **mac_conf.py** if your
system is UNIX/Linux or Mac respectively.

Expected output on UNIX/Linux systems

```md
$ python3 linux_conf.py

sudo password is required to install any missing packages.

Package Manager is apt

[some output comes here]

***********************************************
	System ready for Sci-Hub Downloader!
***********************************************

```

Expected output on Mac

```md
$ python3 mac_conf.py

[some output comes here]

***********************************************
	Your Mac is ready for Sci-Hub Downloader!
***********************************************

```

Regardless of your OS run test.py to confirm your system is properly configured and everything works

Success

```md
$ python3 test.py
Test successful. Ready to use sci_hub.py
```

Failure.

```md
$ python3 test.py
Looks like some dependency is missing.
Run the appropriate conf file to fix this.
```

Check all dependencies are properly installed and importable without any errors if a failure occurs.

## Usage

Once your system is properly configured and test.py returns a success message, you are ready to use
Sci-Hub Downloader.

Run sci_hub.py

```md
$ python3 sci_hub.py
URL from primary method is: https://sci-hub.tw/

Validating https://sci-hub.tw/

https://sci-hub.tw/ validated

Enter URL/DOI of paper to be fetched:
URL should be complete eg: https://<some URL>/<some path>:

```

The script has two methods written to get the URL of a valid sci-hub mirror. The primary method was
sufficient to get a valid mirror in the output mentioned above.

If the primary method somehow fails then a secondary method is invoked and the output in this case
is also similar.

Now type in the DOI/URL that you normally enter in sci-hub and press enter.

It is preferred to input DOI wherever possible but if a URL is being input then make sure it is the
exact URL as copy-pasted from the address bar of a browser.

```md
Correct URL input 	: https://ieeexplore.ieee.org/document/1695678/
Incorrect URL input	: ieeexplore.ieee.org/document/1695678/
```

After inputting target URL/DOI the file should be downloaded.

```md
Enter URL/DOI of paper to be fetched:
URL should be complete eg: https://<some URL>/<some path>:

https://ieeexplore.ieee.org/document/1695678/

If somehow the download fails visit this link in a browser:

[A link is provided here]
```

The PDF file is downloaded as [DOI of the paper].pdf

```md
Input URL : https://ieeexplore.ieee.org/document/1695678/
DOI		  : 10.1109/MS.1987.229797
Saved as  : 10.1109_MS.1987.229797.pdf
```

After the PDF is successfully downloaded the user is prompted for an optional download of the metadata
of input paper.

```md
Extract metadata into a separate text file?[y/n]
```

If you type "y" then the metadata is downloaded and saved as a text file.

If you type "n" then the program is terminated.

After all files are downloaded they are moved into a separate directory with the DOI of the input
file as the name inside the current working directory.

```md
10.1109_MS.1987.229797
├── 10.1109_MS.1987.229797.pdf
└── 10.1109_MS.1987.229797.txt

0 directories, 2 files
```

## Known issues

Though the script tries its best in doing its job is has few issues/limitations.
These are mentioned here.

* Captcha
  * If a captcha is encountered the script is pretty much useless.
  * In such cases try to run the script after some time.
  * It is advisable not to run the script over a college proxy
    or similar networks.

* Proxy
  * None of the network transactions in the script are configured to run over
    proxy
  * If proxy is required, the user should manually alter the script.

* Mirror not found
  * The script has two methods written to find a valid mirror. This can fail.
  * For such cases https://sci-hub.[extension]/[URL/DOI] should be used in
    browser

* DOI not assigned
  * The script is not prepared to handle input whose
    DOI is either not found or not assigned.
  * This will be fixed in a later release.

* Any issue that did not arise during development/testing.


## In case of issues with the script

This script as already mentioned, is not meant to be used for python version 2.x

The scripts have been developed and tested on a Ubuntu 16.04 machine running python 3.5.2

Thus it is assumed that the scripts should function properly on python 3.5+ provided the dependencies are proper.

Still if there is any problem feel free to create an issue on the repository by mentioning the relevant details.
