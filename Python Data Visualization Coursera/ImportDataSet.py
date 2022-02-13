import pandas as pd
import matplotlib.pyplot as plt

URL_xlsx = 'D:\\Research\\Data Visualization\\Dataset\\Canada.xlsx'
URL_csv = 'D:\\Research\\Data Visualization\\Dataset\\archive\\canadian_immegration_data.csv'
URL = ''
xlsx = True

URL = URL_xlsx if (xlsx == True) else URL_csv


def read_csv():
    df_can_csv = pd.read_csv(URL)
    return df_can_csv


def read_xlsx():
    df_can_xlsx = pd.read_excel(
        URL, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
    return df_can_xlsx


df_can = read_xlsx() if (xlsx == True) else read_csv()

# print(df_can.info(verbose=False))

# print(df_can.columns)
# print(df_can.index)

# print(df_can.columns.tolist())
# print(df_can.index.tolist())

# print(df_can.shape)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
# print(df_can.head())

df_can.rename(columns={'OdName': 'Country',
              'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

years = list(range(1995, 2013))

df_can.set_index('Continent', inplace=True)

print(df_can.loc['Asia', 1995])

# df_can['Total'] = df_can.sum(axis=1)
# print(df_can.head())

# print(df_can.describe())

# SELECTING COLUMNS
# print(df_can[['Continent', 'Total']])

# SELECTING ROWS
# print(df_can[1995])

# years = list(range(1995, 2013))
# print(years)

# df_can.set_index('Country', inplace=True)

# df_can_haiti = df_can.loc['Haiti', years]

# df_can_haiti.plot(kind='line')
# plt.show()

# df_can_haiti.index = df_can_haiti.index.map(int)
# df_can_haiti.plot(kind='line')

# plt.title('Immigration from Haiti')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# plt.show()


# VISUALIZING DATA USING MATPLOTLIB

# LINE PLOTS


# print(df_can.Country)
# df_can.plot(kind='line')
# plt.show()
