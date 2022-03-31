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

word = ["analyst", "test"]

# Open CSV file
with open("output-indeed.csv", encoding="utf-8") as file:
    csvString = file.read()
csvString = repr(csvString)
csvString = csvString.replace("\\n", "")

wordList = []
techList = ""

# Extract technology keywords
for i in word:
    tech = re.findall(i, csvString, re.IGNORECASE)
    wordList.append(tech)

# Covert list to string
for i in wordList:
    for x in i:
        techList += x + ", "

# Generate word cloud
wordcloud = WordCloud().generate(techList)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()