import numpy
from sklearn.metrics import r2_score

# The x-axis represents the hours of the day and the y-axis represents the speed:
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

"""

It is important to know how well the relationship between the values of the x- and y-axis is, 
if there are no relationship the polynomial regression can not be used to predict anything.

The relationship is measured with a value called the r-squared.

"""

# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

