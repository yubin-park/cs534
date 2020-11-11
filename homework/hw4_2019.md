# Homework \#4

Due 11/18

## Submission Instruction

The homework must be submitted electronically on Canvas as a single submission.
The submission will be a single Python file named as `hw4.py`.
TA will run automatic test scripts to grade the submissions. Please note that:
- If your homework does not adhere to the naming convention, you will receive zero points for the homework.
- If your source code is flagged for being too similar to other submissions, you will be automatically reported for cheating. We will assess the software similarity with [MOSS](https://theory.stanford.edu/~aiken/moss/).

## kNN with Greedy Feature Selection

Please use [the breast cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer) for this problem.

In this homework, you will implement `class GreedyKNN`, a variant of kNN that borrows the idea from Forward Selection Linear Regression. The outline of the algorithm is as follows:

- Use [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) for the algorithm
- First, complete the following function:

```python
def get_feature_order(X, y, k=5):

	n, m = X.shape
	feature_lst = []

	while len(feature_lst) < m:
		max_auroc = 0.0
		max_var = -1
		for j in range(m):
			if j in feature_lst:
				continue
			# Implement your own kNNpredict function
			# The function should return kNN prediction for the given X, y, and k
			y_hat = kNNpredict(X[,feature_lst + [j]], y, k) # TODO
			auroc = # TODO: measure AUROC with y_hat and y
			if auroc > max_auroc:
				max_auroc = auroc
				max_var = j
		feature_lst.append(max_var)

	return feature_lst
```

- Test your code with the breast cancner dataset with/without standardizing the features. 
- Split the data into training and test sets, and run the `get_feature_order` on the training set
- Plot the test set AUROC performance across various kNN models built based on the first `t` features of `feature_lst`
- Change `k` to different values and interpret the results in terms of the bias-variance tradeoff.
