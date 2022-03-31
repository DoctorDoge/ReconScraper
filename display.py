import pandas as pd
import os
import glob

from tabulate import tabulate


def show():
    path = os.getcwd()
    files = glob.glob(os.path.join(path, "*.csv"))

    for file in files:
        dataframe = pd.read_csv(file)

        print('Location: ', file)
        print('File Name: ', file.split("\\")[-1])

        print('Content: ')
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        print(tabulate(dataframe, headers='keys', tablefmt='fancy_grid'))

#show()
