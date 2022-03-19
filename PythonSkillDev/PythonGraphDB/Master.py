from ExtractRepos import FetchData
from Load import Neo4jConnection
from Transform import CreateCypherQuery
from ExtractUsers import GetUserSpecificData
import csv

if __name__ == "__main__":

    fd = FetchData()
    list = fd.fetchGithubMainPage()
    gd = GetUserSpecificData()
    UserList = gd.getUsersDetails(list)

    with open("Names.csv", 'w', newline='') as file:
        fieldnames = ['User_Repo', 'User_Name', 'User_Url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in UserList:
            writer.writerow({'User_Repo': user.getUserRepository(
            ), 'User_Name': user.getUserName(), 'User_Url': user.getUserUrl()})

    cd = CreateCypherQuery(fd.GIT_HUB_SEARCH_STRING, "Names.csv")
    cd.createQueryString()
    dbString = cd.getCypherString()
    print(dbString)

    greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")

    res = greeter.query(dbString)
    print(res)
