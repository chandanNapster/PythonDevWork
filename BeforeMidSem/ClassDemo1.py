import numpy as np
from re import X
import Helper.ReadData as rd
import os


location = os.getcwd() + '\\Dataset\\P4-Movie-Ratings.csv'

reader = rd.Data(location)

data = reader.getData()

# print(data.YearOfRelease)

# x = 22/7

# print(x)
# y = 22/7

# if(x == y):
#     print("Hello")
# else:
#     print("Welcome")


def recurs(x):
    print(x)
    sr = 200
    if x == 0:
        return sr
    else:
        x = x - 1
        return recurs(x)


print("Number is-->", recurs(10))


def sumDiff(x, y):
    sum = x + y
    diff = x - y
    mul = x * y
    div = x / y
    return sum, diff, mul, div


# print("Number is-->", recurs(10))

print(sumDiff(3, 9)[0], sumDiff(3, 9)[1])

d = sumDiff(3, 9)

print(d[1])
# RETURNS A TUPLE

# d[0] = 45


# print(data.columns)
# print(reader.methodOverloading(1))


def f(x):
    print('x')
    if x <= 1:
        return 1
    else:
        return x + f(x-1)


print(f(4))


Fruit = ('a', 'b', 'c', 'a')
print(Fruit[:2])
# str.lower()

print(str)


num = [1, 2, 3, 4, 5]
alp = ['a', 'b', 'c', 'd']

numAlp = [num, alp]


myArr = np.array(numAlp)
print(myArr[0])


dict = {'a': 1, 'b': 2, 'c': 3}

if 'a' in dict:
    print(dict['a'])
