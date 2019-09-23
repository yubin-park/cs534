# Homework \#2

Due 10/02

## Submission Instruction

In this homework, you will implement two machine learning algorithms: **Ridge Regression** and **Forward-Stagewise Regression** with a little twist. 

The homework must be submitted electronically on Canvas as a single submission.
The submission will be a single Python file named as `hw2.py`.
TA will run automatic test scripts to grade the submissions. Please note that:
- If your homework does not adhere to the naming convention, you will receive zero points for the homework.
- If your source code is flagged for being too similar to other submissions, you will be automatically reported for cheating. We will assess the software similarity with [MOSS](https://theory.stanford.edu/~aiken/moss/).

## Logistic Regression for Brier Score

Logistic regression estimates its coefficients by maximizing the Bernoulli-form log-likelihood function. 
But as usual, your crazy boss wants to tweak the loss function a bit.
Rather than optimizing the log-likelihood, we want to minimize the squared loss, [Brier Score](https://en.wikipedia.org/wiki/Brier_score), while retaining the logistic link function.

In other words, for the `i`th sample, the loss is given as follows:

```python
np.square(y[i] - intercept - expit(np.dot(X[i,:], coef)))
```

Using the matrix notation, the loss function for the full data is:

```python
np.sum(np.square(y - intercept - expit(np.dot(X, coef))))
```

Note that `y` is either `0` or `1`.

In this homework problem,

1. Derive the first derivative of the loss function
2. Implement Newton's method to solve the equation
3. Estimate the coefficients for the [breast cancer data](https://scikit-learn.org/stable/datasets/index.html#breast-cancer-dataset)
4. Compare the coefficients from the regular Logistic regression and interpret the differences


## Predict Tomorrow's Price

You are doing an internship at a hedge fund. 
You love the firm's culture and generous salaries, and you want to get a full-time offer badly.
You want to impress your boss by showing your predictive analytics skills in predicting tomorrow's stock price.

Your first target is Apple (AAPL). 
However, as always, real-world problems are not easy.
You tried various features and models, but none of the results look satisfying.
Your kind boss noticed you are struggling with the problem.
He comes over and gives some hints.
> "In trading, the squared loss is just one metric. You can try other evaluation metrics. You may find some interesting trading ideas"

In this homework problem,
1. Download the Apple data form [here](AAPL.csv)
2. Your test set will be May, June, July of 2019. You will predict tomorrow's closing price using past prices and volumes.
3. Make various features that may help your predictive algorithms e.g. moving average
4. Use Elastic-Net with varying `alpha` and `lambda` - for the purpose of the problem, do not use other machine learning algorithms. Use the [sklearn Elastic Net](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html).
5. Use various evaluation metrics and interpret your results.







