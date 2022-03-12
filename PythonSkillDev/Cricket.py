
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = 10, 6

# Seasons
Seasons = ["2008", "2009",
           "2010", "2011", "2012", "2013", "2014"]

# Season Dictionary
Sdict = {"2008": 0, "2009": 1, "2010": 2,
         "2011": 3, "2012": 4, "2013": 5, "2014": 6}

# Players
Players = ['ViratKohli', 'RohitSharma', 'DavidWarner', 'SteveSmith',
           'MarnusLabuschagne', 'ABdeVilliers', 'ChrisGayle', 'AaronFinch']


# Player Dictionary
Pdict = {"ViratKohli": 0, "RohitSharma": 1, "DavidWarner": 2, "SteveSmith": 3,
         "MarnusLabuschagne": 4, "ABdeVilliers": 5, "ChrisGayle": 6, "AaronFinch": 7}


# Salaries
ViratKohli_Salary = [21262500, 23034375, 24806250,
                     25244493, 27849149, 30453805, 23500000]
RohitSharma_Salary = [14232567, 14976754, 16324500,
                      18038573, 19752645, 21466718, 23180790]
DavidWarner_Salary = [14410581, 15779912, 14500000,
                      16022500, 17545000, 19067500, 20644400]
SteveSmith_Salary = [14410581, 15779912, 17149243,
                     18518574, 19450000, 22407474, 22458000]
MarnusLabuschagne_Salary = [13758000, 15202590,
                            16647180, 18091770, 19536360, 20513178, 21436271]
ABdeVilliers_Salary = [14410581, 15779912, 14500000,
                       16022500, 17545000, 19067500, 20644400]
ChrisGayle_Salary = [4574189, 13520500, 14940153,
                     16359805, 17779458, 18668431, 20068563]
AaronFinch_Salary = [0, 0, 4171200, 4484040, 4796880, 17832627, 18995624]


# Salary Matrix

Salaries = np.array([ViratKohli_Salary, RohitSharma_Salary, DavidWarner_Salary, SteveSmith_Salary,
                     MarnusLabuschagne_Salary, ABdeVilliers_Salary, ChrisGayle_Salary, AaronFinch_Salary])


# Games
ViratKohli_G = [80, 77, 82, 82, 73, 82, 58]
RohitSharma_G = [79, 76, 72, 60, 72, 79, 80]
DavidWarner_G = [79, 78, 75, 81, 76, 77, 69]
SteveSmith_G = [80, 65, 77, 55, 67, 77, 40]
MarnusLabuschagne_G = [82, 82, 78, 54, 76, 71, 41]
ABdeVilliers_G = [70, 69, 77, 57, 74, 79, 44]
ChrisGayle_G = [78, 45, 80, 60, 70, 62, 82]
AaronFinch_G = [35, 35, 80, 66, 81, 81, 27]

# Games Matrix
Games = np.array([ViratKohli_G, RohitSharma_G, DavidWarner_G, SteveSmith_G,
                 MarnusLabuschagne_G, ABdeVilliers_G, ChrisGayle_G, AaronFinch_G])

# Innings
ViratKohli_I = [77, 72, 82, 80, 70, 62, 48]
RohitSharma_I = [74, 66, 72, 60, 52, 69, 70]
DavidWarner_I = [69, 68, 45, 21, 36, 77, 69]
SteveSmith_I = [70, 55, 77, 55, 37, 77, 40]
MarnusLabuschagne_I = [72, 62, 58, 44, 36, 71, 41]
ABdeVilliers_I = [70, 59, 47, 57, 74, 69, 44]
ChrisGayle_I = [78, 45, 60, 50, 70, 62, 72]
AaronFinch_I = [35, 35, 80, 66, 81, 81, 27]

# Innings Matrix
Innings = np.array([ViratKohli_I, RohitSharma_I, DavidWarner_I, SteveSmith_I,
                    MarnusLabuschagne_I, ABdeVilliers_I, ChrisGayle_I, AaronFinch_I])


# Runs
ViratKohli_R = [3567, 4500, 5000, 6720, 7000, 6200, 2500]
RohitSharma_R = [2474, 3666, 5672, 4860, 4352, 2169, 6870]
DavidWarner_R = [5569, 3368, 2345, 3221, 6736, 5477, 6769]
SteveSmith_R = [5570, 6655, 7777, 3355, 2237, 4477, 5040]
MarnusLabuschagne_R = [3272, 4362, 4558, 5444, 6536, 6771, 7841]
ABdeVilliers_R = [4370, 6559, 4347, 6657, 5674, 8769, 7744]
ChrisGayle_R = [5678, 7745, 8060, 7050, 6070, 4562, 7872]
AaronFinch_R = [1135, 635, 7880, 4466, 5581, 5481, 6627]

# Runs Matrix
Runs = np.array([ViratKohli_R, RohitSharma_R, DavidWarner_R, SteveSmith_R,
                 MarnusLabuschagne_R, ABdeVilliers_R, ChrisGayle_R, AaronFinch_R])


pMaker = {"ViratKohli": '^', "RohitSharma": 'o', "DavidWarner": 'd', 'SteveSmith': 'D',
          'MarnusLabuschagne': 's', 'ABdeVilliers': '1', 'ChrisGayle': '2', 'AaronFinch': '*'}


pColor = {"ViratKohli": 'Black', "RohitSharma": 'Yellow', "DavidWarner": 'Red',
          "SteveSmith": 'Green', "MarnusLabuschagne": 'Magenta', "ABdeVilliers": 'indigo',
          "ChrisGayle": 'greenyellow', "AaronFinch": 'maroon'}


# WE CREATED A FOR LOOP HERE SO THAT WE CAN PLOT SCORES OF INDIVIDUAL PLAYERS
for name in Players:
    plt.plot(Runs[Pdict[name]] / Innings[Pdict[name]],
             c=pColor[name], marker=pMaker[name], ls='--', label=name)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(list(range(0, len(Seasons))), Seasons, rotation='vertical')
plt.show()


# TASK FOR YOU
# HOW CAN WE GENERALIZE THE APPROACH WHERE A USER CAN PASS DIFFERENT MATRICES LIKE GAMES, RUNS, (RUNS DIVIDED BY GAMES), (RUNS DIVIDED BY INNINGS) ETC.


def myPlot2(Matrix, plyrList=Players):
    for name in plyrList:
        plt.plot(Matrix[Pdict[name]],
                 c=pColor[name], marker=pMaker[name], ls='--', label=name)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, len(Seasons))), Seasons, rotation='vertical')
    plt.show()


if __name__ == "__main__":
    user_input = input("Press any key to continue or press q to quit")
    while(user_input.casefold() != 'q'):
        user_input = input(
            "For Salary/Games press 1 or For Salary/Innings press 2 or Press q to quit")
        if user_input != 'q':
            if int(user_input) == 1:
                matrx = Salaries/Games
            elif int(user_input) == 2:
                matrx = Salaries/Innings
            elif int(user_input) == 3:
                matrx = Runs/Innings
            else:
                matrx = Runs/Games
        else:
            break
        myPlot2(matrx)
