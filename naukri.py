import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Get URL from user input
def getURL(job):
    urlString = "https://www.naukri.com/{}-jobs"
    job = job.lower().replace(' ', '-')
    url = urlString.format(job)
    return url


def main(job):
    url = getURL(job)

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-naukri.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        print("\033[94mLoading driver...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(15)

        # Parse URL into BeautifulSoup
        print("\033[94mLoading page...")
        driver.get(url)
        driver.find_elements(by=By.CLASS_NAME, value="job-description fs12 grey-text")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        response = soup.find(class_='list')

        jobArticles = response.find_all("article", class_="jobTuple bgWhite br4 mb-8")
        print("\033[94mWriting jobs...")

        # Get individual job details and write to file
        for job in jobArticles:
            job.find('a', class_='title fw500 ellipsis').get('href')
            jobTitle = job.find('a', class_='title fw500 ellipsis')
            jobCompany = job.find('a', class_='subTitle ellipsis fleft')
            jobLocation = job.find('li', class_='fleft grey-text br2 placeHolderLi location')
            jobDescription = job.find('div', class_='job-description fs12 grey-text')
            writer.writerow((jobTitle.text, jobCompany.text, jobLocation.span.string, jobDescription.text))
    print("\033[92mComplete")
                    # Example inputs


main("Singtel")