import matplotlib.pyplot as plt
from scipy import stats # Import scipy and draw the line of Linear Regression

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# Execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)
# Remember Y = MX + C

def myfunc(x):
    return slope * x + intercept

# creating a list that uses the function myfunc to create a list of values for models 
# by iterating thru the values of x
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()