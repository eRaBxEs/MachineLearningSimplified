import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()


df = pd.read_csv('data.csv')

X = df[['Weight', 'Volume']] # Pick the indepenedent values that you want to scale

scaledX = scale.fit_transform(X) # Apply scaling

print(scaledX)

