from random import randint
import re
from time import sleep
from ExtractRepos import FetchData
from Load import Neo4jConnection
from Transform import CreateCypherQuery
from Transform import SearchExistingUsers
from ExtractUsers import SearchFollowers
from ExtractUsers import GetUserSpecificData
import csv
import json

if __name__ == "__main__":
    staging_area = "Names2.csv"
    # fd = FetchData()
    # list = fd.fetchGithubMainPage()

    # gd = GetUserSpecificData()
    # UserList = gd.getUsersDetails(list)

    # with open("Names.csv", 'w', newline='') as file:
    #     fieldnames = ['User_Repo', 'User_Name', 'User_Url']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for user in UserList:
    #         writer.writerow({'User_Repo': user.getUserRepository(
    #         ), 'User_Name': user.getUserName(), 'User_Url': user.getUserUrl()})

    fd = FetchData()
    cd = CreateCypherQuery(fd.GIT_HUB_SEARCH_STRING, staging_area)
    cd.createQueryString()
    dbCreateString = cd.getCypherString()
    print(dbCreateString)
    greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")
    greeter.query(dbCreateString)

    # print("############################ CREATION ENDED ####################")
    # ad = SearchExistingUsers()
    # matchUserQuery = ad.getSearchQuery()

    # result = greeter.query(matchUserQuery)

    # namesList = []
    # name = ""
    # for records in result:
    #     for record in records:
    #         if record['user_name'] == None:
    #             pass
    #         else:
    #             name = record['user_name']
    #             namesList.append(name)

    # namesList = set(namesList)
    # namesList = list(namesList)

    # print(namesList)
    # sf = SearchFollowers()

    # for name in namesList:
    #     print("***********{0}****************".format(name))
    #     followers = sf.callToGithubApi(name)
    #     sleep(randint(2, 8))
    #     for follower in followers:
    #         print(follower['html_url'])

    # print("*****************************")
    # names = sf.callToGithubApi("renana")

    # for name in names:
    #     print(name['html_url'])

    # json_string = json.dumps(name)

    # print(f'JSON string: {json_string}')

    # greeter.query(cd.dropDB())
