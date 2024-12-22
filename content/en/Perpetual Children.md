+++
title = 'Perpetual Children'
date = 2024-12-22
categories = ["Probability"]
tags = ["Probability"]
keywords = ["Probability", "Random Walks"]
description = "SEO Description Here"
draft = false
featuredImage =  "/images/vivek-kumar-riAKT8Z7ifE-unsplash.jpg"
[params.math]
  math = true
+++


![Image](/images/vivek-kumar-riAKT8Z7ifE-unsplash.jpg)
[Image by Vivek Kumar](https://unsplash.com/@vikceo)

**The Question**
A couple chooses to keep having children till they have an equal number of boys and girls. How many children will they have on average?

In this article we will cover 2 ways to solve this problem. First using a random walk and proof by contradiction. The second is Optiver's solution to this problem.

**Solution 1**
Let $X_t$ denote the random variable for which child has been born at time $t$.

Given the first child is already born at time 0. If the first child is a boy, then let $X_t$ take the value 1 if a boy is born at time t and let $X_t$ be -1 if a girl is born at time t. Similarly, if the first child is a girl, then  $X_t$ will take the value 1 if a girl is born at time t and we will take the value -1 if a girl has been born at time t.

Using the random variable $X_t$, we can model this question as a 1D random walk starting at the point 1. 
![Image](/images/random_walk_1d.png)

Without loss of generality, we will assume the first child to be born is a boy. If the next child born is a boy, we go up one, otherwise we go down one. 

$$X_t = \begin{cases} 1 \quad  &w.p. 1/2 \ \ (\text{if a boy}) \\ -1 \quad &w.p. 1/2 \ \ (\text{if a girl})\end{cases}$$

The random walk will finish once we hit 0 (i.e. when we have had equal number of boys and girls).

Now, let $W_x$ denote the number of walks starting from x to reach 0. More specifically, $W_x$ is the first time, given we have started at x, to hit 0.
$$\sum_{i=x}^{W_x} X_i = 0$$
Our goal is to determine $\mathbb{E}[W_1]$, i.e. the number of children needed to have an equal number of boys and girls, given that our first child is a boy.

Spoiler warning. The answer is infinite and to prove this we will use a proof by contradiction. Given we are at step 1, let us suppose that $\mathbb{E}[W_1]$ is finite. Following this assumption and the formula for expectation:
$$\begin{align*}\mathbb{E}[W_1] &= \mathbb{P}[X_1 = -1] \mathbb{E}[W_1 | X_1 = -1] + \mathbb{P}[X_1 = 1] \mathbb{E}[W_1 | X_1 = 1] \\ &=\frac{1}{2}(1 + \mathbb{E}[W_0]) + \frac{1}{2}(1 + \mathbb{E}[W_2]) \\ &= 1 + \frac{1}{2}\mathbb{E}[W_2]\end{align*}$$

Given you are at step 2, returning back to step 1 is equivalent to being at step 1 and returning to step 0, i.e., they are identically distributed.

$$\mathbb{E}[W_2] = \mathbb{E}[W_1] + \mathbb{E}[W_1]$$
By substitution, we get:
$$\begin{align*}\mathbb{E}[W_1] &= 1 + \frac{1}{2}(\mathbb{E}[W_1] + \mathbb{E}[W_1]) \\ &= 1 + \mathbb{E}[W_1]\end{align*}$$
This is a contradiction! As a result, the expected number of children to have before you hit 0 is infinite.

**Solution 2**

This is still under works for now!

Let