# SeleniumCraigslist
A python script written using selenium package.

###Disclaimer:
This is just for demonstration purposes, it is not intended for use on actual Craigslist accounts.
This script simply shows the power of the Selenium Python package paired with chromedriver.
Any misuse or conduct violation lies with the user.

##Selenium
Selenium is a suite of tools that allows for browser automation.
It is mainly used for web application testing.

##Implementation
I have currently implemented it to allow a user to add their account information
for Craigslist. Then when run will log in and cycle through a users ads and renews them.
If combined with task runners such as windows scheduler, it can be set to automate this
process on a regular schedule.

##Setup
1. [Install Python 3.6](https://www.python.org/downloads/)
2. [Install chromedriver 2.27](https://sites.google.com/a/chromium.org/chromedriver/)
3. Run `pip install selenium` in the terminal for UNIX systems
   Run `py.exe -m install selenium` in command prompt for Windows
   Add `sudo` as necessary
4. Go into the `cl_renew.py` and edit the "email" and "password" fields leaving the quotation marks.
5. Run the file by double clicking or from terminal.
