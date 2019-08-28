from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

# stepwise
data = load_boston()
X = data.data
n, m = X.shape
X = np.append(np.ones(n).reshape(n, 1), X, axis=1)
y = data.target
columns = ["Intercept"] + data.feature_names.tolist()
X_df = pd.DataFrame(X, columns=columns)

col_sel = ["Intercept"]
columns.remove("Intercept")
mse_lst = []
while len(columns) > 0:
    col = columns[0]
    mse_min = np.inf  
    for col in columns:
        X_tmp = X_df.loc[:,col_sel + [col]]
        XTXinv = np.linalg.inv(np.dot(X_tmp.T, X_tmp))
        beta = np.dot(XTXinv, np.dot(X_tmp.T, y))
        y_hat = np.dot(X_tmp, beta)
        mse = np.mean(np.square(y - y_hat))
        if mse < mse_min:
            mse_min = mse
            col_best = col
    columns.remove(col_best)
    col_sel.append(col_best)
    mse_lst.append(mse_min)

print(col_sel)

#df = pd.DataFrame({"mse": mse_lst, "nvars": np.arange(len(mse_lst))})
#ax = df.plot.line(x="nvars", y="mse", figsize=(8,4))
#fig = ax.get_figure()
#fig.savefig("img/boston_forwardstepwise.png")
#ax.clear()

from sklearn.preprocessing import scale

# Forward Stagewise

data = load_boston()
X = scale(data.data)
n, m = X.shape
y = data.target
columns = data.feature_names.tolist()

nsteps = 1000
delta = 1e-2
beta = np.zeros(m)
y = y - np.mean(y)

path = []
for s in range(nsteps):
    r = y - np.dot(X, beta)
    mse_min, j_best, gamma_best = np.inf, 0, 0
    for j in range(m):
        gamma_j = np.dot(X[:,j], r)/np.dot(X[:,j], X[:,j])
        mse = np.mean(np.square(r - gamma_j * X[:,j]))
        if mse < mse_min:
            mse_min, j_best, gamma_best = mse, j, gamma_j
    if np.abs(gamma_best) > 0:
        beta[j_best] += gamma_best * delta
        path.append(beta.tolist())

df = pd.DataFrame(path, columns=columns)
ax = df.plot.line(figsize=(8,4))
fig = ax.get_figure()
fig.savefig("img/boston_forwardstagewise.png")
ax.clear()




