import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from fontcolours import colours


# Get URL from user input
def getURL(job):
    urlString = "https://www.naukri.com/{}-jobs"
    job = job.lower().replace(' ', '-')
    url = urlString.format(job)
    return url


def getNaukri(job):
    url = getURL(job)

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-naukri.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        i = 1
        while True:
            print(colours.BLUE + "Loading driver..." + colours.ENDC)
            sleep(0.1)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.implicitly_wait(5)
            # Parse URL into BeautifulSoup
            print(colours.BLUE + "Loading page..." + colours.ENDC)
            driver.get(url + "-" + str(i))
            driver.find_elements(by=By.CLASS_NAME, value="job-description fs12 grey-text")
            if driver.current_url == url and i != 1:
                break
            soup = BeautifulSoup(driver.page_source, "html.parser")
            response = soup.find(class_='list')

            jobArticles = response.find_all("article", class_="jobTuple bgWhite br4 mb-8")
            driver.close()
            print(colours.BLUE + "Writing jobs..." + colours.ENDC)
            # Get individual job details and write to file
            for job in jobArticles:
                job.find('a', class_='title fw500 ellipsis').get('href')
                jobTitle = job.find('a', class_='title fw500 ellipsis')
                jobCompany = job.find('a', class_='subTitle ellipsis fleft')
                jobLocation = job.find('li', class_='fleft grey-text br2 placeHolderLi location')
                jobDescription = job.find('div', class_='job-description fs12 grey-text')
                writer.writerow((jobTitle.text, jobCompany.text, jobLocation.span.string, jobDescription.text))
            i += 1
    print(colours.GREEN + "Complete" + colours.ENDC)
                    # Example inputs


# getNaukri("Singtel")