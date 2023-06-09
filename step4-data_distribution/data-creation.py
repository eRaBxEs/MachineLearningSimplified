# To create big data sets for testing, we use the Python module NumPy, 
# which comes with a number of methods to create random data sets, of any size.

import numpy

# A single random number
y = numpy.random.uniform(2, 5)
print(y)

# Create an array containing 250 random floats between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)

print(x)