# Homework \#2

Due 10/01

## Submission Instruction

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


## Predict Tomorrow's Stock Movements

You are doing an internship at a hedge fund. 
You love the firm's culture and generous salaries, and you want to get a full-time offer badly.
You want to impress your boss by showing your predictive analytics skills in predicting tomorrow's stock price.

Your first target is Apple (AAPL). 
However, as always, real-world problems are not easy.
You tried various features and models, but none of the results look satisfying.
Your kind boss noticed you are struggling with the problem.
He comes over and gives some hints.
> "In trading, the squared loss is just one metric. You can try other evaluation metrics, and perhaps, you can set up a different target variable such as if the tomorrow's price will go up by at least 1% up or not. You may find some interesting trading ideas."

In this homework problem,
1. Download the Apple data form [here](AAPL.csv)
2. Your test set will be May, June, July of 2020. You should set up your own target varible such as tomorrow's closing price, tomorrow's percent change, a percent change with a threshold, etc., that meet your trading idea. However, please focus on predicting future values - don't bring any values from the past.
3. Make various features that may help your predictive algorithms e.g. moving average
4. Use Elastic-Net with varying `alpha` and `lambda` - for the purpose of the problem, do not use other machine learning algorithms. Use the [sklearn Elastic Net](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html).
5. Use various evaluation metrics and targets and interpret your results.

Note that you are allowed to explore different evaluation metrics. For example, if you want to predict if AAPL will fall more than 2% in the next day, you can deploy a short-selling strategy to gain some profits. In this case, you would be solving a binary classification problem, not a regression problem. 

On the other hand, if you want to use call/put options, then you would want to predict something different. How would you come up with a reasonable strategy based on your predictions, and how would you formulate a machine learning problem to achieve that? 

Please come up with something of your own and think about what interesting things you can find with this stock data. 







