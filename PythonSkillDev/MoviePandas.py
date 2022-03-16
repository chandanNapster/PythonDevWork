import Helper.ReadData as rd
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

fileloc1 = '\\Dataset\\P4-Movie-Ratings.csv'


location = os.getcwd() + fileloc1


data = pd.read_csv(location)
print(data)

# IMPORTANT FUNCTIONS
print(data.head())
print(data.tail())
print(data.columns)
print(len(data))

# SUBSETTING DARAFRAMES IN PANDAS
# SLICING THE ROWS
print(data[22:56])

# SLICING THE COLUMNS
lista = data.columns
print(lista[:2])
print(data[21:36][lista[:3]])


# CLEANING THE HEADERS OF DATASET
cData = rd.CleanData(location)
dataFrame = cData.getData()
print(dataFrame.head())


print(dataFrame[lista[:2]].tail())

# MATHEMATICAL OPERATIONS

results = dataFrame.RottenTomatoesRatings / dataFrame.AudienceRatings

print(results)


Filter = (dataFrame.AudienceRatings >= 40) & (
    dataFrame.RottenTomatoesRatings > 50) & (dataFrame.Genre == 'Comedy')
print("hello")
print(dataFrame[Filter])


# SUMMARY STATISTICS
print(dataFrame.info())
print(dataFrame.describe())

print(len(data))
print(dataFrame.info())
print(dataFrame.head())

print(dataFrame.describe())
dataFrame.Film = dataFrame.Film.astype('category')
dataFrame.Genre = dataFrame.Genre.astype('category')
dataFrame.YearOfRelease = dataFrame.YearOfRelease.astype('category')
print(dataFrame.describe())
print(dataFrame.info())
print(dataFrame.info())


# WORKING WITH JOINTPLOTS
# j = sns.scatterplot(
#     data=dataFrame, x='RottenTomatoesRatings', y='BudgetMillion')

# j = sns.histplot(data=dataFrame, x='AudienceRatings', kde=True)

j = sns.jointplot(data=dataFrame, x='RottenTomatoesRatings',
                  y='AudienceRatings', kind='reg')

plt.show()
