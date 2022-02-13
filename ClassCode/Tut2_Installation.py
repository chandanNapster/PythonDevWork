import os
import sys

print(os.getcwd())
print(sys.version)


data = 'Hello world'

print(data[0])
print(data[0].lower() + data[1:len(data)].upper())
print(len(data))


val = 99

list1 = [89,99,100,200,-1]

for v in list1:
    if val == v:
        print('Hello')
    elif val > v:
        print('rrr')
    else:
        print('very fast')


##TUPLES LISTS AND DICTINARIES
a = (1,2,3)
b = [1,2,3]
print(a)

##a[0] = 5
b[0] = 5

##print(a)
print(b)

##DICTIONARY
myDict = {'chandan':0, 'rohan':1, 'ron':2}

for dic in myDict.keys():
    print(myDict[dic])


def multiValueFunc(value, name):
    val = value + 1
    nam = name
    list1 = []
    list1.append(value)
    list1.append(nam)
##    list1.append(list1)
    return val, nam, list1


x,y,z = multiValueFunc(10,"chandan")

print(x)
print(y)
print(z)



##NUMPY


import numpy as np


myArry = np.array(z)

print(myArry)

from matplotlib import pyplot as plt

myArr = np.array([1,2,3,40,-1,2,3,4])
print(myArr)

plt.plot(myArr)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

plt.hist(myArr)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()



plt.scatter(myArr,myArr)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()




