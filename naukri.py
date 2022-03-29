import csv
from bs4 import BeautifulSoup
from selenium import webdriver


# Get URL from user input
def getURL(job, location):
    urlString = "https://www.naukri.com/{}-jobs-in-{}/"
    job = job.replace(' ', '-')
    location = location.replace(' ', '-')
    url = urlString.format(job, location)
    return url


def main(job, location):
    url = getURL(job, location)

    header = ["Job Title", 'Company', 'Location', 'Job Description']

    # Save output to CSV file
    with open('output-naukri.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        driver = webdriver.Chrome("chromedriver.exe")

        # Parse URL into BeautifulSoup
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        response = soup.find(class_='list')

        jobArticles = response.find_all("article", class_="jobTuple bgWhite br4 mb-8")

        # Get individual job details and write to file
        for job in jobArticles:
            job.find('a', class_='title fw500 ellipsis').get('href')
            jobTitle = job.find('a', class_='title fw500 ellipsis')
            jobCompany = job.find('a', class_='subTitle ellipsis fleft')
            jobLocation = job.find('li', class_='fleft grey-text br2 placeHolderLi location')
            jobDescription = job.find('div', class_='job-description fs12 grey-text')
            writer.writerow((jobTitle.text, jobCompany.text, jobLocation.span.string, jobDescription.text))
                    # Example inputs


main("c programmer", "singapore")