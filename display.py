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

        filenames.append('File Name: ' + file.split("\\")[-1] + '\n')
        allFrames.append(dataframe)

    print(colours.BLUE + "Setting tables style..." + colours.ENDC)
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    print(colours.BLUE + "Generating tables...")
    for frame in allFrames:
        tables.append(tabulate(frame, headers='keys', tablefmt='fancy_grid'))

    print(colours.GREEN + "Tables generated" + colours.BLUE + "\nPrinting tables...\n" + colours.ENDC)
    for (filename, table) in zip(filenames, tables):
        print(filename + table)
    print(table + colours.GREEN + "\nComplete!" + colours.ENDC)

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
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    print(colours.BLUE + "Generating table...")
    table = tabulate(allFrame, headers='keys', tablefmt='fancy_grid')
    print(colours.GREEN + "Table generated" + colours.BLUE + "\nPrinting table...\n" + colours.ENDC)
    print(table + colours.GREEN + "\nComplete!" + colours.ENDC)

#show()
