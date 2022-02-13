import Helper.ReadData as rd
import pandas as pd
import os

fileloc1 = '\\Dataset\\P4-Movie-Ratings.csv'
fileloc2 = '\\Dataset\\P4-Demographic-Data.csv'

location = os.getcwd() + fileloc1

# print("The location is-->"+location)

# DATASET 2
# '\\Dataset\\P4-Demographic-Data.csv'
# data = pd.read_csv(location)

data = pd.read_csv(location)
# print(data)

# IMPORTANT FUNCTIONS
# print(data.head())
# print(data.tail())
# print(data.columns)
# print(len(data))

# SUBSETTING DARAFRAMES IN PANDAS
# SLICING THE ROWS
# print(data[22:56])
# DEFINE A FUNCTION


# def sliceRows(frm, to):
#     print(data[frm:to])


# sliceRows(22, 56)

# PRINTING ONLY THE ROWS THAT ARE SITUATED AT A PARTICULAR ROW
# print(data[22:23])
# DEFINE A FUNCTION
# def sliceRows(frm, to):
#     print(data[frm:to])


# sliceRows(22, 23)
# def printArow(num):
#     print(data[num:num+1])

# printArow(24)

# print(data[::-1])
# REVERSE THE ORDER OF DATA FRAME
# print(data[::-1])

# GET ROWS WITH CERTAIN INTERVALS
# print(data[::20])
# DEFINE A FUNCTION

# SLICING THE COLUMNS
lista = data.columns
# print(lista[:2])
# print(data[21:36][lista[:3]])

# print(data[lista[:2]])
# print(data['Country Name'])

# print(data.head())

# USING COLUMN HEADERS TO FETCH DATA
# print(data[lista[:3]])

# print(lista)
# print(data.Country Code)


# CLEANING THE DATASET
cData = rd.CleanData(location)

# print(cData.methodOverloading(2, 3, 5))

dataFrame = cData.getData()
# print(dataFrame.RottenTomatoesRatings)
# print(dataFrame[lista[:2]].tail())

# MATHEMATICAL OPERATIONS
##
# print(dataFrame.head())
# results = dataFrame.RottenTomatoesRatings / dataFrame.AudienceRatings

# print(results)
# print(dataFrame.head())


# print(dataFrame.columns)
# result = dataFrame.BirthRate/dataFrame.InternetUsers
# print(result.head())

# print(dataFrame.head())

# ADD COLUMNS
# dataFrame['MyCalc'] = dataFrame.BirthRate/dataFrame.InternetUsers
# print(dataFrame.head())

# REMOVE A COLUMN
# print(dataFrame.head())
# print(dataFrame.drop('MyCalc', axis=1).head())
# data = data.drop('MyCalc',axis=1)
# print(data.head())

# FILTERING THE DATA FRAMES
# FILTER ROWS


# print(dataFrame.InternetUsers)
##
# print(dataFrame.InternetUsers < 20)
##
# Filter = dataFrame.InternetUsers < 20
##
##
# Filter2 = data.Birthrate > 40
##
# print(dataFrame[Filter].head())
##
# print(data[data.Birthrate < 40])


# Filter = (dataFrame.IncomeGroup == 'High income') & (
# dataFrame.InternetUsers < 60) & (dataFrame.BirthRate < 20)
# Filter3 =(data.Birthrate < 40)
# print("hello")
# print(dataFrame[Filter])


# SUMMARY STATISTICS
# print(dataFrame.info())
# print(dataFrame.describe())

# print(len(data))
# print(dataFrame.info())
# print(dataFrame.head())

# print(dataFrame.describe())
dataFrame.Film = dataFrame.Film.astype('category')
dataFrame.Genre = dataFrame.Genre.astype('category')
dataFrame.YearOfRelease = dataFrame.YearOfRelease.astype('category')
# print(dataFrame.describe())
# print(dataFrame.info())
# print(dataFrame.info())


df = dataFrame.RottenTomatoesRatings


def genDataFrame(i, j):
    return df[i:j]


def genSteps(interval):
    start = 0
    end = start + interval
    return start, end


df1 = genDataFrame(0, 50)
df2 = genDataFrame(50, 100)
df3 = genDataFrame(100, 150)
df4 = genDataFrame(150, 200)

print(df1)
print(df2)
print(df3)
print(df4)


print(genSteps(50))
