import webbrowser
import numpy as np
import pandas as pd
import os
import glob
from fontcolours import colours


def getFiles():
    path = os.getcwd()
    return glob.glob(os.path.join(path, "*.csv"))

def show():
    print(colours.BLUE + "Finding files..." + colours.ENDC)
    try:
        files = getFiles()
    except FileNotFoundError:
        print(colours.WARNING + "Files not found! Please run Extract Data first!" + colours.ENDC)
        return

    # If no output files are found
    if len(files) == 0:
        print(colours.FAIL + "\nPlease extract data for company first!" + colours.ENDC)
        return

    print(colours.GREEN + str(len(files)) + " files found!" + colours.ENDC)
    print(colours.BLUE + "Reading files..." + colours.ENDC)
    filenames = []
    tables = []
    allFrames = []

    try:
        for file in files:
            dataframe = pd.read_csv(file)
            dataframe.index = np.arange(1, len(dataframe)+1)

            filenames.append('File Name: ' + file.split("\\")[-1] + '\n')
            allFrames.append(dataframe)
    except OSError:
        print(colours.WARNING + "Error reading files. Please redo extract data and try again." + colours.ENDC)

    print(colours.BLUE + "Setting tables style...\n Generating tables" + colours.ENDC)
    for frame in allFrames:
        tables.append(frame.to_html(justify='left').replace('\\n', '<br>').replace('\\r', ''))

    print(colours.GREEN + "Tables generated" + colours.BLUE + "\nPrinting tables...\n" + colours.ENDC)
    try:
        with open('separated-database.html', 'w', encoding='utf-8') as f:
            for (filename, table) in zip(filenames, tables):
                f.write("<h1>Results from " + filename + "</h1>")
                f.write(table)
        webbrowser.open('file://' + os.path.realpath('separated-database.html'))
    except:
        print(colours.WARNING + "Error writing to file. Please ensure permissions is granted to the program.")
    print(colours.GREEN + "\nComplete!" + colours.ENDC)

def showTogether():
    print(colours.BLUE + "Finding files..." + colours.ENDC)
    try:
        files = getFiles()
    except FileNotFoundError:
        print(colours.WARNING + "Files not found! Please run Extract Data first!")
        return

    # If no output files are found
    if len(files) == 0:
        print(colours.FAIL + "\nPlease extract data for company first!" + colours.ENDC)
        return

    print(colours.BLUE + str(len(files)) + " files found." + colours.ENDC)
    print(colours.BLUE + "Reading files..." + colours.ENDC)
    allCsv = []

    try:
        for file in files:
            dataframe = pd.read_csv(file, header=0)
            allCsv.append(dataframe)
    except OSError:
        print(colours.WARNING + "Error reading files. Please redo extract data and try again." + colours.ENDC)
        return

    print(colours.BLUE + "Setting table style..." + colours.ENDC)
    allFrame = pd.concat(allCsv, axis=0, ignore_index=True)
    allFrame.index = np.arange(1, len(allFrame)+1)
    print(colours.BLUE + "Generating table...")
    table = allFrame.to_html(justify='left').replace('\\n', '<br>').replace('\\r', '')
    print(colours.GREEN + "Table generated" + colours.BLUE + "\nPrinting table...\n" + colours.ENDC)
    try:
        with open('combined-database.html', 'w', encoding='utf-8') as f:
            f.write("<h1>Results from all database</h1>")
            f.write(table)
        webbrowser.open('file://' + os.path.realpath('combined-database.html'))
    except:
        print(colours.WARNING + "Error writing to file. Please ensure permissions is granted to the program.")
        return
    print(colours.GREEN + "\nComplete!" + colours.ENDC)

def getCsvFiles():
    # Get CSV files in directory
    csvFiles = []
    
    for file in glob.glob("*.csv"):
        csvFiles.append(file)

    return csvFiles

#showTogether()
