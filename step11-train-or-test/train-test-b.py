# Demonstrate using training and testing data sets
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2) # seeding the random function

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y) # plot the training data on a scatter plot
plt.show() # It looks like the original data set after illustrating it on a scatter plot, it seems to be a fair selection

