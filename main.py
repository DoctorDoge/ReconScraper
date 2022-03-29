from indeed import getIndeed
from jdb import getJDB

def printLogo():
    print("----------------------------------------------------------")
    print("  ___ ___ ___ ___  _  _   ___  ___ ___    _   ___ ___ ___ ")
    print(" | _ \ __/ __/ _ \| \| | / __|/ __| _ \  /_\ | _ \ __| _ \\")
    print(" |   / _| (_| (_) | .` | \__ \ (__|   / / _ \|  _/ _||   /")
    print(" |_|_\___\___\___/|_|\_| |___/\___|_|_\/_/ \_\_| |___|_|_\\")
    print("                                                          ")
    print("----------------------------------------------------------")
    print("\n")

# Get company name from user input
def getCompanyName():
    companyName = ""

    while True:
        if companyName == "":
            companyName = input("Input company name to begin reconnaissance: ")
            if companyName != "":
                break
            else:
                print("\nCompany name cannot be empty!")

    return companyName

def printActions():
    print("---------------")
    print("Actions")
    print("1. Extract data")
    print("2. Display data")
    print("3. Exit")
    print("---------------")

# Get action from user input
def mainMenu(companyName):    

    while True:
        printActions()
        inputNumber = input("Please select action: ")
        if inputNumber == "1":
            extractData(companyName)
        elif inputNumber == "2":
            print("Display data")
        elif inputNumber == "3":
            quit()
        elif inputNumber == "":
            print("\nInput cannot be empty!")
        else:
            print("\nInvalid input!")  

def printDatabases():
    print("------------")
    print("Databases")
    print("1. Indeed")
    print("2. JobsDB")
    print("3. Glassdoor")
    print("4. Back to main menu")
    print("5. Exit")
    print("------------")

# Get data source from user input
def extractData(companyName):

    while True:
        printDatabases()
        inputNumber = input("Please select database to extract from: ")
        if inputNumber == "1":
            print("\nExtracting data for " + companyName + " from " + "Indeed")
            print("\nPlease wait for the extraction process to complete... This process might take a while...")
            getIndeed(companyName)
            print("\nExtraction complete!")
            mainMenu(companyName)
        elif inputNumber == "2":
            print("\nExtracting data for " + companyName + " from " + "JobsDB")
            print("\nPlease wait for the extraction process to complete... This process might take a while...")
            getJDB(companyName)
            print("\nExtraction complete!")
            mainMenu(companyName)
        elif inputNumber == "3":
            print("\nExtracting data for " + companyName + " from " + "Glassdoor")
            print("\nPlease wait for the extraction process to complete... This process might take a while...")
            print("\nExtraction complete!")
            mainMenu(companyName)
        elif inputNumber == "4":
            mainMenu(companyName)
        elif inputNumber == "5":
            quit()    
        elif inputNumber == "":
            print("\nInput cannot be empty!")
        else:
            print("\nInvalid input!")       

def main():
    printLogo()
    companyName = getCompanyName()
    mainMenu(companyName)

main()