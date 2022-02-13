import Helper.ReadData as rd
import os


class Stats:
    __start = 0
    __end = 0

    def __init__(self):

        self.__fileloc1 = '\\Dataset\\P4-Movie-Ratings.csv'
        self.__location = os.getcwd() + self.__fileloc1
        self.cData = rd.CleanData(self.__location)
        self.dataFrame = self.cData.getData()
        self.df = self.dataFrame.RottenTomatoesRatings

    def genDataFrame(self, i, j):
        return self.df[i:j]

    def genSteps(self, interval):
        self.__interval = interval
        self.__end = self.__start + self.__interval
        self.__start = self.__end
        return self.__start, self.__end
