from sklearn import linear_model
import pandas as pd

dataset = pd.read_csv("boardgeekgame_dataset.csv")

print(dataset.head())


target = dataset.iloc[:,1].values #ave rating

print(target)

data = dataset.iloc[:,[3]]

print(data.head())

regression = linear_model.LinearRegression()

regression.fit(data, target)

X = [
	[279],#page169star
	[66],#24
	[689],#trivial
]

results = regression.predict(X)

print(results)