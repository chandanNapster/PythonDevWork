##INTRODUCTION TO SEABORN

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.rcParams['figure.figsize'] = 8,4

colList = []

def readData():
    data = pd.read_csv('C:\\Users\\A\\Desktop\\DevWork\\Python\\Dataset\\P4-Demographic-Data.csv')
    for col in data.columns:
        col = col.replace(' ','')
        colList.append(col)
    return data
        
data = readData()
data.columns = colList

print(data.head())

##Filter = (data["IncomeGroup"] == "High income") & (data["Internetusers"] > 60.0)
##Filter = (data.Internetusers > 60.0) & (data.IncomeGroup == "High income")
Filter =(data.IncomeGroup == "High income") & (data.Birthrate > 20) & (data.Internetusers > 17)
Filter3 = (data.IncomeGroup == 'High income')&(data.Internetusers < 60)&(data.Birthrate < 20)
print(data[Filter])

# CREATE DISTRIBUTION:
##vis1 = sns.distplot(data["Internetusers"], bins = 30)

##plt.show()

# BOX PLOTS

##vis2 = sns.boxplot(data = data, x = 'IncomeGroup', y = 'Birthrate')

##plt.show()

#SEABORN GALLARY

vis3 = sns.lmplot(data = data[Filter], y = "Internetusers",
                  x = "Birthrate", fit_reg= False,
                  hue = 'IncomeGroup', size = 6, aspect= 2)
plt.show()

##KEYWORD ARGUMENTS
##MARKER SIZE



##vis3 = sns.lmplot(data = data, y = "Internetusers",
##                  x = "Birthrate", fit_reg= False,
##                  hue = 'IncomeGroup', size = 6,
##                  scatter_kws={"s":50})
##plt.show()











