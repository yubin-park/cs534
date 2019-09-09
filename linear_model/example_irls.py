from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
from scipy.special import expit

data = load_breast_cancer()
X = data.data
n, m = X.shape
X = np.append(np.ones(n).reshape(n, 1), X, axis=1)
y = data.target

def loss(y, X, beta):
    ll = y * np.dot(X, beta) - np.log(1 + np.exp(np.dot(X, beta)))
    return -np.sum(ll)

beta = np.zeros(m+1)
loss_lst = []
loss_lst.append(loss(y, X, beta))
for i in range(30):
    p = expit(np.dot(X, beta))
    W = np.diag(p * (1-p))
    XWXinv = np.linalg.inv(np.dot(np.dot(X.T, W), X))
    beta = beta + np.dot(XWXinv, np.dot(X.T, y-p))
    loss_lst.append(loss(y, X, beta))
print(loss_lst)

eps = 1e-5
beta = np.zeros(m+1)
loss_lst = []
loss_lst.append(loss(y, X, beta))
for i in range(30):
    p = np.clip(expit(np.dot(X, beta)), eps, 1-eps)
    W = np.diag(p * (1-p))
    XWXinv = np.linalg.inv(np.dot(np.dot(X.T, W), X))
    beta = beta + np.dot(XWXinv, np.dot(X.T, y-p))
    loss_lst.append(loss(y, X, beta))
print(loss_lst)


