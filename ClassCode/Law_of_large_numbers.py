# LAW OF LARGE NUMBERS
import numpy as np
import time
from numpy.random import randn


def coinToss():

    NUM_OF_COIN_TOSSES = None
    x = ''
    avgOne = 0
    avgTwo = 0
    avgThree = 0
    x = input("Enter the number of coin tosses OR Press q to exit = ")
    while(not(x == 'q')):

        NUM_OF_COIN_TOSSES = int(x)
        counterOne = 0
        counterTwo = 0
        counterThree = 0
        for i in range(NUM_OF_COIN_TOSSES):
            y = randn()
            if y >= -1 and y <= 1:
                counterOne += 1
            elif y >= -2 and y <= 2:
                counterTwo += 1
            else:
                counterThree += 1

        avgOne = (counterOne/NUM_OF_COIN_TOSSES)*100
        avgTwo = (counterTwo/NUM_OF_COIN_TOSSES)*100
        avgThree = (counterThree/NUM_OF_COIN_TOSSES)*100
        print("The average 1 is -->", avgOne)
        print("The average 2 is -->", avgTwo)
        print("The average 3 is -->", avgThree)
        print(round(avgOne + avgTwo + avgThree))
        x = input("Enter the number of coin tosses OR Press q to exit = ")


# print()
startTime = time.time()
coinToss()
endTime = time.time()
timeTaken = endTime - startTime
print(timeTaken)
