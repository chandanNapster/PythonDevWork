import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import re
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 8, 4

colList = []

fileName = '\\Dataset\\P4-Movie-Ratings.csv'
fileName2 = '\\Dataset\\P4-Demographic-Data.csv'

datasetLoc = os.getcwd() + fileName


def toUpperCase(wordList):
    colName = ''
# print(wordList.split())
    for word in wordList.split():
        colName += word[0].upper() + word[1:].lower()
    return colName


def readData(datasetLoc):
    data = pd.read_csv(datasetLoc)
##    wordList = []
    for col in data.columns:
        col = re.sub("[$|%|(|)]*", "", col)
        col = toUpperCase(col)

##        col = col.replace(' ','')
##        col = col.replace('$','')
##        col = col.replace('%','')
##        col = col.replace('(','')
##        col = col.replace(')','')
        colList.append(col)
    return data


data = readData(datasetLoc)
data.columns = colList


# print(os.getcwd())

##data2 = pd.read_csv(os.getcwd() + '\\Dataset\\P4-Movie-Ratings.csv')

# print(len(data))
print(data.info())
print(data.head())

print(data.describe())
data.Film = data.Film.astype('category')
data.Genre = data.Genre.astype('category')
data.YearOfRelease = data.YearOfRelease.astype('category')
print(data.describe())
print(data.info())

print(data.YearOfRelease.cat.categories)
# print(data.columns)

# def
# print(data.info())


# WORKING WITH JOINTPLOTS
# j = sns.scatterplot(data=data, x='RottenTomatoesRatings', y='BudgetMillion')
# j = sns.jointplot(data=data, x='RottenTomatoesRatings',
#                   y='AudienceRatings', kind='hex')
j = sns.jointplot(data=data, x='RottenTomatoesRatings',
                  y='AudienceRatings', kind='reg')

plt.show()
