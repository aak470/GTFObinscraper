#!/usr/bin/env python3

import sys
import os
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: ./program.py string_to_match")
    sys.exit()

# get string to match from user input
string_to_match = sys.argv[1]

# scrape GTFObins website
url = 'https://gtfobins.github.io/'
print(f"Fetching {url}...")
response = requests.get(url)
print(f"Response: {response}")
soup = BeautifulSoup(response.content, 'html.parser')

# extract binary paths and links
binaries = {}
for table in soup.find_all('table'):
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) > 1:
            binary = tds[0].text.strip()
            link = tds[0].find('a').get('href')
            binaries[binary] = link

print(f"\nFound {len(binaries)} binaries.")

# match last word in user input with last part of each binary path
matches = []
for binary in binaries.keys():
    binary_last_word = os.path.basename(binary)
    for line in string_to_match.split('\n'):
        user_last_word = line.strip().split('/')[-1]
        if binary_last_word == user_last_word:
            matches.append(binary)

print(f"\nFound {len(matches)} matches:")
for match in matches:
    link = f"{url.rstrip('/')}/{binaries[match].lstrip('/')}"
    print(f"Fetching {link}...")
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    code = soup.find('code').text.strip()
    print(f"\n{match}\n{code}\n{'-'*80}\n")
