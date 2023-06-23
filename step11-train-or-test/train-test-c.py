import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# training set
train_x = x[:80]
train_y = y[:80]

# test set
test_x = x[80:]
test_y = y[80:]

# using the test data set
plt.scatter(test_x, test_y) 

plt.show() # The testing set also looks like the original data set


