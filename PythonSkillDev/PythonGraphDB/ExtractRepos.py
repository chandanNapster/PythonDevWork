
from bs4 import BeautifulSoup
from time import sleep
from random import randint

import requests as rq


class FetchData:

    def __init__(self):
        self.GIT_HUB_SEARCH_STRING = "womenwhocode"
        self.__nameListMain = []
        self.__FIRST_PAGE = 1
        self.__MIN_WAIT_TIME = 4
        self.__MAX_WAIT_TIME = 12
        self.__URL = "https://github.com/search?p={0}&q={1}&type=Repositories"

    def __getRequestToGithub(self, url):
        response = rq.get(url, headers={'User-agent': "Mozila"})
        response_code = response.status_code
        print("*************************************")
        if(response_code != 200):
            print("Error occured")
        else:
            return BeautifulSoup(response.content, 'html.parser')

    def fetchGithubMainPage(self):
        url = self.__URL.format(
            self.__FIRST_PAGE, self.GIT_HUB_SEARCH_STRING)
        # Create DOM model
        dom = self.__getRequestToGithub(url)
        self.__getAllUserData(int(self.__getTotalPages(dom.select("em"))))
        self.__nameListMain = self.__displayList()
        return self.__nameListMain

    def __getUserInfo(self, url):
        nameList = []

        print("The Url is -->", url)
        # Create a DOM model for HTML data obtained
        dom = self.__getRequestToGithub(url)
        all_repo = dom.select("ul.repo-list li div.d-flex div a")
        for each_repo in all_repo:
            name = each_repo.attrs["href"][1:]
            href_link = "https://github.com/{}".format(name)
            nameList.append(href_link)
        return nameList

    def __getAllUserData(self, total_pages):
        print(total_pages)
        total_pages = 1
        for i in range(0, total_pages):
            i = i + 1
            url = self.__URL.format(i, self.GIT_HUB_SEARCH_STRING)
            print(url)
            nList = self.__getUserInfo(url)
            self.__nameListMain.append(nList)
            sleep(randint(self.__MIN_WAIT_TIME, self.__MAX_WAIT_TIME))
        return self.__nameListMain

    def __displayList(self):
        nameLst = []
        for nl in self.__nameListMain:
            for names in nl:
                nameLst.append(names)
        return nameLst

    def __getTotalPages(self, pages):
        for page in pages:
            tp = page.attrs
            if(not(bool(tp))):
                continue
            else:
                total_pages = tp.get("data-total-pages")
        return total_pages
