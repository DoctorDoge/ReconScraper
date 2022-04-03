import csv
import requests
import re
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from fontcolours import colours

# Get URL from user input
def getURL(job, version):
    if version == 1:
        urlString = "https://www.indeed.com/jobs?q={}"
    elif version == 2:
        urlString = "https://sg.indeed.com/jobs?q={}"
    url = urlString.format(job)
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
        jobCompany = "Not Found"

    try:
        # Check if "+ location" is in span
        jobLocation = soup.find_all("div", "companyLocation")[num].text
        jobLocation = re.sub('\+.*','',jobLocation)
    except IndexError:
        jobLocation = "Not Found"

    try:
        jobDescription = soup.find_all("div", "job-snippet")[num].text.strip()
    except IndexError:
        jobDescription = "Not Found"

    jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)
    
    return jobEntry

def writeToFile(writer, url, version):
    while True: 
        # Parse URL into BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        jobTitleDiv = soup.find_all("div", "heading4")
        
        # Check if company can be found
        if len(jobTitleDiv) == 0:
            return 

        # Parse all job entries on page
        for x in range(len(jobTitleDiv)):
            jobEntry = getJobEntry(jobTitleDiv, soup, x)
            writer.writerow(jobEntry)
            
        try:
            if version == 1:
                url = "https://www.indeed.com" + soup.find('a', {"aria-label": "Next"}).get("href")
            else:
                url = "https://sg.indeed.com" + soup.find('a', {"aria-label": "Next"}).get("href")
            sleep(randint(1,8))
        except AttributeError:
            break

# Output user input to file
def getIndeed(job):
    intUrl = getURL(job, 1)
    sgUrl = getURL(job, 2)

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-indeed.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
        writer.writerow(header)

        # Write international and SG versions to file
        intWrite = writeToFile(writer, intUrl, 1)
        sgWrite = writeToFile(writer, sgUrl, 2)

        if intWrite is None and sgWrite is None:
            print(colours.FAIL + "\nCompany cannot be found in Indeed!" + colours.ENDC)
        else:
            print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)
