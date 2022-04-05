# ReconScraper

## Contributors
| **Lee Zhi Yang Aloysius** | **Tse Kin Ping** | **Kee Zhong Yi** | **Cherie Teo Ing Ee** |
| :---: | :---: | :---: | :---: |
| 2001348 | 2001568 | 2000652 | 2002152 |

## System Architecture
![System Architecture](https://user-images.githubusercontent.com/72640752/161764487-13878965-7422-467c-a8bd-f1621f4920d3.png)

## Solution Details
The tool that can be run on the Windows command line and any IDE that supports Python Programming Language. 

The tool allows the input of a company name, then the user will be able to select the job site they want to scrape the data from: Indeed, JobsDB, Glassdoor or Naukri. The data scraped will be saved and can be displayed in the CSV or HTML formats.

Recon Scraper is able to display the top 10 or all technologies found.

![image](https://user-images.githubusercontent.com/72640752/161767145-7c61030f-d84a-4977-a72c-6c1cb7522380.png)

Recon Scraper can generate a graph or word cloud of technologies to represent the data graphically.

![image](https://user-images.githubusercontent.com/72640752/161767330-82ac1a98-94e1-4850-b724-483e3e09a769.png)

![image](https://user-images.githubusercontent.com/72640752/161767450-e0203772-9693-4ddb-8179-a2d3d0185199.png)

## Package Installation

```
pip install -r requirements.txt
```
Note: If the installation of the wordcloud package were to fail, please download the correct wheel file for your version of Python using the link below. To install the wheel file, run the command below. 

https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

```
pip install <wheel file>
```

## How To Run

### Using command line:
At the main directory of the repository
```
python main.py
```

### **OR**

### Using Python IDE: 
Run main.py
