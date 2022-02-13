##DATA FRAMES
###Method 2
##import os
##print(os.getcwd())

##DATA FRAMES
## SIMILAR TO TABLES
import pandas as pd

#Method 1: Specify Full Path to File

df = pd.read_csv('C:\\Users\\A\\Desktop\\DevWork\\Python\\Dataset\\P4-Demographic-Data.csv')
print(df)
print(len(df))
print(df.head(100))
print(df.tail(4))
print(df.info())
print(df.describe())
print(df.describe().transpose())


##RENAMING COLUMNS ON DATAFRAME

print(df.head())
print(df.columns)
##df.columns = ['a','b','c','d','e']
print(df)
