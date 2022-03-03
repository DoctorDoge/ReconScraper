import csv
import requests
import re
from bs4 import BeautifulSoup
from random import randint
from time import sleep

# Get URL from user input
def getURL(job, location):
    urlString = "https://sg.indeed.com/jobs?q={}&l={}"
    url = urlString.format(job, location)
    return url

# Get individual job entry
def getJobEntry(jobTitleDiv, soup, num):
    # Check if "new" is in span
    try:
        jobTitle = jobTitleDiv[num].h2.find_all('span')[1].text
    except IndexError:
        jobTitle = jobTitleDiv[num].h2.find_all('span')[0].text

    try:
        jobCompany = soup.find_all("span", "companyName")[num].text
    except IndexError:
        jobCompany = ""

    try:
        # Check if "+ location" is in span
        jobLocation = soup.find_all("div", "companyLocation")[num].text
        jobLocation = re.sub('\+.*','',jobLocation)
    except IndexError:
        jobLocation = ""

    try:
        jobDescription = soup.find_all("div", "job-snippet")[num].text.strip()
    except IndexError:
        jobDescription = ""

    jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)
    
    return jobEntry

def main(job, location):
    url = getURL(job, location)

    while True: 
        # Parse URL into BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        jobTitleDiv = soup.find_all("div", "heading4")
        
        # Parse all job entries on page
        for x in range(len(jobTitleDiv)):
            jobEntry = getJobEntry(jobTitleDiv, soup, x)
            print(jobEntry)
        
        try:
            url = "https://sg.indeed.com" + soup.find('a', {"aria-label": "Next"}).get("href")
            sleep(randint(1,8))
        except AttributeError:
            break

main("chief executive officer", "ang mo kio")