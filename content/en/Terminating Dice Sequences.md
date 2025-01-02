+++
title = 'Terminating Dice Sequences'
date = 2025-01-02
categories = ["Probability"]
tags = ["Probability"]
keywords = ["Dice", "Probability", "Random Walks", "Optiver"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](/images/robin-noguier-sydwCr54rf0-unsplash.jpg)
[Image by Robin Nouguier](https://unsplash.com/@robinnoguier)
### Question
What is the expected number of dice that need to be rolled till the sum exceeds 6? [1]

### Solution
To do this, we'll start with the formula for expectation for discrete random variables:

$$\mathbb{E}[X] = \sum_{i=1}^6 \mathbb{P}[X = i]$$

There is a neat trick you can use where:

$$\begin{align}\mathbb{E}[X] &= 1 \cdot \mathbb{P}[X=1] + 2 \cdot \mathbb{P}[X=2] + 3 \cdot \mathbb{P}[X=3] + 4 \cdot \mathbb{P}[X=4]  + 5 \cdot \mathbb{P}[X=5] + 6 \cdot \mathbb{P}[X=6] \\ &=\mathbb{P}[X=1] \\ &+ \mathbb{P}[X=2] + \mathbb{P}[X=2] \\ &+ \mathbb{P}[X=3] + \mathbb{P}[X=3] + \mathbb{P}[X=3] \\ &+ \mathbb{P}[X=4] + \mathbb{P}[X=4] + \mathbb{P}[X=4] + \mathbb{P}[X=4] \\ &+ \mathbb{P}[X=5] + \mathbb{P}[X=5] + \mathbb{P}[X=5] + \mathbb{P}[X=5]+ \mathbb{P}[X=5] \\ &+ \mathbb{P}[X=6]+\mathbb{P}[X=6]+\mathbb{P}[X=6]+\mathbb{P}[X=6]+\mathbb{P}[X=6]+\mathbb{P}[X=6]. \\ &= \mathbb{P}[X>0]+\mathbb{P}[X>1]+\mathbb{P}[X>2]+\mathbb{P}[X>3]+\mathbb{P}[X>4]+\mathbb{P}[X>5]\end{align}$$
This gives a new formula for expectation written as:

$$\mathbb{E}[X] = \sum_{k=0}^5 \mathbb{P}[X>k]$$
So, our new goal is to calculate $\mathbb{P}[X>k]$ for $k \in \{0, ..., 5 \}$.

Denote the dice throw at step $i$ be denoted as $d_i$. When $k=3$, the first 3 dice throws must sum to less than or equal to 5. This is  equivalent to finding:

$$\mathbb{P}[d_1+d_2+d_3 \leq 5] = \mathbb{P}[d_1+d_2+d_3 = 3] + \mathbb{P}[d_1+d_2+d_3 = 4] + \mathbb{P}[d_1+d_2+d_3 = 5].$$

Using the stars and bars theorem which states for n items and k bins, there are $\binom{n+k-1}{k-1}$ ways to distribute the items. [2]

For $\mathbb{P}[d_1+d_2+d_3 = 5]$ we have 5 items and 3 bins but with the limitation that each bin must be of size greater than 1. Hence, there are $\binom{4}{2}$ ways to distribute the items.

Applying this for each of the 3 sub-equations gives:

$$\begin{align} \mathbb{P}[d_1+d_2+d_3 = 3] &= \frac{\binom{2}{2}}{6^3}, \\ \mathbb{P}[d_1+d_2+d_3 = 3] &= \frac{\binom{3}{2}}{6^3}, \\ \mathbb{P}[d_1+d_2+d_3 = 5] &= \frac{\binom{4}{2}}{6^3}.\end{align}$$
There's one final trick we can use from here called the Christmas Stocking Identity (also known as the Hockey Stick Identity) [3]. This states that:

$$\binom{r}{r} + \binom{r+1}{r} + ... + \binom{n}{r} = \binom{n+1}{r+1}.$$

Using this identity:

$$\mathbb{P}[d_1+d_2+d_3 \leq 5] = \frac{1}{6^3}\binom{5}{3}.$$


Returning to the discrete expectation formula:

$$\begin{align}\mathbb{E}[X] &= \sum_{k=0}^5 \mathbb{P}[X>k] \\ &= \sum_{k=0}^5 \frac{1}{6^k} \binom{5}{k} \\ &= (1 + \frac{1}{6})^5 \approx 2.16 \end{align}$$

### References:
1. Optiver (2024). _Prove it - Ep3: Terminating Dice Sums_. [online] YouTube. Available at: https://www.youtube.com/watch?v=YKE5SRXK_nI [Accessed 2 Jan. 2025].
2. Wikipedia. (2023). _Stars and bars (combinatorics)_. [online] Available at: https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics).
3. Wikipedia. (2023). _Hockey-stick identity_. [online] Available at: https://en.wikipedia.org/wiki/Hockey-stick_identity.

‌


‌
