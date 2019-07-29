# CS534 - Machine Learning

This repository contains course materials for [CS 534 - Machine Learning](https://www.cs.emory.edu/courses/atlas/graduate/) provided in Fall 2019 at [Emory University](http://www.emory.edu/home/index.html).

Course syllabus, slides, and homework are largely borrowed/copied from Professor Joyce Ho's [CS534 class](https://joyceho.github.io/course/cs534_f18/).

## Overview

["Software is eating the world,"](https://a16z.com/2011/08/20/why-software-is-eating-the-world/)
 said Marc Andreessen in 2011. 
By then, he was referring to companies like Amazon, Netflix, Apple, and Google who are massively transforming the traditional industries with the power of internet and software.
It was true in some sense, as apparent in [their enormous growth in market capitalization](https://www.investopedia.com/terms/f/faang-stocks.asp).

How did these companies become so successful?
There may be many reasons, one may say. 
Unfortunately, the answer to this question is beyond the scope of this course.
However, I find that one commonality of these companies remarkably stands out:
their love for data.
Six years later, Marc Andreessen's famous quote was wittily supplemented with
["..., but AI is going to eat software"](https://www.technologyreview.com/s/607831/nvidia-ceo-software-is-eating-the-world-but-ai-is-going-to-eat-software/)
by Jensen Huang.

We are living in an exciting time.
Artificial intelligence and its key engine, machine learning, are impacting [every aspect of our lives](http://www.bbc.com/future/machine-minds).
From shopping groceries to treating diseases, 
people are experimenting and adopting machine learning algorithms, 
achieving the level of productivity that was never possible before.

In this course, students will learn some of the fundamental concepts, theories, and algorithms of machine learning. 
Students will have a chance to implement and test some of the time-tested machine learning algorithms.
At the end of the class, students will be able to 
1) identify and formulate machine learning problems, 
2) implement and test appropriate machine learning algorithms, and
3) understand and articulate the limitations of the approaches.

_Prerequisites:_
- Undergraduate-level linear algebra
- Undergraduate-level probability 
- Undergraduate-level algorithms
- Programming ability in Python 

## Logistics

- Programming Language
  - Python is the primary language for the course
- Textbook
  1. [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman
  1. [A Course in Machine Learning](http://ciml.info/) by Hal Daum&#xE9; III
- Office Hours
  - 2:30 pm ET - 3:30 pm ET on Monday
  - 12:00 pm ET - 1:00 pm ET on Wednesday

## Schedule

| Date | Topic | Reference | Assignment |
| ---- | ----- | --------- | ---------- |
| 08/28 | [Introduction](prerequisite/slides.pdf) | . | [Homework #0](homework/hw0.md) |
| 09/04 | Prerequisite - Statistics | . | . |
| 09/09 | Linear Model - Regression (1)  | . | Homework #1 |
| 09/11 | Linear Model - Regression (2) | . | . |
| 09/16 | Linear Model - Classification | . | . |
| 09/18 | Linear Model - Other Distributions | . | . |
| 09/23 | Decision Tree | . | Homework #2 |
| 09/25 | Boosting | . | . |
| 09/30 | Bootstrap | . | . |
| 10/02 | Random Forests | . | Homework #3 |
| 10/07 | Bias-Variance Tradeoff | . | . |
| 10/09 | Evaluation Metrics | . | . |
| 10/16 | Evaluation Strategies | . | . |
| 10/21 | _Midterm Exam_ | . | . |
| 10/23 | Nearest Neighbors | . | Homework #4 |
| 10/28 | Dimensionality Reduction (1) | . | . |
| 10/30 | Dimensionality Reduction (2) | . | . |
| 11/04 | Convex Optimization | . | Homework #5 |
| 11/06 | _Project Elevator Pitch_ | . | . |
| 11/11 | Support Vector Machine | . | . |
| 11/13 | Neural Networks | . | . |
| 11/18 | Deep Learning (1) | . | . |
| 11/20 | Deep Learning (2) | . | . |
| 11/25 | Applications - DL-based Drug Discovery | . | . |
| 11/27 | Applications - Recommender System | . | . |
| 12/02 | _Presentations_ | . | . |
| 12/04 | _Presentations_ | . | . |
| 12/09 | _Presentations_ | . | . |

NOTE: Course materials with the `md` extension are [Markdown](https://en.wikipedia.org/wiki/Markdown) files.
To read the Markdown files, you can use various "free" Markdown viewer applications out there e.g:
- [Markdown Viewer Chrome Add-on](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en)
- [Slide-style View using Remark](https://github.com/gnab/remark)
- [Slide-style View using Remark (web service)](https://remarkjs.com/remarkise)


## Grading

- Homeworks: 35%
- Midterm: 15%
- Project: 40%
- Participation: 10%

## Project

The goal of the final project is to: 
1. identify and formulate a machine learning problem, 
1. come up with appropriate solutions, 
1. implement the solutions, 
1. analyze the results and limitations, and 
1. suggest any algorithmic/engineering improvements.

You are free to find any datasets and problems of your research interest.

You are encouraged to work in groups of 2-3 people for the project.
Teams are required to hand in a project proposal, a final report, and presentation slides of their work.

Note that the final project contributes to 40% of your final grade. 
The final report should include a section that details each member's contribution to the project. 

_Grading for the Final Project:_
- Proposal (due TBD): 15%
- Elevator Pitch (due TBD): 10%
  - Elevator pitch needs to address 1) why the problem is important or interesting, 2) what are existing solutions, and 3) how you plan to solve the problem differently
  - Teams are required to present this in **2 minutes** - that's why it's called elevator pitch.
- Presentation (due TBD): 25%
- Report (due TBD): 50%


## Policy

- Assignments
  - Homeworks are due electronically on Canvas at 11:59 pm ET.
  - Late submissions are accepted with the following scoring rule:
      - `Score = 0.7^{number_of_late_days} x original_score` 
      - The number of late days counts from 1 right after the deadline.
      - Note that `0.7^14=0.00678`. This means homework submitted after 2 weeks will get zero points regardless of their original scores.
  - No partial submission is allowed. You either submit the full homework on-time or not.
  - The latest submission will count as the submission.
    - Even if your prior submissions have higher scores, the scores from the later submissions will overwrite.

- Midterm Exam
  - The midterm exam is open-book, open-notes, but no electronic devices.
  - The exam must be taken at the required time.
  - If you need to reschedule the midterm exam, you must request at least a week before the exam date to be considered.

## Honor Code

All classwork is governed by the College Honor Code, Emory Laney Graduate School, and Computer Science Departmental Policy. 
It is acceptable and encouraged to discuss homework with other students. 
However, this should be noted on your submitted homework and all code and writeup must be written by yourself. 
Any code and writeup that is found to be similar are grounds for an honor code investigation by the Director of Graduate Studies, Laney Graduate School, and the honor council. 




