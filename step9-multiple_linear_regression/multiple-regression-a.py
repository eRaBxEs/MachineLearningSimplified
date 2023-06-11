import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

# Make a list of the independent values and call this variable X
X = df[['Weight','Volume']] 

# Put the dependent values in a variable called y.
y = df['CO2'] 

reg = linear_model.LinearRegression() # Creates a linear regression object
# fit() takes the dependent and independent values as parameters and fills the regression object with data that describes the relationship
reg.fit(X, y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictCO2 = reg.predict([[2300, 1300]])
print(predictCO2)