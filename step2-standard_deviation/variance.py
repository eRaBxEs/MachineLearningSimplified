# Variance is another number that indicates how spread out the values are.

# In fact, if you take the square root of the variance, you get the standard deviation!

# Or the other way around, if you multiply the standard deviation by itself, you get the variance!

"""

To calculate the variance you have to do as follows:
    1. Find the mean : (32+111+138+28+59+77+97) / 7 = 77.4
    2. Find the difference between the values in the data set and the mean
    3. Find the square of each difference value respectively
    4. The variance is the average of these squared differences

"""
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)

# Get the standard deviation and multiply by itself to compare with the variance if they are equal
y = numpy.std(speed)
print(y)

if x == y**2:
    print("Square of the standard deviation gives the variance")
