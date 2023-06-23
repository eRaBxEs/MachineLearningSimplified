# Now that we can ascertain that our model is okay, 
# we have to use our model with the test data set to see if it gives the same result
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x # always use x as the denominator

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r = r2_score(test_y, mymodel(test_x)) # checking the model with our test data set
print(r) # The result is 0.81 stills shows that our model is still okay. 