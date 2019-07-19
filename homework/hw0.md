# Homework \#0

Due mm/dd

## Problem 1

It is your first day as a data scientist at your dream company.
However, your team recently had a huge turnover of staffs, 
and many of projects and data files are not trackable.
Your boss comes to you and asks:
> "Hey, here is a data file I found in our data warehouse, but I don't know what this is. Can you figure out?"

There is no description of the data file and no one to ask.
You will read the file (download from [here](hw0_p1.csv)) and see if you find any underlying patterns.
Hopefully, such patterns may give a hint for your boss to figure what that is.

Find out any patterns in the data, and provide the evidence and Python script for such patterns.

[hint] You can read the file as follows:
```python
import pandas as pd
data = pd.read_csv("{path to the file}")
```

## Problem 2

You recently cashed out your stock options, and now you have some money to invest.
You are thinking of investing in the stock market, and you want to do it wisely.
Being a data scientist, you believe historic patterns of stock prices may have some signals for future prices.
First, you decide to analyze Apple (NASDAQ: AAPL). 

1. Download the data from [here](AAPL.csv), and plot the daily closing prices over time using Python.
1. Daily return is calculated as the ratio of consecutive closing prices (i.e. today's closing price divided by yesterday's closing price). 
From the data, obtain the mean and variance of the Apple stock's daily return.
1. You think the daily return is a moving target, and you want to see the daily returns calculated in each year. Using the data, calculate the daily returns for the Year 2014, 2015, 2016, 2017, 2018, and 2019. 


## Problem 3

Your 3 year-old son is an evil genius. 
While Mom is busy washing dishes, your son came up with a very silly game of mixing his chocolate milk and orange juice.
He first pours 30% of chocolate milk to the cup that has orange juice originally, 
then pours 20% of whatever-it-is-now in the orange juice cup to the chocolate milk cup. 
He started with exactly 1 cup of chocolate milk and 1 cup of orange juice. 

1. He just went through the first cycle of mixing each other cup. How much liquid is in each cup now?
1. He went through 10 cycles of mixing things. How much liquid is in each cup now?
1. Create a Pandas data frame with the columns of `number_of_cycle, volume_of_chocolate_cup, volume_of_orange_cup`. The number of cycle variable ranges from 1 to 100. 

[hint] Use Python to simulate the process.
```python
import numpy as np

choco_to_orange = np.array([[0.7, 0], [0.3, 1]])
orange_to_choco = np.array([[1, 0.2], [0, 0.8]])
one_cycle = np.dot(orange_to_choco, choco_to_orange)

state0 = np.array([1, 1])
state1 = np.dot(one_cycle, state0)

```



