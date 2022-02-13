import numpy as np


listA = []
listA.append(21.78)
listA.append(12.1)
listA.append(15)
listA.append(89.03)
listA.append(678.77)
listA.append(19.05)
listA.append(48.65)
listA.append(59.05)
listA.append(75.05)
listA.append(19.05)


##print(listA)

arryA = np.array(listA)

##print(arryA[2:arryA.size])

#print(arryA.mean())


##BASKETBALL TRENDS
##NBA (NATIONAL BASKETBALL ASSOCIATION) EXAMPLE
##MATRICES
##A[0,:] --> get everything in row 0
##A[:,0] --> get everything in column 0
## BUILDING FIRST MATRIX

matrx = np.reshape(listA, (5,2), 'F')

print(matrx[3,:])

print(arryA.reshape(5,2))

##OOP CONCEPTS
## np.array()

r1 = ['I', 'am', 'happy']
r2 = ['What', 'a', 'day']

print(np.array([r1, r2, listA,arryA]))

print(np.array([r1,r2]))


##DICTIONARIES
#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]

#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])


print(Games[0,:])
print(Games[2,:])
print(Games[2,9])

##Dictionaries
dict1 = {'key1':'val1', 'key2':'val2', 'key3':'val3'}
print(dict1['key1'])


dictCountry = {'Genrmany':2, 'France':'Been here', 'Sweden':True}

print(dictCountry['France'])







