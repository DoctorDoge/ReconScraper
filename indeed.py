import csv
import requests
import re
from bs4 import BeautifulSoup

# Get URL from user input
def getURL(job, location):
    urlString = "https://sg.indeed.com/jobs?q={}&l={}"
    url = urlString.format(job, location)
    return url

# Get individual job entry
def getJobEntry(jobTitleDiv, soup, num):
    # Check if "new" is in span
    try:
        try:
            jobTitle = jobTitleDiv[num].h2.find_all('span')[1].text
        except IndexError:
            jobTitle = jobTitleDiv[num].h2.find_all('span')[0].text
    except AttributeError:
        jobTitle = ""

    try:
        jobCompany = soup.find_all("span", "companyName")[num].text
    except AttributeError:
        jobCompany = ""

    try:
        # Check if "+ location" is in span
        jobLocation = soup.find_all("div", "companyLocation")[num].text
        jobLocation = re.sub('\+.*','',jobLocation)
    except AttributeError:
        jobLocation = ""

    try:
        jobDescription = soup.find_all("div", "job-snippet")[num].text.strip()
    except AttributeError:
        jobDescription = ""

    jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)
    
    return jobEntry

def main(job, location):
    url = getURL(job, location)

    # Parse URL into BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobTitleDiv = soup.find_all("div", "heading4")
    
    # Parse all job entries on page
    for x in range(len(jobTitleDiv)):
        jobEntry = getJobEntry(jobTitleDiv, soup, x)
        print(jobEntry)

main("retail", "singapore")