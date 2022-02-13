import os
import time

# stage = os.environ["ALLUSERSPROFILE"].upper()
# print("THE ENVIRONMENT IS")
# print(stage)


# stage = os.getenv("STAGE", "dev").upper()

# print("WIHLE USING getenv")
# print(stage)

# now = time.localtime()
# print(str(now.tm_year) + " " + str(now.tm_mon))

# print("The year is {0} \n And the month is {1}".format(
#     now.tm_year, now.tm_mon))


# listA = [1, 2, 3]

# print(listA)

# listA.append("Chandan")

# print(listA)

# listA.append(10.4)

# print(listA)

# dict = {"key1": "v1", "k2": "v2"}

# print(dict.get("k2"))


# u_input = int(input("Enter some thing\n"))


# def printSomething(user_passed_something):
#     return user_passed_something


# print(type(printSomething(u_input)))

# def add_two(number):
#     return 2 + number


# print("The sum is \t" + str(add_two(23)))


def muti_func():
    height = 180
    weight = 85
    system = "Ubuntu"
    return height, weight, system


# print(muti_func())

# tup = muti_func()
# print(tup[0])

# # print(tup)
# # lista = [1, 2]

# # print(lista)

# for i in range(len(tup)):
#     if i == 1:
#         tup[i] = 'Chandan'
#         print(tup[i])
#     else:
#         continue


now = time.localtime()

print(str(now.tm_year) + " " + str(now.tm_mon))
