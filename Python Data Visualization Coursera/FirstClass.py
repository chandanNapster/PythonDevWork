# DATA VISUALIZATION
# IMPORT FIGURE CANVAS
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# IMPORT FIGURE ARTIST
from matplotlib.figure import Figure
fig = Figure()
canvas = FigureCanvas(fig)

# CREATE 1000 RANDOM NUMBERS USING NUMPY
x = np.random.randn(1000)

# CREATE AN AXES ARTIST
# 111 IS A MATLAB CONVENTION
# WHICH MEANS THAT GENERATE A GRID OF 1 * 1 AND USE THE 1ST BOX
ax = fig.add_subplot(111)

# GENERATE A HISTOGRAM
# WITH 100 BINS
ax.hist(x, 100)

ax.set_title('Normal Distribution with $\mu =0, \sigma = 1$')
fig.savefig('matplotlib_histogram.png')
