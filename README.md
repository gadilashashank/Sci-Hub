# Sci-Hub Downloader
---
A script to download papers from Sci-Hub.

**Initial Release** - 24 June, 2018

**Current Version** - 2.0

**Update release** - 14th July, 2018

**Author** - Gadila Shashank Reddy

---

## Disclaimer

This application is for educational purpose only. I do not take responsibility
of what you choose to do with this application.


## About

*Sci-Hub downloader* is a simple python script that attempts to automatically
download papers from sci-hub without the hassle of finding a working mirror or
going through multiple sites that are not legit sci-hub mirrors via a
*Command Line Interface*.

Hope you like it!

## Requirements

### For UNIX/Linux

* Python 3.x
```md
sudo apt update
sudo apt install python3
```
The command may vary across different package managers but the end goal is to
install Python 3.x

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
pip3 is a requirement but I have no clue if the mentioned command works. A quick
search should help.

* python3-pip

```md
sudo easy_install python3-pip
```

### Windows

This application is **NOT guaranteed** to work on Windows systems directly. It
is advised to run it on a *Windows subsystem for Linux* a.ka.
*Bash on Ubuntu on Windows* or on a Linux virtual machine. Please note that at
the time of writing this document none of these methods have been tested for
proper functioning.

## A word

Friendly warnings are printed whenever the script is used in an unexpected manner.
It is therefore advised to read these errors properly and take appropriate action.

If you feel any such warning is a mistake, please create an issue on the
repository.

An example warning

```md
$ python2 sci_hub.py
This script is NOT compatible with Python 2.x
Use this command to run the script:

python3 sci_hub.py
```

## Installation

Once the requirements have been satisfied, run either **linux_conf.py** or
**mac_conf.py** if your system is UNIX/Linux or Mac respectively.

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

Regardless of your OS run test.py to confirm your system is properly configured
and everything works

Success

```md
$ python3 test.py
Built in modules imported successfully.

External dependencies successfully imported

******************************
	TEST PASSED
******************************

```

Failure.

```md
$ python3 test.py
Error in importing built in dependencies

Make sure os, sys, re, platform, json modules can be imported

Try reinstalling python3

******************************
	TEST FAILED
******************************
```

## Usage

After ensuring everything is set, fire up sci_hub.py

```md
$ python3 sci_hub.py -h
usage: sci_hub.py [-h] [-p P] [-b B] target

Sci-Hub downloader: Utility to download from Sci-Hub

positional arguments:
  target      URL/DOI to download PDF

optional arguments:
  -h, --help  show this help message and exit
  -p P        Absolute path to save files to (Default = ~/Downloads/sci_hub)
  -b B        Command to invoke browser
```

The different command line arguments accepted by the script are briefly explained.

### Target

This is either the complete URL or the DOI of the paper to be downloaded.

```md
Correct URL input 	: https://ieeexplore.ieee.org/document/1695678/
Incorrect URL input	: ieeexplore.ieee.org/document/1695678/
```

DOI is case-insensitive

```md
Correct DOI : 10.1109/MS.1987.229797
Correct DOI : 10.1109/ms.1987.229797
```

Example usage
```md
$ python3 sci_hub.py 10.1109/MS.1987.229797
$ python3 sci_hub.py https://ieeexplore.ieee.org/document/1695678/
```

### -b

This optional argument can be used to specify the command that needs to be
invoked to open the browser. This argument need not be specified if
**Mozilla Firefox** is installed and can be invoked with *firefox*

Whenever a captcha is encountered the script can automatically fire up the
browser and navigate to the download link.

```md
$ python3 sci_hub.py -b chrome 10.1109/MS.1987.229797
```

If this argument is not mentioned and a captcha is encountered, then the script
prints out the download link which can be opened in any browser directly.

### -h

This flag displays help message.

## Known issues

Though the script tries its best in doing its job is has few issues/limitations.
These are mentioned here.

* Proxy
  * None of the network transactions in the script are configured to run over
    proxy
  * If proxy is required, the user should manually alter the script for now.
    This will be fixed in a later update.

* Unexpected redirects
  * Sometimes sci-hub redirects requests to libgen and can lead to unexpected
	  errors.
  * If input was a URL, try by inputting the DOI
  * If the input was a DOI, then try prepending "http://dx.doi.org/" to the DOI.

An example of a failure due to redirection to libgen
```md
$ python3 sci_hub.py 10.1007/978-3-540-74496-2_36
Trying primary method.
URL from primary method is: https://sci-hub.tw/

Validating https://sci-hub.tw/
https://sci-hub.tw/ validated

Extracting download links...
Traceback (most recent call last):
  File "sci_hub.py", line 193, in <module>
    main()
  File "sci_hub.py", line 181, in main
    doi, mirror = get_links(url)
TypeError: 'NoneType' object is not iterable
```

Success by altering target
```md
$ python3 sci_hub.py http://dx.doi.org/10.1007/978-3-540-74496-2_36
Trying primary method.
URL from primary method is: https://sci-hub.tw/

Validating https://sci-hub.tw/
https://sci-hub.tw/ validated

Extracting download links...
Downloading paper...
Sending request
Response received. Analyzing...

Downloaded 0.32 MB

Files saved in ~/Downloads/sci_hub/ as 10.1007_978-3-540-74496-2_36.pdf
```

* DOI not assigned
  * The file is saved in PDF format by replacing "/" in
	  the respective DOI with '\_' in the mentioned path.
  * If DOI is not found then is is left as wuieobgefn.pdf in the mentioned path.

* Any issue that did not arise during development/testing.


## In case of issues with the script

This script is **NOT** meant to be used for python version 2.x

The scripts have been developed and thoroughly tested on the following platforms

* An Ubuntu 16.04 LTS machine running Python 3.5.2
* Arch Linux machine running Python 3.6.6

Thus it is assumed that the scripts should function properly on python 3.5+
provided the dependencies are proper. Functioning in Python 3 versions below
3.5 are also expected to work without any issues.

Still if there is any problem feel free to create an issue [here](https://github.com/gadilashashank/Sci-Hub/issues) by
mentioning the relevant details.
