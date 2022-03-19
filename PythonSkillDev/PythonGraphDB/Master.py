from ExtractRepos import FetchData
from Load import Neo4jConnection
from Transform import CreateCypherQuery


if __name__ == "__main__":

    fd = FetchData()

    cd = CreateCypherQuery(fd.GIT_HUB_SEARCH_STRING, "Names.csv")
    cd.createQueryString()
    dbString = cd.getCypherString()
    print(dbString)

    greeter = Neo4jConnection("bolt://localhost:7687", "neo4j", "chandan")

    res = greeter.query(dbString)
    print(res)
