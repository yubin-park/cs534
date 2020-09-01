# Homework \#1

Due 09/15

## Submission Instruction

In this homework, you will implement two machine learning algorithms: **Ridge Regression** and **Forward-Stagewise Regression** with a little twist. 
For this homework, you need to download [`hw1_template.py`](hw1_template.py) (homework template) and fill out the empty classes in the template.

The homework must be submitted electronically on Canvas as a single submission.
The submission will be a single Python file named as `hw1.py`.
TA will run automatic test scripts to grade the submissions. Please note that:
- If your homework does not adhere to the naming convention, you will receive zero points for the homework.
- If your source code is flagged for being too similar to other submissions, you will be automatically reported for cheating. We will assess the software similarity with [MOSS](https://theory.stanford.edu/~aiken/moss/).

*Please do not use other libraries except for `numpy`.*


## Ridge Regression with Prior Coefficients (100 points)

You are really fond of Ridge Regression.
Ridge Regression works well for colinear feature matrices 
and provides robust predictive performance overall.
You have been using it for every data science project, until now.

You have a new project with a somewhat small dataset from a client.
Some domain experts at the client site claim that 
they have rough estimates on a certain set of coefficients, `coef_prior`.

However, if we use the regular Ridge Regression, 
then many of the coefficients will be estimated near zeros, 
which doesn't conform with the experts' domain knowledge.
For this project, given the size of the dataset, 
you want to incorporate this prior knowledge into your Ridge Regression as much as possible.

You have been thinking for some time, and
finally, you came up with an idea.
The idea is to modify the penalty term of the loss function to reflect the prior knowledge.
A new loss function should be as follows:

```
np.sum(np.square(y - np.dot(X, coef))) + lmbd * np.sum(np.square(coef - coef_prior))
```

Your job is to implement a Python class that minimizes the above loss function and saves the estimated coefficients.
Here are the overall steps to implement this new method:

1. Normalize `X` 
1. Scale `coef_prior` according to the normalized `X` 
1. Derive a closed-form solution for the new loss function and solve it 
1. Adjust `coef` and `intercept` for the de-normalized `X` 

Please take a look at the `MyRidge` class in the template for more details.

More detailed questions in the homework template. 
Please read the homework template carefully, and fill in the blanks with both Python codes and comments.




