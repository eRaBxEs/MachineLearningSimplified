# Percentiles are used in statistics to give you a number 
# that describes the value that a given percent of the values are lower than or equal.

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# What is the age that 75% of the people are younger than?
p = numpy.percentile(ages, 75)

print(p)