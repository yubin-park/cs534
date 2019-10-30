from collections import defaultdict
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

np.random.seed(4)

data = load_iris()
scaler = StandardScaler()
X = data.data
y = (data.target == 1).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

n, m = X.shape
R = 20
B = 5
U_lst = [np.random.randn(m, R) for b in range(B)]

def simhash(x, U):
    return "".join([str(int(h>0)) for h in np.dot(x, U)])

def fit(X, y, U_lst):
    n, m = X.shape
    B = len(U_lst)
    htab = [defaultdict(list) for b in range(B)]
    for i in range(n):
        x_i = X[i,:]
        y_i = y[i]
        for b in range(B):
            key = simhash(x_i, U_lst[b])
            htab[b][key].append((x_i, y_i))
    return htab

def predict(X, U_lst, htab):
    y_hat = []
    n, m = X.shape
    B = len(U_lst)
    for i in range(n):
        x_i = X[i,:]
        y_hat_i = 0.0
        for b in range(B):
            key = simhash(x_i, U_lst[b])
            if key not in htab[b]:
                continue
            pairs = htab[b][key]
            X_nn = np.array([p[0] for p in pairs])
            idx = np.argsort(np.dot(X_nn, x_i))[-1]
            y_hat_i = [p[1] for p in pairs][idx]
            break
        y_hat.append(y_hat_i)
    return y_hat
            
htab = fit(X_train, y_train, U_lst)
y_hat = predict(X_test, U_lst, htab)
print(y_test)
print(np.array(y_hat))
acc = np.mean(y_hat == y_test)
print(acc)
print(np.mean(y_test))


