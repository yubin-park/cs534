# CS534 - Machine Learning

This repository contains course materials for [CS 534 - Machine Learning](https://www.cs.emory.edu/courses/atlas/graduate/) provided in Fall 2020 at [Emory University](http://www.emory.edu/home/index.html).

Course syllabus, slides, and homework are largely borrowed/copied from Professor Joyce Ho's [CS534 class](https://joyceho.github.io/course/cs534_f18/).

## Overview

["Software is eating the world,"](https://a16z.com/2011/08/20/why-software-is-eating-the-world/)
 said Marc Andreessen in 2011. 
By then, he was referring to companies like Amazon, Netflix, Apple, and Google who are massively transforming the traditional industries with the power of the internet and software.
It was true in some sense, as apparent in [their enormous growth in market capitalization](https://www.investopedia.com/terms/f/faang-stocks.asp).

How did these companies become so successful?
There may be many reasons, one may say. 
Unfortunately, the answer to this question is beyond the scope of this course.
However, I find that one commonality of these companies remarkably stands out:
"their insatiable appetite for data".
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
  - 2:30 pm ET - 3:30 pm ET on Monday at Zoom (the link will be available on Slack)
  - 3:00 pm ET - 4:00 pm ET on Wednesday at Zoom (the link will be available on Slack)
- TA Office Hours
  - Han Xie (email: {firstname}.{lastname}@emory.edu)
    - Thursday 2:30 pm to 3:30 pm at Zoom (the link will be available on Slack)
- 100% Online Class
  - This course is offered 100% online using these tools:
    - [Canvas](https://canvas.emory.edu/courses/76953): Canvas will be used to track assignments, grades, and important announcements. 
    - [Zoom](https://emory.zoom.us/): Zoom will be used for the synchronous online lectures. Please check the Zoom link on the Canvas course page.
    - [Slack](https://slack.com/): Slack will be used as the main communication tool for the class e.g. questions regarding homework, lectures, etc. The instructor and TAs will try to respond to any Slack messages within 24 hours during weekdays, 48 hours during weekends.
  - Please show up in the scheduled Zoom sessions
    - This course intends to teach you how to think with machine learning, not the knowledge of machine learning.
    - Attendance is up to the individual student. Students should be responsible for keeping their course schedules and deadlines. 
  - Lastly, please be mindful of your personal safety, and avoid including personal information, such as phone numbers or addresses, in discussion forums. All online communications should be transmitted with the intent to inform, inspire, etc. - not to offend or breach personal privacy. Never use private information about other individuals and be sensitive to the information you share about yourself.
  
## Schedule

**WEEKLY OBJECTIVE:**
Most of the time, each lecture focuses on a different machine learning algorithm, starting from very foundational yet simple ones to more complex and sophisticated ones. 
Students will be able to understand 1) how such machine learning algorithms are motivated/developed, 2) when such models will be useful and avoided, and 3) how to implement and modify such models to deal with more custom settings.

**GUEST LECTURES:** We are excited to have a stellar array of guest lecturers:
- [Tian Su, PhD](https://www.linkedin.com/in/tian-su-81103538/), Director of Machine Learning at Walmart
- [Hyunjoon Jung, PhD](https://www.linkedin.com/in/hyunvincero/), Director of Personalization Data Science at Nike
- [Jenny Wang](https://www.linkedin.com/in/jenny-fengjuan-wang-a70b3810/), VP of Episode Development at Signify Health
- [Yen Sia Low, PhD](https://www.linkedin.com/in/yenlow/), ML Architect at Rally Health (Optum Digital)

| Date | Topic | Reference | Assignment |
| ---- | ----- | --------- | ---------- |
| 08/19 | [Introduction](prerequisite/slides.html) | . | [Homework #0](homework/hw0.md) |
| 08/24 | [Prerequisite - Statistics](prerequisite/slides.html#13) | . | . |
| 08/26 | [Linear Model - Regression (1)](linear_model/slides_reg.html)  | ESL Chapter 3 | [Homework #1](homework/hw1.md) |
| 08/31 | [Linear Model - Regression (2)](linear_model/slides_reg.html) | ESL Chapter 3 | . |
| 09/02 | [Linear Model - Classification](linear_model/slides_cls.html) | ESL Chapter 4 | . |
| 09/07 | [Linear Model - Other Distributions](linear_model/slides_cls.html) | ESL Chapter 4 and [GLMNET](https://web.stanford.edu/~hastie/glmnet/glmnet_beta.html) | . |
| 09/09 | [Evaluation Metrics](evaluation/slides.html) | ESL Chapter 7 | [Homework #2](homework/hw2.md) |
| 09/14 | [Evaluation Strategies](evaluation/slides.html) | ESL Chapter 7 | . |
| 09/16 | [Bias-Variance Tradeoff](bias_variance/slides.html) | Chapter 20-27 of [Machine Learning Yearning](https://www.deeplearning.ai/machine-learning-yearning/) (Optional) | . |
| 09/21 | [Decision Tree](decision_tree/slides.html) | . | [Homework #3](homework/hw3.md) |
| 09/23 | [Boosting](boosting/slides.html) | . | . |
| 09/28 | [Bagging](bagging/slides.html) | . | . |
| 09/30 | [Random Forests](random_forests/slides.html) | . | . |
| 10/05 | _Midterm Exam_ | . | . |
| 10/07 | [Nearest Neighbors](nearest_neighbors/slides.html) | Chapter 3 of [Mining of Massive Dataset](http://www.mmds.org/) (Optional) | . |
| 10/12 | [Dimensionality Reduction (1)](dim_reduction/slides.html) | . | [Homework #4](homework/hw4.md) |
| 10/14 | Dimensionality Reduction (2) | . | . |
| 10/19 | Convex Optimization | . | . |
| 10/21 | _Project Elevator Pitch_ | . | . |
| 10/26 | Support Vector Machine | . | . |
| 10/28 | Neural Networks | . | Homework #5 |
| 11/02 | Deep Learning (1) | . | . |
| 11/04 | Deep Learning (2) | . | . |
| 11/09 | Guest Lecture (TBD) | . | . |
| 11/11 | Guest Lecture (TBD) | . | . |
| 11/16 | _Presentations_ | . | . |
| 11/18 | _Presentations_ | . | . |
| 11/23 | _Presentations_ | . | . |

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
- Proposal (due 10/30): 15%
- Elevator Pitch (due 11/04): 10%
  - Elevator pitch needs to address 1) why the problem is important or interesting, 2) what are existing solutions, and 3) how you plan to solve the problem differently
  - Teams are required to present this in **2 minutes** - that's why it's called the elevator pitch.
- Presentation (due 11/27): 25%
- Report (due 12/13): 50%


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




