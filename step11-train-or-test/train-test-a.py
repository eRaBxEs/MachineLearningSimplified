# 80% for training and 20% for testing
# Data represents 100 customers in a shop and their shopping habit
import numpy
import  matplotlib.pyplot as plt
numpy.random.seed(2) # seeding the random function

x = numpy.random.normal(3, 1, 100) # The x axis represents the number of minutes before making a purchase.
y = numpy.random.normal(150, 40, 100) / x # The y axis represents the amount of money spent on the purchase.

plt.scatter(x, y)

plt.show()
