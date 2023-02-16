# GTFObinscraper

This Python script scrapes the GTFObins website and searches for binaries that match a user-supplied string. Once a match is found, the script fetches the associated code snippet from the website and displays it on the command line.
Requirements

Python 3.x
requests library (pip install requests)
BeautifulSoup library (pip install beautifulsoup4)

Usage

bash:

    ./program.py string_to_match

string_to_match should be a string that you want to search for within the GTFObins binaries.

For example, to search for binaries that match the string "sudo", you would run:

bash"

    ./program.py sudo

Output

The script outputs the binary path, followed by the associated code snippet from the GTFObins website, for each match that is found.

Notes

The script requires an internet connection to scrape the GTFObins website.
The script only matches the last word in each line of the user-supplied string with the last part of each binary path. If you need to match a full path, you can modify the script accordingly.
The script does not handle sudo commands correctly. If a binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
