from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

# Least Angle Regression

data = load_boston()
X = scale(data.data)
n, m = X.shape
y = data.target
columns = data.feature_names.tolist()
y = y - np.mean(y)

path = []
lr = 1e-3
max_iter = 100
def soft_thr(beta, lmbd):
    beta[np.abs(beta) <= lmbd] = 0
    beta[beta > lmbd] -= lmbd
    beta[beta < -lmbd] += lmbd
    return beta

def loss_func(y, X, beta, lmbd):
    return (np.sum(np.square(y - np.dot(X, beta))) + 
            lmbd * np.sum(np.abs(beta)))

for lmbd in np.linspace(3.5, 0.0): 
    beta, loss = np.zeros(m), np.inf
    beta_new = soft_thr(lr * np.dot(X.T, y), lmbd) 
    loss_new = loss_func(y, X, beta, lmbd)
    i = 0
    while loss_new < loss and i < max_iter:
        loss, beta = loss_new, beta_new
        r = y - np.dot(X, beta)
        beta_new = soft_thr(beta + lr * np.dot(X.T, r), lmbd)
        loss_new = loss_func(y, X, beta_new, lmbd) 
        i += 1
    path.append(beta.tolist())

df = pd.DataFrame(path, columns=columns)
ax = df.plot.line(figsize=(8,4))
ax.legend(loc=7)
fig = ax.get_figure()
fig.savefig("img/boston_lasso.png")
ax.clear()


