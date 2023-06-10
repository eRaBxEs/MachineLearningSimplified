# Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
import numpy
import matplotlib.pyplot as plt

# The first array will have the mean set to 5.0 with a standard deviation of 1.0.
x = numpy.random.normal(5.0, 1.0, 1000)

# The second array will have the mean set to 10.0 with a standard deviation of 2.0:
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)

plt.show()