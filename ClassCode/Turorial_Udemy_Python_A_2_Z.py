#SCRIPT TO JUST TWO NUMBERS
##x = input("Enter a number ")
##while not(int(x) == 0):
##    print('You entered ', x)
##    y = int(x) + 1
##    print(y*4)
##    x = input("Enter some number or press 0 to stop me!!!!")
##    if int(x) == 0:
##        print("Exiting the loop!! OK Byeeeeee")
##    elif int(x) == -1:
##        print("Obey what is say")
##    else:
##        print("Ok i will add 1 to", x , "and then multiple it by 4")
##
##
####THE TUTORIAL BOOLEAN VARIABLES AND OPERATORS
#### TRUE and FALSE
##print(4 < 5)
##print(4 == 6)
##print(4 == 4 and not(4 > 2))
##print (4 == 4 or not(4 > 2))
##
####FOR LOOPS
##for i in range(5):
##    print("Hello chandan ", i)
##
####RANGE --> A QUICK WAY TO CREATE A SET
##print(list(range(5)))
##
##
##
#### ANOTHER WAY
##myList = []
##myList.append(10)
##myList.append(100)
##myList.append(1000)
##
##for jj in myList:
##    print(jj)

##IF ELSE AND ELIF
## TO SEE WHERE NUMBERS ARE DISTRIBUTED
## GENERATED SOME RANDOM NUMBERS AND C WHERE THEY OCCUR
##------ -2------ -1 -------0--------1------2-------
##import numpy as np
##from numpy.random import randn
##
##answer = None
##
##for i in range(15):
##    x = randn()
##    if x >= 1 and x < 2:
##        answer = "Greater than 1"
####        x *= 10
##    elif x < 1 and x > -1:
##        answer = "Lesser than 1"
####        x *= 10
##    else:
##        answer = "Number is greater than 2 or the number is less than -1"
####        x *= 10
##    
##    print(x)
##    print(answer)
##    print("********************")
    
##TEST TO CHECK RANGE OF randn
import numpy as np
from numpy.random import randn

NUM = 3


for i in range(10000000):
    
    x = randn()
    if x > NUM:
        answer = x
    elif x < -NUM:
        answer = x
    else:
        answer = x - x
        continue
print("The answer is -->",answer)    
    
    
    
