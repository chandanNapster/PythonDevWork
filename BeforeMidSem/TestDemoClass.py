import numpy as np

ListA = [1, 2, 3, 4]
ListB = [1, 2, 3, 4]
ListC = [1, 2, 3, 4]
ListD = [1, 2, 3, 4]


myArr = np.array([ListA, ListB, ListC, ListD])


def myFunc(x, y):
    return x + y


def cal1(x, y):
    sum = x + y
    diff = x - y
    mul = x * y
    div = x / y
    return sum, diff, mul, div


# print(cal1(10, 20))

tup = cal1(10, 20)

# print(tup[1] == 40)

ListA = [1, 2, 3, 4]
ListB = [10, 21, 33, 42]
ListC = [11, 12, 13, 14]
ListD = [21, 22, 23, 24]

# ListA.append("chandan")

# print(ListA)

# ListA[4] = "Pratham"

myArr = np.array(ListA)

# print(myArr)

myArr2 = np.array([ListA, ListB, ListC, ListD])
