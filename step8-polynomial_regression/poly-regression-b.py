import numpy
import matplotlib.pyplot as plt

# The x-axis represents the hours of the day and the y-axis represents the speed:
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy has a method that lets us make a polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Start at positiion 1 and stop at 22 on x-axis and start at position 1 and stop at 100 on y-axis
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)

# Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))

plt.show()
