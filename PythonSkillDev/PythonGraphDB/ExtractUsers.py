import requests as rq
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import time
from loadbar import LoadBar

# pip install load-bar termcolor


class GetUserSpecificData:
    NUMBER_OF_ITERATIONS = 0

    def __init__(self):
        self.MIN_WAIT_TIME = 2
        self.MAX_WAIT_TIME = 8

    def __getRequestToGithub(self, url, length_of_list):
        response = rq.get(url, headers={'User-agent': "Mozila"})
        response_code = response.status_code
        GetUserSpecificData.NUMBER_OF_ITERATIONS += 1

        bar = LoadBar(
            max=length_of_list
        )
        bar.start()
        bar.update(step=GetUserSpecificData.NUMBER_OF_ITERATIONS)
        time.sleep(1)

        if(response_code != 200):
            print("Error occured")
        else:
            return BeautifulSoup(response.content, 'html.parser')

    def getUsersDetails(self, list):
        UserList = []
        length_of_list = self.__getTrueListSize(list)
        for item in list:
            itemstr = str(item)
            if "stargazers" in itemstr.casefold():
                pass
            else:
                dom = self.__getRequestToGithub(item, length_of_list)
                dom = dom.select(
                    "div.css-truncate.css-truncate-overflow.color-fg-muted > a")

                sleep(randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
                usr = UserInfo()

                for link in dom:
                    user_name = link.text
                    user_url = "https://www.github.com{0}".format(
                        link.attrs["href"])
                    usr = UserInfo(item, user_name, user_url)

                if usr.isEmpty():
                    usr.setUserName(item)
                    usr.setUserUrl(item)
                    usr.setUserRepository(item)
                    UserList.append(usr)
                    # TO DO - ADD A RECURSIVE CALL IF NO DATA FETCHED FROM GITHUB
                else:
                    UserList.append(usr)
        return UserList

    def __getTrueListSize(self, list):
        lengthList = 0
        for item in list:
            itemstr = str(item)
            if "stargazers" in itemstr.casefold():
                pass
            else:
                lengthList += 1
        return lengthList


class UserInfo:
    def __init__(self, repository="", user_name="", user_url=""):
        self.user_name = user_name
        self.user_url = user_url
        self.repository = repository

    def getUserName(self):
        return self.user_name

    def getUserUrl(self):
        return self.user_url

    def getUserRepository(self):
        return self.repository

    def setUserName(self, user_name):
        self.user_name = user_name

    def setUserUrl(self, user_url):
        self.user_url = user_url

    def setUserRepository(self, repository):
        self.repository = repository

    def isEmpty(self):
        if self.user_name == "" and self.user_url == "" and self.repository == "":
            return True
        else:
            return False

    def __str__(self):
        return ("Repository : {0} || User Name : {1} || User URL : {2}".format(self.getUserRepository(), self.getUserName(), self.getUserUrl()))


class SearchFollowers:
    def __init__(self):
        self.__apilink = "https://api.github.com/users/"

    def callToGithubApi(self, userName):
        url = self.__apilink + userName + "/followers"
        response = rq.get(url, headers={'User-agent': "Mozila"})
        response_code = response.status_code

        if(response_code != 200):
            print("Error occured")
        else:
            return response.json()
