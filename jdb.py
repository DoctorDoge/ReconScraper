import csv
import requests
import re
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from fontcolours import colours

# Get URL from user input
def getURL(job):
    job = job.replace(" ", "+")
    urlString = "https://sg.jobsdb.com/j?sp=search&q={}"
    url = urlString.format(job)
    return url

# Get individual job entry
def getJobEntry(jobTitleLi):
    
    #Get "a" tag containing job title
    entry = jobTitleLi.find("a","job-link")

    if entry == None:
        jobTitle = "Not Found"
    else:
        jobTitle = entry.text

    #Get div containing company and location
    jobTitleDiv = jobTitleLi.find_all('div')[3]

    if jobTitleDiv == None:
        jobCompany = "Not Found"
        jobLocation = "Not Found"
    else:
        try:
            #Get div with company name
            jobCompany = jobTitleDiv.find_all('span')[0]
            #Get company name from span
            jobCompany = jobCompany.text
            if jobCompany == '':
                jobCompany = "Not Found"
        except (IndexError,AttributeError) as e:
            jobCompany = "Not Found"

        try:
            #Get div with job location
            jobLocation = jobTitleDiv.find_all('span')[2]
            #Get job location from span
            jobLocation = jobLocation.text
            if jobLocation == '':
                jobLocation = "Not Found"
        except (IndexError,AttributeError) as e:
            jobLocation = "Not Found"

    #To add code to retrieve job description
    #Retrieve link for job post
    url = "https://sg.jobsdb.com/" + entry.get("href")

    #Set user agent and request for link
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=user_agent)
    soup = BeautifulSoup(response.text, "html.parser")

    #Get job description
    jobDescDiv = soup.find("div", {"id":"job-description-container"})
    try:
        jobDescription = jobDescDiv.text
    except AttributeError:
        jobDescription = "Not Found"

    jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)

    return jobEntry
    
    
def getJDB(job):
    url = getURL(job)
    user_agent = {'User-Agent': 'Mozilla/5.0'}

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open("output-jdb.csv", 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
        writer.writerow(header)
    
        while True:
            # Parse URL into BeautifulSoup
            response = requests.get(url,headers=user_agent)
            soup = BeautifulSoup(response.text, "html.parser")

            jobTitleLi = soup.find_all("article", "organic-job")
            
            # Check if company can be found
            if len(jobTitleLi) == 0:
                print(colours.FAIL + "\nCompany cannot be found in JobsDB!" + colours.ENDC)
                return

            # Parse all job entries on page
            for x in range(len(jobTitleLi)):
                jobEntry = getJobEntry(jobTitleLi[x])
                sleep(randint(1,2))
                writer.writerow(jobEntry)

            try:
                url = "https://sg.jobsdb.com/" + soup.find('a', "next-page-button").get("href")
                #sleep(randint(1,8))
            except AttributeError:
                break 

    print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)