import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from fontcolours import colours


# Get URL from user input
def getURL(companyName):
    urlString = "https://www.naukri.com/{}-jobs"
    companyName = companyName.lower().replace(' ', '-')
    url = urlString.format(companyName)
    return url


def getNaukri(companyName):
    url = getURL(companyName)

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-naukri.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\')
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
                print((colours.GREEN + "No more jobs" + colours.ENDC))
                break
            elif i == 1:
                url = driver.current_url
            soup = BeautifulSoup(driver.page_source, "html.parser")
            response = soup.find(class_='list')

            # Check if company can be found
            try:
                jobArticles = response.find_all("article", class_="jobTuple bgWhite br4 mb-8")
            except:
                print(colours.FAIL + "\nCompany cannot be found in Naukri!" + colours.ENDC)
                driver.close()
                return

            if len(response.find_all("article", class_="jobTuple bgWhite br4 mb-8")) != 0:
                jobArticles = response.find_all("article", class_="jobTuple bgWhite br4 mb-8")
            else:
                print(colours.FAIL + "\nCompany cannot be found in Naukri!" + colours.ENDC)
                driver.close()
                return

            driver.close()
            print(colours.BLUE + "Writing jobs..." + colours.ENDC)
            # Get individual job details and write to file
            for job in jobArticles:
                job.find('a', class_='title fw500 ellipsis').get('href')
                try:
                    jobTitle = job.find('a', class_='title fw500 ellipsis').text
                except:
                    jobTitle = "Not Found"
                try:
                    jobCompany = job.find('a', class_='subTitle ellipsis fleft').text
                except:
                    jobCompany = "Not Found"
                if not companyName.lower() in jobCompany.lower():
                    continue
                try:
                    jobLocation = job.find('li', class_='fleft grey-text br2 placeHolderLi location')
                except:
                    jobLocation = "Not Found"
                try:
                    jobDescription = job.find('div', class_='job-description fs12 grey-text').text
                except:
                    jobDescription = "Not Found"
                jobTagsList = job.find('ul', class_='tags has-description')
                jobTags = []
                for tag in jobTagsList.findAll('li'):
                    jobTags.append(tag.text)
                jobTags = ','.join(jobTags)
                jobDescription = jobDescription + "\nSkills: " + jobTags
                writer.writerow((jobTitle, jobCompany, jobLocation.span.string, jobDescription))
            i += 1

    print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)

