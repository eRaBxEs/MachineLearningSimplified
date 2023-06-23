import pandas
from sklearn import linear_model


df = pandas.read_csv("data.csv")

X = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()

regr.fit(X, y)

predictCO2 = regr.predict([[3300, 1300]])

print(predictCO2)

# Coefficient : [0.00755095 0.00780526] : 
# The coefficient of multiple Linear regression always have to be two, one for the x-axis and the other for the y-axis
"""

     The predicted C02 for weight of 2300kg and volume 1000cm3 = [107.2087328]
     So since the weight was increased by 1000kg,
     the new predicted CO2 = 107.2087328 + 1000 * 0.00755095.
     I have written a code to check this below:

"""
rounded_1 = round(predictCO2[0], 2)
if  rounded_1 == round(107.2087328 + (1000 * 0.00755095), 2):
    print("Coefficient rocks!")
