# from the initial/previous scatter plot, what does the diagram look like, the best fit for it would be ploynomial regression
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# get a model
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100) # the line for the dimension of both the x and the y axis

plt.scatter(train_x, train_y)

# draw the plot
plt.plot(myline, mymodel(myline))

plt.show() # display
