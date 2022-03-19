from ExtractRepos import FetchData
from ExtractUsers import GetUserSpecificData
from Load import Neo4jConnection
import csv


class CreateCypherQuery:

    def __init__(self, searchString):
        self.__queryString = ""
        self.__searchString = searchString

    def setQueryString(self, query):
        self.__queryString = query

    def getQueryString(self):
        return self.__queryString

    def createQueryString(self):
        cypherStr = "Create "
        i = 0
        while i < 10:
            index = str(i)
            if i == 0:
                cypherStr += "(a"  ":MAIN{name:" + "\"chandan\"" + \
                    "})<-[:IS_PART_OF]-(b"+index + \
                    ":REPOSITORY{name:" + "\"sharma\"" + "}),"
            else:
                cypherStr += "(a)<-[:IS_PART_OF]-(b"+index + \
                    ":REPOSITORY{name:" + "\"sharma\"" + "}),"

            i += 1
        print(cypherStr)


if __name__ == "__main__":

    # list = ["https://github.com/WomenWhoCode/WomenWhoCode",
    #         "https://github.com/WomenWhoCode/WWCodeDataScience", "https://github.com/shanselman/womenwhocodepdxgit"]

    fd = FetchData()
    # list = fd.fetchGithubMainPage()
    # # # for item in list:
    # # #     print(item)
    # # print(len(list))
    # gd = GetUserSpecificData()
    # UsrList = gd.getUsersDetails(list)

    # print("\n")

    # for usres in UsrList:
    #     print(usres.getUserName(), usres.getUserUrl())
    # print(list)

    # with open("Names.csv", 'w', newline='') as file:
    #     fieldnames = ['User_Repo', 'User_Name', 'User_Url']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for user in UsrList:
    #         writer.writerow({'User_Repo': user.getUserRepository(), 'User_Name': user.getUserName(),
    #                         'User_Url': user.getUserUrl()})

    with open("Names.csv", 'r') as file:
        c_file = csv.DictReader(file)
        for row in c_file:
            print(row["User_Repo"], row["User_Name"], row["User_Url"])

    print(fd.GIT_HUB_SEARCH_STRING)

    cd = CreateCypherQuery(fd.GIT_HUB_SEARCH_STRING)
    print(cd.createQueryString())
    # for item in list:
    #     print(item)

    # with open("Names.csv", 'w') as file:
    #     for item in list:
    #         file.write(str(item) + "\n")

    # greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")
    # q = "MATCH (a) RETURN a"

    # c = CreateCypherQuery()
    # c.setQueryString(q)
    # res = greeter.query(c.getQueryString())
    # print(res)
