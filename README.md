# ChangeLog
* [x] fix URL issue: all URLs in contents start with `//`
* [x] Add proxy to `requests`, test only default `socks5://127.0.0.1:1080`, `requests` must be proxy supported version.

**Origin README from gadilashashank/Sci-Hub**

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f10b5a4f5f73497399d175f613824574)](https://www.codacy.com/app/shashankgadila/Sci-Hub?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gadilashashank/Sci-Hub&amp;utm_campaign=Badge_Grade)
![Version 2.3](https://img.shields.io/badge/Version-2.3-brightgreen.svg)
![Release 5September, 2018](https://img.shields.io/badge/Release-5September,2018-8000bf.svg)
![License AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-00688B.svg)
![Version 2.2](https://img.shields.io/badge/Version-2.2-brightgreen.svg)
![Release 17July, 2018](https://img.shields.io/badge/Release-17July,2018-8000bf.svg)
![License AGPL-3.0](https://img.shields.io/badge/Lincense-AGPL--3.0-00688B.svg)
![Author Gadila Shashank Reddy](https://img.shields.io/badge/Author-Gadila_Shashank_Reddy-0066cc.svg)

# Sci-Hub Downloader

## Disclaimer

This application is for educational purpose only. I do not take responsibility
of what you choose to do with this application.


## About

*Sci-Hub downloader* is a command line wrapper of Sci-Hub written in Python. You can use the script to download research articles from your terminal itself.  

Hope you find it useful.

## Installation

### Windows

This application is not designed/tested to run on Windows machines natively . So if you are using Windows either you need to modify the script to run natively, or in a Virtual Machine with any Linux OS, installed or on Windows Subsystem for Linux.


### GNU/Linux

If you are using a Linux system, simply run the *configure.sh*, which is a bash script
that tries to install all the dependencies. Currently, this script can
automatically configure systems which use **apt, dnf, pacman or slackpkg**
as their package managers.

```md
sudo bash configure.sh
```

Otherwise refer REQUIREMENTS.md file and manually install the mentioned dependencies.

### MacOS

Run the following commands
* Install Homebrew

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

Next run configure.sh file or the following command. I'm not sure if sudo is
required.

```md
pip3 install requests beautifulsoup4 lxml
```

Regardless of OS, run the *test.py* file as mentioned below to ensure that
everything works properly.
Make sure you can spot the success message in the output.

Sample output
```md
$ python3 test.py https://google.com
This is a test file and does nothing.

**************************************************
YOUR TEST IS ALREADY SUCCESSFUL
The next output is to satisfy Codacy :/

You can safely ignore the output next
**************************************************

[SOME DEBUG OUTPUT COMES HERE]

```

If you don't get a similar success message as shown above then try to solve the
problem by reading the error messages before filing a bug report.

## A word

Friendly warnings are printed whenever the script is used in an unexpected manner.
It is therefore advised to read these errors properly and take appropriate action.

If you feel any such warning is a mistake, please create an issue
[here.](https://github.com/gadilashashank/Sci-Hub/issues)

An example warning

```md
$ python2 sci_hub.py
This script is NOT compatible with Python 2.x
Use this command to run the script:

python3 sci_hub.py
```

## Usage

After ensuring everything is set, fire up sci_hub.py

```md
$ python3 sci_hub.py -h
usage: sci_hub.py [-h] [--view] target

Sci-Hub downloader: Utility to download from Sci-Hub

positional arguments:
  target      URL/DOI to download PDF

optional arguments:
  -h, --help  show this help message and exit
  --view      Open article in browser for reading
```

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
$ python3 sci_hub.py --view 10.1109/MS.1987.229797
```

### -h

This flag displays help message.

### --view

This optional flag specifies the script to open the article in a browser window without downloading.

### Using the script over proxy

```
BACKWARDS INCOMPATIBILITY ALERT!!!
This feature is depreciated.
```

In the previous version there was a separate file to specify proxy configurations for all network transactions. From current version onwards this feature is reverted/depreciated because it clashed with system proxy settings.

From v2.2 onwards to use the script over proxy, specify proxy environment variables or make appropriate changes to your system's proxy settings.

### Download/storage

If the script downloads an article, its location is printed. By default all files are downloaded to a Downloads folder in the working directory of the script.

```md
Downloaded 0.32 MB

Files saved at ./Downloads/10.1007_978-3-540-74496-2_36.pdf
```

### Updating to newer versions

A simple ```git pull``` from the cloned repository should do the trick.



## Known issues

Though the script tries its best in doing its job is has few issues/limitations.
These are mentioned here.

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
Mirror not found
DOI not found
Download link not available
Please try after sometime
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

Files saved at ./Downloads/10.1007_978-3-540-74496-2_36.pdf

Thanks for using.
```

* Any issue that did not arise during development/testing.


## In case of issues with the script

This script is **NOT** meant to be used for python version 2.x

The scripts have been developed and thoroughly tested on the following platforms

* An Ubuntu 16.04 LTS machine running Python 3.5.2
* Arch Linux machine running Python 3.6.6 and 3.7.0

Thus it is assumed that the scripts should function properly on python 3.5+
provided the dependencies are proper. Functioning in Python 3 versions below
3.5 are also expected to work without any issues.

Still if there is any problem feel free to create an issue
[here](https://github.com/gadilashashank/Sci-Hub/issues) by mentioning the
relevant details.

While reporting a bug please include the complete output after running test.py
The output prints out some system related information **none** of which can be
used to individually identify the user. This information is required **only** for
debugging purposes and nothing beyond that whatsoever.
