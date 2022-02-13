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
##j = sns.jointplot(data= data, x = 'RottenTomatoesRatings', y = 'BudgetMillion')
##j = sns.jointplot(data= data, x = 'RottenTomatoesRatings', y = 'AudienceRatings',kind = 'hex')
##j = sns.jointplot(data= data, x = 'RottenTomatoesRatings', y = 'AudienceRatings',kind = 'reg')
# ALREADY METHODS
# sns.set_style("darkgrid")
##m1 = sns.distplot(data.AudienceRatings, bins = 20)
##m2 = sns.distplot(data.RottenTomatoesRatings, bins = 20)

##n1 = plt.hist(data.AudienceRatings, bins = 15)
##n1 = plt.hist(data.RottenTomatoesRatings, bins = 15)

# STACKED HISTOGRAMS

print(data.Genre.cat.categories)

genr = data.Genre.cat.categories

hyList = []
myLabels = []

for gen in genr:
    filter1 = data.Genre == gen
    hyList.append(data[filter1].BudgetMillion)
    myLabels.append(gen)

##filter1 = data.Genre == "Action"

##plt.hist(hyList, stacked= True, bins = 15)
##plt.hist(hyList, bins = 15, rwidth= 1, stacked= True, label=myLabels)
# plt.legend()


# CREATING KDE PLOTS
# HOW CAN BE VISSULIZE AUDIENCE VS CRICTIC RATING

##vis1 = sns.lmplot(data = data, x="RottenTomatoesRatings", y ="AudienceRatings", fit_reg=False, hue= 'Genre',size=7)

##vis2 = sns.kdeplot(data.RottenTomatoesRatings, data.AudienceRatings,shade=True, shade_lowest=False, cmap='Reds')
##vis2 = sns.kdeplot(data.RottenTomatoesRatings, data.AudienceRatings, cmap='Reds')


# WORKING WITH SUB-PLOTS
sns.set_style("dark")
##k1 = sns.kdeplot(data.BudgetMillion, data.AudienceRatings)

##fig, axes = plt.subplots(2,2,figsize=(12,6), sharex = True, sharey = True)
##k1 = sns.kdeplot(data.BudgetMillion, data.AudienceRatings, ax = axes[0][0])
##k2 = sns.kdeplot(data.BudgetMillion, data.RottenTomatoesRatings, ax = axes[1][0])
# k1.set(xlim=(-100,300))


# VIOLIN PLOTS

##z = sns.violinplot(data= data, x = 'Genre', y = 'RottenTomatoesRatings')
##z = sns.violinplot(data= data[data.Genre == 'Drama'], x = 'YearOfRelease', y = 'RottenTomatoesRatings')

# CREATING FACET GRID


##g = sns.FacetGrid(data,row= 'Genre',col='YearOfRelease', hue='Genre')
##g = g.map(plt.hist, 'RottenTomatoesRatings')


g = sns.FacetGrid(data, row='Genre', col='YearOfRelease', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'RottenTomatoesRatings', 'AudienceRatings', **kws)

plt.show()
