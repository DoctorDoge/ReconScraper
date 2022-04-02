import glob
import os
import re
from typing import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

def generateTechList():
    technologies = getTechnologies()
    fileList = getFileList()
    
    # Check if output files exist
    if len(fileList) == 0:
        return "empty"

    wordList = []
    techString = ""

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
            techString += x + " "

    return techString
    
def generateGraph():
    techString = generateTechList()

    # If no output files are found
    if techString == "empty":
        print("Please extract data for company first!")
        return

    if len(techString) != 0:
        techString = techString.lower()
        words = techString.split()

        # Count word frequency
        wordCount = Counter(words)

        # Generate graph
        plt.bar(wordCount.keys(), wordCount.values())
        plt.xticks(rotation=90)
        plt.show()
    else:
        print("Technologies cannot be found for company!")

def generateWordCloud():
    techString = generateTechList()

    # If no output files are found
    if techString == "empty":
        print("Please extract data for company first!")
        return
    
    if len(techString) != 0:
        # Generate word cloud
        wordcloud = WordCloud(collocations=False).generate(techString)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
    else:
        print("Technologies cannot be found for company!")
