import csv
import requests
import re
from bs4 import BeautifulSoup

def getURL(job, location):
  urlString = "https://sg.indeed.com/jobs?q={}&l={}"
  url = urlString.format(job, location)
  return url

def getJobEntry(jobTitleDiv, soup, num):
  # Check if "new" is in span
  try:
    jobTitle = jobTitleDiv[num].h2.find_all('span')[1].text
  except IndexError:
    jobTitle = jobTitleDiv[num].h2.find_all('span')[0].text

  jobCompany = soup.find_all("span", "companyName")[num].text

  # Check if "+ location" is in span
  jobLocation = soup.find_all("div", "companyLocation")[num].text
  jobLocation = re.sub('\+.*','',jobLocation)

  jobDescription = soup.find_all("div", "job-snippet")[num].text.strip()
  jobEntry = (jobTitle, jobCompany, jobLocation, jobDescription)
  
  return jobEntry

def main(job, location):
  url = getURL(job, location)

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  jobTitleDiv = soup.find_all("div", "heading4")
  
  for x in range(len(jobTitleDiv)):
    jobEntry = getJobEntry(jobTitleDiv, soup, x)
    print(jobEntry)

main("retail", "singapore")