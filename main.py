import os
from indeed import getIndeed
from jdb import getJDB
from glassdoor import getGlassdoor
from naukri import getNaukri
import os
import display
import glob
from display import getFiles, getCsvFiles
from fontcolours import colours
from generatetechnologies import generateGraph, generateWordCloud, displayTop10Technologies, displayAllTechnologies

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
    print("--------------------------------------")
    print("Actions")
    print("1. Extract data")
    print("2. Open as CSV")
    print("3. Open as HTML")
    print("4. Display top 10 technologies")
    print("5. Display all technologies")
    print("6. Generate graph of technologies")
    print("7. Generate word cloud of technologies")
    print("8. Exit")
    print("--------------------------------------")

# Get action from user input
def mainMenu(companyName):    

    while True:
        printActions()
        inputNumber = input("Please select action: ")
        if inputNumber == "1":
            extractData(companyName)
        elif inputNumber == "2":
            showFileOptions(companyName)
        elif inputNumber == "3":
            showDataOptions(companyName)
        elif inputNumber == "4":
            displayTop10Technologies()  
        elif inputNumber == "5":
            displayAllTechnologies()     
        elif inputNumber == "6":
            generateGraph()
        elif inputNumber == "7":
            generateWordCloud()
        elif inputNumber == "8":
            quit()    
        elif inputNumber == "":
            print(colours.WARNING + "\nInput cannot be empty!" + colours.ENDC)
        else:
            print(colours.WARNING + "\nInvalid input!" + colours.ENDC)

def printFileOptions():
    count = 1
    csvFiles = getCsvFiles()
    
    print("------------")
    print("Options")

    # Print existing CSV files in directory dynamically
    for file in csvFiles:
        print(str(count) + ". " + file)
        count += 1

    print(str(count) + ". Back to main menu" )
    count += 1
    print(str(count) + ". Quit" )

    print("------------")

def showFileOptions(companyName):
    while True:

        # Check if CSV files exist
        if len(getCsvFiles()) == 0:
            print(colours.FAIL + "\nPlease extract data for company first!" + colours.ENDC)
            mainMenu(companyName)

        printFileOptions()
        inputFile = input("Please select file: ")

        if int(inputFile) == len(getCsvFiles()) + 1:
            mainMenu(companyName)
        elif int(inputFile) == len(getCsvFiles()) + 2:
            quit()

        try:
            # Open existing CSV files in directory
            for i in range(len(getCsvFiles())):
                if int(inputFile) == i + 1:
                    os.startfile(os.getcwd() + "\\"+ getCsvFiles()[i])
                    print(colours.GREEN + "\n" + getCsvFiles()[i] + " opened!" + colours.ENDC)
                    mainMenu(companyName)
        except:
            if inputFile == "":
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
            mainMenu(companyName)

        elif inputNumber == "2":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "JobsDB" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getJDB(companyName)
            mainMenu(companyName)

        elif inputNumber == "3":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "Glassdoor" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getGlassdoor(companyName)
            mainMenu(companyName)

        elif inputNumber == "4":

            print(colours.BLUE + "\nExtracting data for " + companyName + " from " + "Naukri" + colours.ENDC)
            print(colours.CYAN + "\nPlease wait for the extraction process to complete... This process might take a while..." + colours.ENDC)
            getNaukri(companyName)
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
    # Enable font colours
    os.system("Color 00")
    
    printLogo()
    # clearExistingCsvs()
    companyName = getCompanyName()
    mainMenu(companyName)

main()