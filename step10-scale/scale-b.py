# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_csv('data.csv')

X = df[['Weight', 'Volume']] # declaring the indepenedent values
y = df['CO2'] # declaring the dependedent value
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]]) # Scaling the given values

predictedCO2 = regr.predict([scaled[0]])

print(predictedCO2)




