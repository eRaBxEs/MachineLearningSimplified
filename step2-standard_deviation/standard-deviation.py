# Standard deviation is a number that describes how spread out the values are.

import numpy

speed_a = [86,87,88,86,87,85,86]
# A low standard deviation means that most of the numbers are close to the mean (average) value.
sdx = numpy.std(speed_a)

print(sdx)

speed_b = [32,111,138,28,59,77,97]

# A high standard deviation means that the values are spread out over a wider range.
sdy = numpy.std(speed_b)

print(sdy)