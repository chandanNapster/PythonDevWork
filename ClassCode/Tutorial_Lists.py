##LET US CREATE SOME LISTS
myList = []
myList.append(1)
myList.append(1)
myList.append(1)
myList.append(1)
myList.append("Chandan")
myList.append("Chandan")
myList.append("Chandan")
myList.append(True)
myList.append(False)

myList2 = []

myList2.append("changes")
myList2.append("changes22")
myList2.append(myList)
print(myList2)

##FUNCTIONS
x = list(range(len(myList2)))
for i in range(len(x)):
    print(myList2[i])

w = list(range(100,120,3))
print(w)

##USING BRACKETS
w = ['a','c','d','e']
print(w)

for i in range(len(w)):
    if i == 2:
        w[i] = 67
        
print(w)

##LYGOMETRY


##SLICING
alphaList = ['A','B','C','D','E','F','G','H','I','J']
print(alphaList)
print(alphaList[2:7])

for i in range(len(alphaList)):
    print(alphaList[i:len(alphaList)])

##ADVANCED SLICING
for i in range(len(alphaList)):
    print(alphaList[i*-1:len(alphaList)])


print(alphaList[::-1])
print("00000")
print(alphaList[7:1:-1])
      
##TUPLES IN PYTHON = IMMUTABLE SEQUENCE OF VALUES
t1 = ()

##for i in range(len(alphaList)):
##    t1.append(alphaList[i])
##   
##    
##print(len(t1))


##FUNCTIONS


myList3 = list(range(20,31))

def testFunc(aList):
    return max(aList[2:7])


print(testFunc(myList3))
































