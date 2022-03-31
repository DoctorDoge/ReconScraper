import csv
import requests
import re
from bs4 import BeautifulSoup
from random import randint
from time import sleep

# Get URL from user input
def getURL(job, location, locationID, version):
    job = job.replace(" ", "-")
    if locationID == "":
        if version == 1:
            urlString = "https://www.glassdoor.com/Job/{}-jobs-SRCH_KO0,{}.htm"
        elif version == 2:
            urlString = "https://www.glassdoor.sg/Job/{}-jobs-SRCH_KO0,{}.htm"
        url = urlString.format(job, len(job))
    else:
        if version == 1:
            urlString = "https://www.glassdoor.com/Job/{}-jobs-SRCH_IL.0,{}.htm"
        elif version == 2:
            urlString = "https://www.glassdoor.sg/Job/{}-jobs-SRCH_IL.0,{}.htm"
        location = location.replace(" ", "-")
        search = location + "-" + job
        url = urlString.format(search, locationID + "," + str(len(search)))
    return url

# Get individual job entry
def getJobEntry(jobTitleLi, version):
    #Get "a" tag containing job title
    entry = jobTitleLi.find("a",{"data-test":"job-link"})

    if entry == None:
        jobTitle = "Not Found"
    else:
        jobTitle = entry.span.text

    #Get div containing company and location
    jobTitleDiv = jobTitleLi.find("div","job-search-key-1mn3dn8")

    if jobTitleDiv == None:
        jobCompany = "Not Found"
        jobLocation = "Not Found"
    else:
        try:
            #Get div with company name
            jobCompany = jobTitleDiv.find_all('div')[0]
            #Get company name from span
            jobCompany = jobCompany.a.span.text
            if jobCompany == '':
                jobCompany = "Not Found"
        except (IndexError,AttributeError) as e:
            jobCompany = "Not Found"

        try:
            #Get div with job location
            jobLocation = jobTitleDiv.find_all('div')[2]
            #Get job location from span
            jobLocation = jobLocation.span.text
            if jobLocation == '':
                jobLocation = "Not Found"
        except (IndexError,AttributeError) as e:
            jobLocation = "Not Found"

    #To add code to retrieve job description
    #Retrieve link for job post
    if version == 1:
        url = "https://www.glassdoor.com" + entry.get("href")
    elif version == 2:
        url = "https://www.glassdoor.sg" + entry.get("href")

    #Set user agent and request for link
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=user_agent)
    soup = BeautifulSoup(response.text, "html.parser")

    #Get job description
    jobDescDiv = soup.find("div", {"id":"JobDescriptionContainer"})
    try:
        jobDescription = jobDescDiv.div.div.text
    except AttributeError:
        jobDescription = "Not Found"

    jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)

    return jobEntry
    
    
def getGlassdoor(job):
    url = getURL(job, "", "", 1)
    urlSG = getURL(job, "", "", 2)
    user_agent = {'User-Agent': 'Mozilla/5.0'}

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-glassdoor.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
        writer.writerow(header)
 
        # Parse URL into BeautifulSoup
        response = requests.get(url,headers=user_agent)
        soup = BeautifulSoup(response.text, "html.parser")

        jobTitleLi = soup.find_all("li", "react-job-listing")
        
        # Parse all job entries on page
        for x in range(len(jobTitleLi)):
            jobEntry = getJobEntry(jobTitleLi[x], 1)
            sleep(randint(1,2))
            writer.writerow(jobEntry)

        # Parse SG URL into BeautifulSoup
        response = requests.get(urlSG,headers=user_agent)
        soup = BeautifulSoup(response.text, "html.parser")

        jobTitleLi = soup.find_all("li", "react-job-listing")
        
        # Parse all job entries on page
        for x in range(len(jobTitleLi)):
            jobEntry = getJobEntry(jobTitleLi[x], 2)
            sleep(randint(1,2))
            writer.writerow(jobEntry)

# getGlassdoor("Singtel")
