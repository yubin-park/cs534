from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

figsize = (6, 5)

# linear regression intro
data = load_boston()
X = data.data
n, m = X.shape
X = np.append(np.ones(n).reshape(n, 1), X, axis=1)
y = data.target
columns = ["Intercept"] + data.feature_names.tolist()
beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))
y_hat = np.dot(X, beta)
df = pd.DataFrame({"y": y, "y_hat": y_hat})
ax = df.plot.scatter(x="y_hat", y="y", figsize=figsize)
fig = ax.get_figure()
fig.savefig("img/boston_simplefitting.png")
ax.clear()


# z-score
from collections import Counter
sigma = np.sqrt(np.sum(np.square(y - y_hat))/(n-m-1))
XTX = np.linalg.inv(np.dot(X.T, X))
nu = np.diag(XTX)
z = beta/sigma/np.sqrt(nu)
z_counter = Counter({k:np.abs(v) for k, v in zip(columns, z)})
for k, v in z_counter.most_common():
    print("{0:<12}{1:>5.2f}".format(k, v))

mse = np.sqrt(np.sum(np.square(y - y_hat))/n)
print("MSE with linear features: {}".format(mse))

# feature expansion
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(2, interaction_only=True)
X = poly.fit_transform(data.data)
n, m = X.shape
y = data.target
beta = np.dot(np.linalg.inv(np.dot(X.T, X) ), np.dot(X.T, y))
y_hat = np.dot(X, beta)
mse = np.sqrt(np.sum(np.square(y - y_hat))/n)
print("MSE with poly(2) features: {}".format(mse))

df = pd.DataFrame({"y": y, "y_hat": y_hat})
ax = df.plot.scatter(x="y_hat", y="y", figsize=figsize)
fig = ax.get_figure()
fig.savefig("img/boston_poly2_interTrue.png")
ax.clear()

poly = PolynomialFeatures(2, interaction_only=False)
X = poly.fit_transform(data.data)
n, m = X.shape
y = data.target
beta = np.dot(np.linalg.inv(np.dot(X.T, X) ), np.dot(X.T, y))
y_hat = np.dot(X, beta)
mse = np.sqrt(np.sum(np.square(y - y_hat))/n)
print("MSE with poly(2) features: {}".format(mse))

df = pd.DataFrame({"y": y, "y_hat": y_hat})
ax = df.plot.scatter(x="y_hat", y="y", figsize=figsize)
fig = ax.get_figure()
fig.savefig("img/boston_poly2_interFalse.png")
ax.clear()

XTX = np.linalg.inv(np.dot(X.T, X))
nu = np.diag(XTX)
print(nu)


