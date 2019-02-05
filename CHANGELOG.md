# CHANGELOG

This summarizes various changes made to the script over the versions


## v1.0 (24th June, 2018)

* Initial release.

### To do

* Captcha workaround.
* Add support for proxy.

## v2.0 (14th July, 2018)

I know right? What Initially started as v1.1 eventually became v2.0 because of
the radical changes made to the codebase.

In this version every file has been radically changed and a summary is given.

* This changelog has been added.
* Some platform checks and warnings have been added in every executable.
* User input has been replaced by command line arguments.
* Captcha problem has been addressed.
* Documentation was re-written to update changes.
* A requirements file was added with every dependency listed.

### To do

* Add support for proxy.
* Take care of redirects

## v2.1 (17th July, 2018)

Technically this update should have been named as v3.0

Ok, so this is the first update to the application and trust me, it's a very huge
one.

Changes in this version include

* Proxy support added for the main script. Configuration scripts **don't**
  support proxy.

* Add badges to README.

* Include Codacy for code review.

* Decrease code complexity by using built-in modules and getting rid of all
  command line options as a result. Except the input DOI/URL ofc

* test.py now has dual purpose: it checks for errors and prints out useful
  data for debugging purposes only.

Instructions to setup proxy can be found in the proxy.py file in the form
of comments or contact your system administrator for help in setting it up.

## v2.2 (17th July, 2018)

Today's been a long day, I mean two updates on the same day?

* This version includes a software update tool(meh), a python script to pull
  from remote repository by comparing version numbers.

## v.2.3 (5th 5 September, 2018)

This change log thing is a bit boring,,, maybe I gotta hire a writer? :P Anyways

**Backwards incompatibility arises in this release.**

* Proxy configuration depends on system/environment settings
* --view optional flag to view articles without downloading
* Faster retrieval of DOI and Download links
* Made the testing/debugging script more useful. (Again no personal data collected)

[@DCMMC](https://github.com/DCMMC), Feb 5, 2019

* [x] fix URL issue: all URLs in contents start with `//`, e.g., `//sci-hub.tw/cite/10.1016/S1361-3723(17)30089-1`
* [x] Add proxy to `requests`, test only default `socks5://127.0.0.1:1080`, `requests` must be proxy supported version. (`TODO`: test)
* [x] fix URL protocol issue in Google search result, e.g. URL in results is `sci-hub.tw/` instead of `http://sci-hub.tw/`
