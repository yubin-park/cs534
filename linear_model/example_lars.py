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
beta = np.zeros(m)
y = y - np.mean(y)

path = [beta.tolist()]
beta_lst = [np.dot(X[:,j], y)/np.dot(X[:,j], X[:,j]) for j in range(m)]
mse_lst = [np.sum(np.square(y - np.dot(X[:,j], beta_lst[j]))) 
            for j in range(m)]
j_init = np.argmin(mse_lst)
var_inactive = np.full(m, True)
var_inactive[j_init] = False
while np.any(var_inactive):
    var_active = ~var_inactive
    r = y - np.dot(X, beta)
    beta_k = beta[var_active]
    X_act = X[:,var_active]
    gamma = np.dot(np.linalg.inv(np.dot(X_act.T, X_act)), 
                    np.dot(X_act.T, r))
    Xgm = np.dot(X_act, gamma)
    alpha_min, j_best = np.inf, -1
    for j in np.where(var_inactive)[0]:
        alpha_a = np.dot(Xgm - X[:,j], r)/np.dot(Xgm - X[:,j], Xgm)
        alpha_b = np.dot(Xgm + X[:,j], r)/np.dot(Xgm + X[:,j], Xgm)
        alpha = min(np.clip(alpha_a, 0, 1), np.clip(alpha_b, 0, 1))
        if alpha < alpha_min:
            alpha_min, j_best = alpha, j
    alpha_min = np.clip(alpha, 0, 1)
    beta[var_active] += (alpha_min * gamma)
    var_inactive[j_best] = False
    path.append(beta.tolist())

df = pd.DataFrame(path, columns=columns)
ax = df.plot.line(figsize=(8,4))
ax.legend(loc=7)
fig = ax.get_figure()
fig.savefig("img/boston_lars.png")
ax.clear()



