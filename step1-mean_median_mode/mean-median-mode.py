# In the mind of a computer, a data set is any collection of data, an array to a complete database
import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Get the mean
x = numpy.mean(speed)

print(x)

# Get the median
y = numpy.median(speed)

print(y)


# Get the mode
p = stats.mode(speed)

print(p)
