#!/usr/bin/env python3

'''
Asrock B650E PG Riptide BIOS update checker written (mostly) by GPT4
'''

# import requests and BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import json
from win10toast import ToastNotifier

# define the URL to scrape
url = "https://pg.asrock.com/mb/AMD/B650E%20PG%20Riptide%20WiFi/index.asp#BIOS"

# create a webdriver object with headless option
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

# load the page with Selenium
driver.get(url)

# get the HTML source code
html = driver.page_source

# close the driver
driver.quit()

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

div = soup.find("div", class_='Support', id='BIOS')

# find the table element that contains the BIOS versions
table = div.find("table")

# find the first row of the table (the header row)
latest_bios_ver_td = table.find("td")

bios_version = latest_bios_ver_td.text

print(f'Current latest BIOS: {bios_version}')

# load the previous bios version from a json file (or set it to None if not found)
try:
    with open("bios_version.json", "r") as f:
        previous_bios_version = json.load(f)
except FileNotFoundError:
    previous_bios_version = None

# compare the current and previous bios versions
if bios_version != previous_bios_version:
    # save the current bios version to a json file
    with open("bios_version.json", "w") as f:
        json.dump(bios_version, f)

    # display a toast notification using win10toast
    toaster = ToastNotifier()
    toaster.show_toast(
        "Bios Update", f"The bios version has changed from {previous_bios_version} to {bios_version}", icon_path=None, duration=10)
else:
    # do nothing if the bios version has not changed
    pass
