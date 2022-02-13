##LAW OF LARGE NUMBERS
import numpy as np
from numpy.random import randn

NUM_OF_COIN_TOSSES = None

x = None

while(not(x==0)):

    x = input("Enter the number of coin tosses OR Press 0 to exit = ")

    NUM_OF_COIN_TOSSES = int(x)

    toss_result = None

    headList = []
    tailList = []

    headPercentage = 0
    tailPercentage = 0



    for i in range(NUM_OF_COIN_TOSSES):
        y = randn()
        if y >= 0:
            toss_result = "HEAD"
            headList.append(toss_result)
        else:
            toss_result = "TAIL"
            tailList.append(toss_result)

    headPercentage = len(headList)/NUM_OF_COIN_TOSSES
    tailPercentage = len(tailList)/NUM_OF_COIN_TOSSES
    print("The head percentage =", headPercentage, "   ", "The tail percentage =", tailPercentage)

        
