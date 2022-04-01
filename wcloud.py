import glob
import os
import re
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from csv import reader
import matplotlib.pyplot as plt

# df = pd.read_csv("output-indeed.csv")
# print(df[(df['Job Title'].str.contains("analyst", case=False)) | (df['Job Description'].str.contains("Challenger", case=False))])

def getTechnologies():
    lines = []
    with open("technologies.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            lines.append(line)

    return lines

def getFileList():
    fileList = []
    path = os.getcwd()
    for file in glob.glob(os.path.join(path, "*.csv")):
        fileList.append(file)

    return fileList

def generateWordCloud():
    technologies = getTechnologies()
    fileList = getFileList()

    wordList = []
    techList = ""

    for file in fileList:
        # Open CSV file
        with open(file, encoding="utf-8") as file:
            csvString = file.read()
        csvString = repr(csvString)
        csvString = csvString.replace("\\n", "")

        # Extract technology keywords
        for i in technologies:
            tech = re.findall("\\b"+i+"\\b", csvString, re.IGNORECASE)
            if len(tech) != 0:
                wordList.append(tech)

    # Covert list to string
    for i in wordList:
        for x in i:
            techList += x + ", "
    
    if len(techList) != 0:
        # Generate word cloud
        wordcloud = WordCloud(collocations=False).generate(techList)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig("output-wordcloud.png", format="png")
        plt.show()

        print("Word cloud saved to output-wordcloud.png")
    else:
        print("Technologies cannot be found for company!")

generateWordCloud()