import webbrowser

import numpy as np
import pandas as pd
import os
import glob

from tabulate import tabulate

from fontcolours import colours


def getFiles():
    path = os.getcwd()
    return glob.glob(os.path.join(path, "*.csv"))

def show():
    print(colours.BLUE + "Finding files..." + colours.ENDC)
    files = getFiles()
    print(colours.GREEN + str(len(files)) + " files found!" + colours.ENDC)
    print(colours.BLUE + "Reading files..." + colours.ENDC)
    filenames = []
    tables = []
    allFrames = []

    for file in files:
        dataframe = pd.read_csv(file)
        dataframe.index = np.arange(1, len(dataframe)+1)

        filenames.append('File Name: ' + file.split("\\")[-1] + '\n')
        allFrames.append(dataframe)

    print(colours.BLUE + "Setting tables style..." + colours.ENDC)
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    print(colours.BLUE + "Generating tables...")
    for frame in allFrames:
        tables.append(tabulate(frame, headers='firstrow', tablefmt='fancy_grid'))

    print(colours.GREEN + "Tables generated" + colours.BLUE + "\nPrinting tables...\n" + colours.ENDC)
    for (filename, table) in zip(filenames, tables):
        print(filename + table)
    with open('temp.html', 'w', encoding='utf-8') as f:
        for (filename, frame) in zip(filenames, allFrames):
            f.write("<h1>Results from: " + filename + "</h1>")
            f.write(frame.to_html(justify='left'))
    webbrowser.open('file://' + os.path.realpath('temp.html'))
    print(colours.GREEN + "\nComplete!" + colours.ENDC)

def showTogether():
    print(colours.BLUE + "Finding files..." + colours.ENDC)
    files = getFiles()
    print(colours.BLUE + str(len(files)) + " files found." + colours.ENDC)
    print(colours.BLUE + "Reading files..." + colours.ENDC)
    allCsv = []

    for file in files:
        dataframe = pd.read_csv(file, header=0)
        allCsv.append(dataframe)

    print(colours.BLUE + "Setting table style..." + colours.ENDC)
    allFrame = pd.concat(allCsv, axis=0, ignore_index=True)
    allFrame.index = np.arange(1, len(allFrame)+1)
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    print(colours.BLUE + "Generating table...")
    table = tabulate(allFrame, headers='firstrow', tablefmt='fancy_grid')
    print(colours.GREEN + "Table generated" + colours.BLUE + "\nPrinting table...\n" + colours.ENDC)
    with open('temp.html', 'w', encoding='utf-8') as f:
        f.write("<h1>Results from all database</h1>")
        f.write(allFrame.to_html(classes='table table-striped'))
    webbrowser.open('file://' + os.path.realpath('temp.html'))
    print(table + colours.GREEN + "\nComplete!" + colours.ENDC)

def getCsvFiles():
    # Get CSV files in directory
    csvFiles = []
    
    for file in glob.glob("*.csv"):
        csvFiles.append(file)

    return csvFiles

#show()
