# THIS PROGRAM IS USED AS AN ILLUSTRATION TO pyplot

import matplotlib.pyplot as plt
import numpy as np

URL = 'C://Users//A//Desktop//'

x = np.random.randn(1000)
# A HISTOGRAM WITH 100 BINS
plt.hist(x, 100)
plt.title(r'Normal Distribution with $\mu =0 , \sigma = 1$')
plt.savefig(URL + 'test.png')
