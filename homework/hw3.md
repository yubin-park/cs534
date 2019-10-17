# Homework \#3

Due 10/21

## Submission Instruction

The homework must be submitted electronically on Canvas as a single submission.
The submission will be a single Python file named as `hw3.py`.
TA will run automatic test scripts to grade the submissions. Please note that:
- If your homework does not adhere to the naming convention, you will receive zero points for the homework.
- If your source code is flagged for being too similar to other submissions, you will be automatically reported for cheating. We will assess the software similarity with [MOSS](https://theory.stanford.edu/~aiken/moss/).

## Quarternary Decision Tree (classification)

Please use [the breast cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer) for this problem.

A regular decision tree splits data into two partitions at each node i.e. binary tree. 
In this problem, you will make a decision tree that splits in 4 ways - quarternary tree. 
To split the node in 4 ways, you will use 2 variables at the same time. 
For example, let's say `(x_1, s_1)` and `(x_2, s_2)` are two splitting varible and value pairs.
With these two pairs, you will have 4-way partitions as follows:
- `x_1 > s_1 and x_2 > s_2`
- `x_1 > s_1 and x_2 <= s_2`
- `x_1 <= s_1 and x_2 > s_2`
- `x_1 <= s_1 and x_2 <= s_2`

Your quarternary decision tree will grow 2 levels, which may produce maximum 16 nodes.
You will implement a Python class named as `class QuarternaryDecisionTree` that has two class methods:
- `fit(X, y)`: fits the quarternary decision tree and store the tree inside
- `predict(X)`: outputs the predictions for `X`

Test your algorithm using various evaluation strategies you learned from the class. 
Interpret which splitting pairs are selected.


## Divide-and-Regress (regression)

Please use [the boston housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston) for this problem.

A regular decision tree predicts with the mean value of the target variable at each node. 
In this problem, you will predict with an additional regression model.
At each node, you will fit a Ridge linear regression and use the model to enhance the mean value prediction.

In other words, you will use the minimum variance criterion to split the data into two partitions. After you split, you will apply a linear regression at each data partition, and use the regression model to predict for future data points.

Your divide-and-regress decision tree will grow 1 to 2 levels for this problem, but your code should be able to handle deeper depths. You will implement a Python class named as `class DaRDecisionTree` that has two class methods:
- `fit(X, y)`: fits a binary decision tree and store the tree inside
- `predict(X)`: outputs the predictions for `X`

Test your algorithm using various evaluation strategies you learned from the class. 
Interpret which splitting pairs are selected.


