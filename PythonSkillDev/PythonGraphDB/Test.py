import time
from loadbar import LoadBar


def test():
    bar = LoadBar(
        max=5
    )
    bar.start()
    for x in range(5):
        bar.update(step=x)
        time.sleep(1)
    bar.end()


if __name__ == "__main__":
    test()


# if __name__ == "__main__":

    # list = ["https://github.com/WomenWhoCode/WomenWhoCode",
    #         "https://github.com/WomenWhoCode/WWCodeDataScience", "https://github.com/shanselman/womenwhocodepdxgit"]

    # fd = FetchData()
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

    # cd = CreateCypherQuery(fd.GIT_HUB_SEARCH_STRING)
    # cypherStr = "Create "
    # with open("Names.csv", 'r') as file:
    #     c_file = csv.DictReader(file)
    #     i = 0

    #     for row in c_file:
    #         # print(row["User_Repo"], row["User_Name"], row["User_Url"])
    #         index = str(i)
    #         if i == 0:
    #             cypherStr += "(a"  ":MAIN{name:" + "\"" + fd.GIT_HUB_SEARCH_STRING + "\"" + \
    #                 "})<-[:IS_PART_OF]-(b"+index + \
    #                 ":REPOSITORY{repo_url:" + "\"" + \
    #                 row["User_Repo"] + "\"" + \
    #                 "})<-[:CONTRIBUTES_TO]-(c"+index+":USER{user_name:" + \
    #                 "\""+row["User_Name"] + "\"" + ",user_url:" + \
    #                 "\""+row["User_Url"] + "\"" + "}"+"),"
    #         else:
    #             cypherStr += "(a)<-[:IS_PART_OF]-(b"+index + \
    #                 ":REPOSITORY{repo_url:" + "\"" + \
    #                 row["User_Repo"] + "\"" + \
    #                 "})<-[:CONTRIBUTES_TO]-(c"+index+":USER{user_name:" + \
    #                 "\""+row["User_Name"] + "\"" + ",user_url:" + \
    #                 "\""+row["User_Url"] + "\"" + "}"+"),"
    #         i += 1
    #         # print(cypherStr)
    #         # cd.createQueryString(row["User_Repo"])
    #     print(cypherStr)
    #     cypherStr = cypherStr

    # # print(fd.GIT_HUB_SEARCH_STRING)

    # # print(cd.createQueryString())
    # # for item in list:
    # #     print(item)

    # # with open("Names.csv", 'w') as file:
    # #     for item in list:
    # #         file.write(str(item) + "\n")

    # greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")
    # q = "MATCH (a) RETURN a"

    # cypherStr = "Create (a:CHANDAN{name:\"Test\"})"
    # c = CreateCypherQuery(cypherStr)
    # c.setQueryString(q)
    # res = greeter.query(cypherStr)
    # # print(res)

   # def getUsersDetails(self, list):
    #     users = []
    #     for item in list:
    #         itemstr = str(item)
    #         # print(itemstr)

    #         if "stargazers" in itemstr.casefold():
    #             pass
    #         else:
    #             print(item)
    #             dom = self.getRequestToGithub(item)
    #             dom = dom.select(
    #                 "div.css-truncate.css-truncate-overflow.color-fg-muted > a")
    #             sleep(randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))

    #             for link in dom:
    #                 print(link.text, "https://www.github.com" +
    #                       link.attrs["href"])
    #             # dom = self.getRequestToGithub(item)
    #             # sleep(randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
    #             # for links in dom.find_all("div"):
    #             #     link = links.find('a')
    #             #     if link == None or not ("class" in link.attrs):
    #             #         continue
    #             #     else:
    #             #         if('commit-author' in link.attrs['class'] or 'user-mention' in link.attrs['class']):
    #             #             print(link.attrs['href'])
    #             #             users.append(link.attrs['href'])
    #             print("########################")
    #     users = set(users)
    #     return users

# if __name__ == "__main__":
#     f = FetchData()
#     f.fetchGithubMainPage()

# if __name__ == "__main__":
#     greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")
#     q = "MATCH (a) RETURN a"
#     res = greeter.query(q)
#     print(res)
