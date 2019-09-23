# Homework \#1

Due 09/23

## Submission Instruction

In this homework, you will implement two machine learning algorithms: **Ridge Regression** and **Forward-Stagewise Regression** with a little twist. 
For this homework, you need to download [`hw1_template.py`](hw1_template.py) (homework template) and fill out the empty classes in the template.

The homework must be submitted electronically on Canvas as a single submission.
The submission will be a single Python file named as `hw1.py`.
TA will run automatic test scripts to grade the submissions. Please note that:
- If your homework does not adhere to the naming convention, you will receive zero points for the homework.
- If your source code is flagged for being too similar to other submissions, you will be automatically reported for cheating. We will assess the software similarity with [MOSS](https://theory.stanford.edu/~aiken/moss/).

*Please do not use other libraries except for `numpy`.*


## [Problem 1] Ridge Regression with Prior Coefficients (50 points)

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

1. Normalize `X` (5 points)
1. Scale `coef_prior` according to the normalized `X` (5 points)
1. Derive a closed-form solution for the new loss function and solve it (15 points)
1. Adjust `coef` and `intercept` for the de-normalized `X` (5 points)

Please take a look at the `Ridge` class in the template for more details.

TAs will test if the estimated coefficients are valid or not.
If the coefficients are valid, then you will receive 20 points more.
An example test script is as follows:

```python
from hw1 import Ridge

coef_prior = ... # TA will pick a random vector 
X, y = ... # TA will choose a dataset for grading

ridge = Ridge()
ridge.fit(X, y, coef_prior=beta_prior)
intercept, coef = ridge.get_coef() # TA will test if the coefficients are valid
```

## [Problem 2] Incremental Forward-Stagewise with Cannot-Link Constraints (50 points)

Congratulations! 
Your client was satisfied with your custom Ridge Regression solution.
They were pleased by its predictive performance and coefficients that adhere to their domain knowledge.
However, after using the solution for a while, they came back with some improvement ideas.

They are saying that the new Ridge Regression solution works great, 
but the model is a bit complex; too many non-zero coefficients.
To address this issue, their domain experts came up with a suggestion.
They categorized similar features into a few groups.
They think at most one of the features in the same group should be active (i.e. non-zero coefficient) in the model.

For example, if the first and second columns of the feature matrix are in the same group, 
the model should use at most one of the column, not both. 
This type of model constraint is often called as "cannot-link" constraint.
The cannot-link constraint will be expressed as follows:

```
cannot_link = [[0, 1], [2, 3, 4], [5, 6]]
```

The above example tells that the `0, 1` columns cannot be together, and `2, 3, 4` columns cannot be together, and so on.

Incorporating this cannot-link constraint into Ridge will be non-trivial.
This time, rather than using Ridge, you want to use Forward-Stagewise Regression.
Given the simplicity of Forward-Stage Regression, you can incorporate this constraint in a relatively simple manner.

Forward-Stagewise updates one coefficient at a time. 
At each iteration, we will check if any of the cannot-link groups is activated or not.
If activated, then we will ignore the updates for the variables in their affiliated groups, 
and perform the next best update. 

Your job is to implement a Python class that minimizes the above loss function and saves the estimated coefficients.
Here are the overall steps to implement this new method:

1. Normalize `X` (5 points)
1. Implement Incremental Forward-Stagewise (5 points)
1. Implement Cannot-Link Constraint inside the Forward-Stagewise process (10 points)
1. Adjust `coef` and `intercept` for the de-normalized `X` (5 points)
1. Construct a numpy array for the `path` variable (5 points)

Please take a look at the `ForwardStagewise` class in the template for more details.

TA will test if the estimated coefficients are valid or not.
If the coefficients are valid, then you will receive 20 points more.
An example of such test scripts is as follows:


```python
from hw1 import ForwardStagewise

cannot_link = ...
X, y = ... 

fsw = ForwardStagewise()
fsw.fit(X, y, lmbd=1.0, cannot_link=cannot_link)
fsw.get_coef_path()
```

## [Problem 3] Bonus (0 point)

**Problem 3 will not be graded.**
This problem is meant to give you some ideas how all these pieces can be put together.

How would you combine the ideas from Problem 1 and Problem 2?
Can you think of a solution that incorporates prior coefficients and cannot-link constraints at the same time?
