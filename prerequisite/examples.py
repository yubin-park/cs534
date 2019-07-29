from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

data = load_boston()
X = data.data
y = data.target
df = pd.DataFrame(X, columns = data.feature_names)
df["MEDV"] = y
n, m = df.shape # n: number of rows, m: number of columns

#print(df.head())
#print(df["RM"].values[:100])

#col = "RM" # the number of rooms
col = "MEDV" # median price of houses

xmin = df[col].min()
xmax = df[col].max()
figsize = (3.6, 2.7)

ax = df[col].hist(bins=10, figsize=figsize) # histogram
ax.set_xlim(xmin, xmax) # setting the range of x-axis
fig = ax.get_figure()
fig.savefig("img/histogram_{}.png".format(col))
ax.clear()

col_cdf = "CDF_{}".format(col) # a new variable name
df = df.sort_values(by=[col])
df = df.reset_index() # reindex from the smallest RM to largest RM
df[col_cdf] = df.index / n # normalize by the number of rows
ax = df.plot.line(x=col, y=col_cdf, figsize=figsize)
fig = ax.get_figure()
fig.savefig("img/cdf_{}.png".format(col))
ax.clear()

np.random.seed(1)

mu = np.mean(df[col]) # mean
sigma2 = np.var(df[col]) # variance
sigma = np.sqrt(sigma2) # standard deviation

col_simul = "{}_simul".format(col)
df[col_simul] = sigma * np.random.randn(n) + mu # random samples
ax = df[col_simul].hist(bins=10, figsize=figsize)
ax.set_xlim(xmin, xmax)
fig = ax.get_figure()
fig.savefig("img/histogram_{}.png".format(col_simul))
ax.clear()

#def normal_pdf(x, mu, sigma):
#    sigma2 = np.square(sigma)
#    pdf = np.exp(-np.square(x - mu)/2/sigma2)
#    norm_const = np.sqrt(2*np.pi*sigma2)
#    return pdf/norm_const

ax = df.boxplot(column="MEDV", by="CHAS")
fig = ax.get_figure()
fig.savefig("img/boxplot_CHAS_MEDV.png")
ax.clear()

a = df.loc[df["CHAS"]==0,"MEDV"].values
b = df.loc[df["CHAS"]==1,"MEDV"].values

from scipy import stats

print(stats.ttest_ind(a, b))


