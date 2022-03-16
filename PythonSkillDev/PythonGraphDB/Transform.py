from Extract import FetchData
from Load import Neo4jConnection
import openpyxl


class CreateCypherQuery:

    def __init__(self):
        self.__queryString

    def setQueryString(self, query):
        self.__queryString = query

    def getQueryString(self):
        return self.__queryString


if __name__ == "__main__":
    fd = FetchData()
    list = fd.fetchGithubMainPage()
    fd.getUsersDetails(list)

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
