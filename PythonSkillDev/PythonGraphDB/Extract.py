import requests as rq
import json as js
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


class FetchData:

    def __init__(self):
        # GIT_HUB_SEARCH_STRING = "girlswhocode"
        self.GIT_HUB_SEARCH_STRING = "womenwhocode"
        self.nameListMain = []
        self.FIRST_PAGE = 1
        self.MIN_WAIT_TIME = 4
        self.MAX_WAIT_TIME = 12
        self.URL = "https://github.com/search?p={0}&q={1}&type=Repositories"

    def getRequestToGithub(self, url):
        response = rq.get(url, headers={'User-agent': "Mozila"})
        response_code = response.status_code
        print("*************************************")
        if(response_code != 200):
            print("Error occured")
        else:
            return BeautifulSoup(response.content, 'html.parser')

    def fetchGithubMainPage(self):
        url = self.URL.format(self.FIRST_PAGE, self.GIT_HUB_SEARCH_STRING)
        # Create DOM model
        dom = self.getRequestToGithub(url)
        self.getAllUserData(int(self.getTotalPages(dom.select("em"))))
        nameListMain = self.displayList()
        # print(nameListMain)
        return nameListMain

    def getUserInfo(self, url):
        nameList = []

        print("The Url is -->", url)
        # Create a DOM model for HTML data obtained
        dom = self.getRequestToGithub(url)
        all_repo = dom.select("ul.repo-list li div.d-flex div a")
        for each_repo in all_repo:
            name = each_repo.attrs["href"][1:]
            href_link = "https://github.com/{}".format(name)
            nameList.append(href_link)
        return nameList

    def getAllUserData(self, total_pages):
        print(total_pages)
        # # TEST CONDITION
        total_pages = 1
        for i in range(0, total_pages):
            i = i + 1
            url = self.URL.format(i, self.GIT_HUB_SEARCH_STRING)
            print(url)
            nList = self.getUserInfo(url)
            self.nameListMain.append(nList)
            sleep(randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
        return self.nameListMain

    def displayList(self):
        nameLst = []
        for nl in self.nameListMain:
            for names in nl:
                nameLst.append(names)
        return nameLst

    def getTotalPages(self, pages):
        for page in pages:
            tp = page.attrs
            if(not(bool(tp))):
                continue
            else:
                total_pages = tp.get("data-total-pages")
        return total_pages

    # fetchGithubMainPage()
    def getUsersDetails(self, list):
        for item in list:
            # print(item)
            # print(self.getRequestToGithub(item))
            item += "/graphs/contributors"
            print(item)
            dom = self.getRequestToGithub(item)

            dom = dom.select("div.graphs li a")

            for item in dom:
                print(item.attrs["href"][1:])

            # print(dom.select("ol"))
            # list = dom.find_all("ol")
            # print("The list is", list)
            break


# if __name__ == "__main__":
#     f = FetchData()
#     f.fetchGithubMainPage()
