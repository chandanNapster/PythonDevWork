# CORRECT CODE
# import Helper.ReadData as rd
# import pandas as pd
# import os

# fileloc = '\\Dataset\\P4-Demographic-Data.csv'
# location = os.getcwd() + fileloc

# data = rd.CleanData(location)
# data = data.getData()

# columns = data.columns
# dataFrame = data[columns]
# filter = (dataFrame.IncomeGroup == 'High income') & (
#     dataFrame.InternetUsers < 60) & (dataFrame.BirthRate < 20)

# print(dataFrame[filter][2:3])

# MODIFIED CODE
# import Helper.ReadData as rd
# import pandas as pd
# import os

# fileloc = '\\Dataset\\P4-Demographic-Data'
# location = os.getcwd() + fileloc

# data = rd.CleanData(location)
# data = data.getData()

# columns = data.columns
# dataFrame = data[columns]
# filter = (dataFrame.IncomeGroup == 'High income') && (dataFrame.InternetUsers < 60) && (dataFrame.BirthRate < 20)

# print(dataFrame[filter][2:3])

# CORRECT CODE
import Helper.ReadData as rd
import pandas as pd
import os

fileloc = '\\Dataset\\P4-Demographic-Data.csv'
location = os.getcwd() + fileloc

data = rd.CleanData(location)
data = data.getData()


def getRows(dataFrame, x, y):
    row = dataFrame[x:y]
    col = row.columns
    countryName = row[col[x]]
    birthRate = row[col[x+1]]
    internetUsr = row[col[x+2]]
    return countryName, birthRate, internetUsr


dataCol = getRows(data, 2, 3)

for i in range(len(dataCol)):
    print(dataCol[i])

# MODIFIED CODE
# import Helper.ReadData as rd
# import pandas as pd
# import os

# fileloc = '\\Dataset\\P4-Demographic-Data'
# location = os.getcwd() + fileloc

# data = rd.CleanData(location)
# data = data.getData()


# def getRows(dataFrame, x, y):
#     row = dataFrame[x, y]
#     col = row.columns
#     countryName = row[col[x]]
#     birthRate = row[col[x+1]]
#     internetUsr = row[col[X+2]]
#     return countryName, birthRate, internetUsr


# dataCol = getRows(data, 2, 3)

# for i in len(dataCol):
#     dataCol[i] = i
