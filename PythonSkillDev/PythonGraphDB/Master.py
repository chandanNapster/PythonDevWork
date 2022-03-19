from ExtractRepos import FetchData
from ExtractUsers import GetUserSpecificData
from Load import Neo4jConnection
import csv


if __name__ == "__main__":
    fd = FetchData()
    list = fd.fetchGithubMainPage()

    print(len(list))
    gd = GetUserSpecificData()
    UsrList = gd.getUsersDetails(list)

    print("\n")

    for usres in UsrList:
        print(usres.getUserName(), usres.getUserUrl())

    with open("Names.csv", 'w', newline='') as file:
        fieldnames = ['User_Name', 'User_Url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in UsrList:
            writer.writerow({'User_Name': user.getUserName(),
                            'User_Url': user.getUserUrl()})

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
