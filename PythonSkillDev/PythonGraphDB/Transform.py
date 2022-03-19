import csv


class CreateCypherQuery:

    def __init__(self, github_search_string, staging_file):
        self.__github_searchString = github_search_string
        self.__staging_file = staging_file
        self.__cypherString = "Create"

    def createQueryString(self):
        with open(self.__staging_file, 'r') as file:
            c_file = csv.DictReader(file)
            i = 0

            for row in c_file:
                index = str(i)
                if i == 0:
                    self.__cypherString += "(a"  ":MAIN{name:" + "\"" + self.__github_searchString + "\"" + \
                        "})<-[:IS_PART_OF]-(b"+index + \
                        ":REPOSITORY{repo_url:" + "\"" + \
                        row["User_Repo"] + "\"" + \
                        "})<-[:CONTRIBUTES_TO]-(c"+index+":USER{user_name:" + \
                        "\""+row["User_Name"] + "\"" + ",user_url:" + \
                        "\""+row["User_Url"] + "\"" + "}"+"),"
                else:
                    self.__cypherString += "(a)<-[:IS_PART_OF]-(b"+index + \
                        ":REPOSITORY{repo_url:" + "\"" + \
                        row["User_Repo"] + "\"" + \
                        "})<-[:CONTRIBUTES_TO]-(c"+index+":USER{user_name:" + \
                        "\""+row["User_Name"] + "\"" + ",user_url:" + \
                        "\""+row["User_Url"] + "\"" + "}"+"),"
                i += 1

    def getCypherString(self):
        last_index = len(self.__cypherString) - 1
        # print()
        print(last_index)
        resultString = ""
        resultString = self.__cypherString[0:int(last_index)]
        return resultString
