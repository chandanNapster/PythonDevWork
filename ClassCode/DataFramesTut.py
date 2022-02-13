##RENAMING COLUMNS IN A DATAFRAME
import pandas as pd


colList = []


def readData():
    data = pd.read_csv('C:\\Users\\A\\Desktop\\DevWork\\Python\\Dataset\\P4-Demographic-Data.csv')
    for col in data.columns:
        col = col.replace(' ','')
        colList.append(col)
    return data
        
data = readData()
data.columns = colList
print(data.columns[::-1])


##SUBSETTING DARAFRAMES IN PANDAS
##SLICING THE ROWS
##print(data[21:26])
##print(data[:])
####REVERSE THE DATA FRAME
##print(data[::-1])
##
##
#####QUICK EXERCISE
####i = 0
####
####def printInReverse():
####    i = len(data) - 1
####    while(i >= 0):
####        print(data[i:i-1])
####        i -= 1
####
####printInReverse()
##
#### GET ONLY 20th ROW
##print(data[::20])



##COLUMNS

##def printCols():
####    for col in colList:
####        print(data[2:4][col].head())
##    print(data[2:40][colList[:2]])
##    print(data[colList[:2]][2:40])
        

##print(data['CountryName'])

##printCols()

##print(data.Birthrate.head())
## SUBSETTING REVISION
##print(data[colList[:4]][4:30])
##print(data.CountryName[4:30])
##print(data.CountryName[::-1])
##
####MATHEMATICAL OPERATIONS
##
##result = data.Birthrate/data.Internetusers
##print(result.head())
##
####ADD COLUMNS
##data['MyCalc'] = data.Birthrate/data.Internetusers
##print(data)
##
####REMOVE A COLUMN
##print(data.head())
##print(data.drop('MyCalc',axis=1))
##data = data.drop('MyCalc',axis=1)
##print(data.head())
##
####FILTERING THE DATA FRAMES
####FILTER ROWS
##print(data.head())
##
##print(data.Internetusers < 2)
##
##Filter = (data.Internetusers < 2)
##
##
##Filter2 = data.Birthrate > 40
##
##print(data[Filter2])
##
##print(data[data.Birthrate < 40])

##Filter3 = (data.IncomeGroup == 'High income') & (data.Internetusers < 60) &(data.Birthrate < 20)
####Filter3 =(data.Birthrate < 40)
##print("hello")
##print(data[Filter3])

##print(data.IncomeGroup == 'High income' & data.Internetusers < 2)

##ANOTHER ONE
##print(data.IncomeGroup == 'High Income')

##data[data.IncomeGroup == 'High Income']
##
##data = data[data.IncomeGroup == 'High income']
##
##print(data[4:10][colList[:3]])
##
##print(data.IncomeGroup.unique)

##EXERCISE FIND EVERY THING ABOUT Malta

##Filter = data.CountryName == 'Malta'
##
##print(data[Filter])
##
##print(data.CountryCode.unique)

##LOOKING AT INDIVIDUAL ELEMENTS
print(data.head())

print(data.iat[4,1])

print(data.at[2,'Birthrate'])





