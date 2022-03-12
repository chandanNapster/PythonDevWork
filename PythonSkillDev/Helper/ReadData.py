import pandas as pd
import re


class CleanData:
    # __location = ''

    def __init__(self, location):
        self.__location = location

    def __imporveColHeaders(self, colList):
        list = []
        for col in colList:
            col = re.sub("[$|%|(|)]*", "", col)
            col = self.fstWordUppr(col)
            list.append(col)
        return list

    def getData(self):
        data = pd.read_csv(self.__location)
        data.columns = self.__imporveColHeaders(data.columns)
        return data

    def fstWordUppr(self, sentence):
        colName = ''
        for word in sentence.split():
            colName += word[0].upper() + word[1:].lower()
        return colName
