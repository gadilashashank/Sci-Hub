![Version 2.1](https://img.shields.io/badge/Version-2.1-brightgreen.svg)
![Release 16July, 2018](https://img.shields.io/badge/Release-16July,2018-8000bf.svg)
![License AGPL-3.0](https://img.shields.io/badge/Lincense-AGPL--3.0-00688B.svg)
![Author Gadila Shashank Reddy](https://img.shields.io/badge/Author-Gadila_Shashank_Reddy-0066cc.svg)

# Sci-Hub Downloader

## Disclaimer

This application is for educational purpose only. I do not take responsibility
of what you choose to do with this application.


## About

*Sci-Hub downloader* is a simple python script that attempts to automatically
download papers from sci-hub without the hassle of finding a working mirror or
going through multiple sites that are not legit sci-hub mirrors via a
*Command Line Interface*.

Hope you like it!

## Installation

### Windows

This application is **NOT guaranteed** to work on Windows systems directly. It
is advised to run it on a *Windows subsystem for Linux* a.ka.
*Bash on Ubuntu on Windows* or on a Linux virtual machine. Please note that at
the time of writing this document none of these methods have been tested for
proper functioning.

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

[SOME OUTPUT COMES HERE]

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
usage: sci_hub.py [-h] target

Sci-Hub downloader: Utility to download from Sci-Hub

positional arguments:
  target      URL/DOI to download PDF

optional arguments:
  -h, --help  show this help message and exit
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
```

### -h

This flag displays help message.

### Using the script over proxy

If you want the script to send all requests via a proxy then you have to edit
the **proxy.py** file. By default all proxies are set to none. Relevant usage
instructions are mentioned in the file itself.

If you know that you need a proxy setting but don't know how to do so, it is
better if you contact your system administrator.

None of the configuration files run on proxy. So you might need to set the
dependencies on a connection that does not need proxy.

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

Still if there is any problem feel free to create an issue
[here](https://github.com/gadilashashank/Sci-Hub/issues) by mentioning the
relevant details.

While reporting a bug please include the complete output after running test.py
The output prints out some system related information **none** of which can be
used to individually identify the user. This information is required **only** for 
debugging purposes and nothing beyond that whatsoever.
