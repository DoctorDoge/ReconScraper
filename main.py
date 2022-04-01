import os
from indeed import getIndeed
from jdb import getJDB
from naukri import getNaukri
import os
import display
import glob

from fontcolours import colours
from wcloud import generateWordCloud

def printLogo():
    print(colours.CYAN + "----------------------------------------------------------")
    print(colours.GREEN + "  ___ ___ ___ ___  _  _   ___  ___ ___    _   ___ ___ ___ ")
    print(" | _ \ __/ __/ _ \| \| | / __|/ __| _ \  /_\ | _ \ __| _ \\")
    print(" |   / _| (_| (_) | .` | \__ \ (__|   / / _ \|  _/ _||   /")
    print(" |_|_\___\___\___/|_|\_| |___/\___|_|_\/_/ \_\_| |___|_|_\\")
    print("                                                          ")
    print(colours.CYAN + "----------------------------------------------------------" + colours.ENDC)
    print("\n")

# Ensure correct company output is read
def deleteOutputFiles():
    dirName = os.getcwd()
    dirFiles = os.listdir(dirName)
    
    for file in dirFiles:
        if file.endswith(".csv"):
            os.remove(os.path.join(dirName, file))

# Get company name from user input
def getCompanyName():
    companyName = ""

    while True:
        if companyName == "":
            companyName = input("Input company name to begin reconnaissance: ")
            if companyName != "":
                break
            else:
                print(colours.WARNING + "\nCompany name cannot be empty!" + colours.ENDC)

    return companyName

def printActions():
    print("---------------")
    print("Actions")
    print("1. Extract data")
    print("2. Display data")
    print("3. Generate technology graph")
    print("4. Generate technology word cloud")
    print("5. Exit")
    print("---------------")

# Get action from user input
def mainMenu(companyName):    

    while True:
        printActions()
        inputNumber = input("Please select action: ")
        if inputNumber == "1":
            extractData(companyName)
        elif inputNumber == "2":
            #print("Display data")
            showDataOptions(companyName)
        elif inputNumber == "3":
            print("Graphs")
        elif inputNumber == "4":
            generateWordCloud()
        elif inputNumber == "5":
            quit()    
        elif inputNumber == "":
            print(colours.WARNING + "\nInput cannot be empty!" + colours.ENDC)
        else:
            print(colours.WARNING + "\nInvalid input!" + colours.ENDC)


def printDataOptions():
    print("------------")
    print("Options")
    print("1. All-in-One")
    print("2. Separated by Database")
    print("3. Back to main menu")
    print("4. Exit")
    print("------------")


def showDataOptions(companyName):
    while True:
        printDataOptions()
        inputNumber = input("Please select action: ")
        if inputNumber == "1":
            display.showTogether()
        elif inputNumber == "2":
            display.show()
        elif inputNumber == "3":
            mainMenu(companyName)
        elif inputNumber == "4":
            quit()
        elif inputNumber == "":
            print(colours.WARNING + "\nInput cannot be empty!" + colours.ENDC)
        else:
            print(colours.WARNING + "\nInvalid input!" + colours.ENDC)


def printDatabases():
    print("------------")
    print("Databases")
    print("1. Indeed")
    print("2. JobsDB")
    print("3. Glassdoor")
    print("4. Naukri")
    print("5. Back to main menu")
    print("6. Exit")
    print("------------")

# Get data source from user input
def extractData(companyName):

    while True:
        printDatabases()
        inputNumber = input("Please select database to extract from: ")
        if inputNumber == "1":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "Indeed" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getIndeed(companyName)
            print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)
            mainMenu(companyName)

        elif inputNumber == "2":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "JobsDB" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getJDB(companyName)
            print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)
            mainMenu(companyName)

        elif inputNumber == "3":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "Glassdoor" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)
            mainMenu(companyName)

        elif inputNumber == "4":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "Naukri" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getNaukri(companyName)
            print(colours.GREEN + "\nExtraction complete!" + colours.ENDC)
            mainMenu(companyName)

        elif inputNumber == "5":
            mainMenu(companyName)    
        elif inputNumber == "6":
            quit()       
        elif inputNumber == "":
            print(colours.WARNING + "\nInput cannot be empty!" + colours.ENDC)
        else:
            print(colours.WARNING + "\nInvalid input!" + colours.ENDC)


def clearExistingCsvs():
    path = os.getcwd()
    for file in glob.glob(os.path.join(path, "*.csv")):
        os.remove(file)

def main():
    printLogo()
    # clearExistingCsvs()
    companyName = getCompanyName()
    mainMenu(companyName)

main()