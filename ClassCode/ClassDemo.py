##ALL MY CODE GOES HERE
import numpy as np
from numpy.random import randn

firstNum = 0
secondNum = 1

x = input("Enter the count")
print("You printed " + x)

result = 0

for k in range(int(x)):
    result = firstNum + secondNum
    secondNum = firstNum
    firstNum = result
    print(result)

print(randn())



##    print(i+j)
##    i += 1
##    j += 1



















































