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

def main():
    printLogo()

    companyName = getCompanyName()

    print("\nExtracting data for " + companyName)
    print("\nPlease wait for the extraction process to complete...")

    getIndeed(companyName)
    getJDB(companyName)

    print("\nExtraction complete!")

main()