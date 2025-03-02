+++
title = 'Some Questions in Probability II'
date = 2025-01-07
categories = ["Probability"]
tags = ["Probability"]
keywords = ["Dice", "Probability", "Random Walks", "Expectation"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](/images/hannes-knutsson-2icXZAriT_E-unsplash.jpg)

[Image by Hannes Knutsson](https://unsplash.com/@hannesknutsson)

### Question:
On average, how many rolls would it take to get two of the same face when rolling a die.

For example, acceptable sequences with two of the same face include 2344, 1234566, and 123453. [1]

### Solution:

There are two ways you could approach this question, either using markov chains or permutations. Of these, we will focus on the latter, the easier of the two.

Let $X$ denote the number of rolls till we have found the same face twice. Our goal is to find $\mathbb{P}[X=x]$ for $x \in \{2, ..., 7\}$.

At $X=2$, the rolls must form a sequence of $AA$, where $A \in \{1, ..., 6\}$. Given two rolls, there are 6 sequences of this pattern out of the $6^2$ possible sequences. Hence,

$$\mathbb{P}[X=2] = \frac{6}{6^2} = \frac{1}{6}.$$
For $X=3$, the valid sequences take the form of ABA or BAA. As a result,

$$\mathbb{P}[X=3] = 2\cdot\frac{6\cdot5}{6^3} = \frac{5}{18}.$$
For $X=4$, the valid sequences take the form of ABCA, BACA, or BCAA. So,

$$\mathbb{P}[X=4] = 3\cdot\frac{6\cdot5\cdot4}{6^4} = \frac{5}{18}.$$

Iterating this process over the last terms and following the formula for the expectation of a discrete random variable.

$$\mathbb{E}[X] = \sum_{x=2}^7x\mathbb{P}[X=x] = \frac{1223}{324}.$$

### Question:

Suppose we were to roll a die 6k times. What is the probability that each face comes up an equal number of times (lets say k times). Find the asymptotic distribution for the probability in terms of k. [1]
### Solution:

In $6k$ rolls, we want $k$ of them to appear with the face "1". Consequently, there are

$$\binom{6k}{k}$$
ways this can occur. This can be thought of as given there are 6k positions and k of them are 1. How many different permutations are there.

Now given the $5k$ remaining spots, there are

$$\binom{5k}{k}$$
ways face "2" can appear. Continuing this process, leaves

$$\binom{6k}{k} \binom{5k}{k} \binom{4k}{k} \binom{3k}{k} \binom{2k}{k} \binom{k}{k}$$
rolls where there are an equal number of each face.

Since there are $6^{6k}$ total number of sequences. The final probability is:

$$\frac{\binom{6k}{k} \binom{5k}{k} \binom{4k}{k} \binom{3k}{k} \binom{2k}{k} \binom{k}{k}}{6^{6k}} = \frac{(6k)!}{(k!)^6 6^{6k}}$$


### Question:

What is the expected number of rolls to obtain a 6 given that the 6 comes before the 5.

### Solution:

First, we will find the probability that the first 6 comes before the first 5. Let $X$ denote the time of the first 6 given we have not found a 5 yet.

$$\begin{align}\mathbb{P}[X=1] &= \frac{1}{6} \\\mathbb{P}[X=2] &= \frac{1}{6} \frac{4}{6} \\ \mathbb{P}[X=3] &= \frac{1}{6} (\frac{4}{6})^2 \\ &\vdots \\ \mathbb{P}[X=k] &= \frac{1}{6} (\frac{4}{6})^{k-1}  \end{align}$$

Taking the sum of the terms gives:

$$\sum_{k=1}^\infty \mathbb{P}[X=k] = \frac{1}{2}$$

Using this, to find the probability the kth roll will be a 6 given we have not observed a 5 before this roll gives:

$$\begin{align}\mathbb{P}[6 \text{ on k-th roll} | 6 \text{ occurs before 5}] &= \frac{\mathbb{P}[6 \text{ on k-th roll and 6 occurs before 5}]}{\mathbb{P}[6 \text{ occurs before 5}]} \\&= \frac{\frac{1}{6} \cdot (\frac{4}{6})^{k-1}}{\frac{1}{2}}\end{align}$$
Substituting this into the discrete expectation formula:

$$\mathbb{E}[X] = \sum_{k=1}^\infty k \mathbb{P}[X=k].$$
Following this formula gives an expectation of 3.

### Question:

A building has 10 floors above the basement. If 12 people get into an elevator at the basement, and each chooses a floor at random to get out, independently of the others, at how many floors do you expect the elevator to make a stop to let out one or more of these 12 people? [3]

### Solution:

Let $\mathbb{1}_k$ be the indicator variable for whether the lift stops at floor $k$. An indicator variable has two values: 0 and 1. 0 for when no one gets off at floor k and 1 for when someone gets off at floor k.

Our goal is to find the sum $S$ of these 10 indicator variables:

$$\mathbb{E}[S] = \mathbb{E}[\sum_{k=1}^{10}\mathbb{1}_k].$$
Using the linearity of expectation, we rewrite the equation above to:

$$\sum_{k=1}^{10}\mathbb{E}[\mathbb{1}_k].$$
Since each indicator variable is identically distributed. This formula is simplified to:

$$10 \cdot \mathbb{E}[\mathbb{1}_k].$$
The expectation of an indicator variable can be written as:

$$\mathbb{E}[\mathbb{1}_k] = 1\cdot \mathbb{P}[\mathbb{1}_k=1]  + 0\cdot \mathbb{P}[\mathbb{1}_k=0] = \mathbb{P}[\mathbb{1}_k=1].$$
The probability of not observing anyone get off at floor $k$ is $(\frac{9}{10})^{12}$  and the probability of observing someone get off at floor $k$ is $1- (\frac{9}{10})^{12}$.  As a result:

$$\mathbb{E}[S] = 10 \cdot \mathbb{P}[\mathbb{1}_k=1] = 10 \cdot (1- (\frac{9}{10})^{12}) \approx 7.17.$$
So we are expected to stop at 7 of the 10 floors.

### Question:
You have two ropes. Each rope will take exactly 1 hour to burn all the way through. The densities of each rope vary throughout at unknown rates which cause some portions to burn fast and others to burn slow.

Using nothing but a lighter and the two ropes, how can you measure exactly 45 minutes?

### Solution:

Begin by igniting both ends of the first rope and one end of the second rope simultaneously. When the flames from both ends of the first rope meet in the middle, exactly 30 minutes will have elapsed. At this point, ignite the other end of the second rope. Since the second rope will now burn from both ends, it will take 15 minutes for the two flames to meet. Thus, the total elapsed time will be 45 minutes.

### Question:
Choose a person randomly on the street, 𝑋. Let 𝑁 denote the random variable representing the number of people that you select randomly from the street before you find someone who's taller than 𝑋. What is 𝐸[𝑁]? [5]

### Solution:

In short, the answer is infinity.

Let $f_X$ denote the PDF and $F_X$ denote the CDF of the the random variable $X$. Given the height of the first person is $x_0$, the probability someone is taller than $x_0$ is written as $1-F_X(x_0)$. Using this information, we can model the number of people needed till we get someone taller than $x_0$ as $N \sim \text{Geom}(1-F_X(x_0))$, a geometric distribution with parameter $1-F_X(x_0)$. As a result, $\mathbb{E}[N | X=x_0] = \frac{1}{1 - F_X(x_0)}$.

Using the formula for total expectation we get:

$$\mathbb{E}[N] = \mathbb{E} [ \mathbb{E}[N | X]] = \int_{-\infty}^{\infty}\frac{f_X(x)}{1 - F_X(x)}dx = -\ln(1 - F_X(x)) |_{-\infty}^{\infty} = \infty $$

Another nice way to see this is if we assume $X$ follows a uniform distribution over $(0, 1)$. Assuming $x_0$ is the height of the first person. The probability someone is taller is equivalent to $1-x_0$ and the number of people we would have to find till we found someone taller than $x_0$ follows a geometric distribution,  $N \sim \text{Geom}(1- x_0)$.

Using total expectation again gives:

$$\mathbb{E}[N] = \mathbb{E} [ \mathbb{E}[N | X]] = \int_{0}^{1}\frac{x}{1 - x}dx = -x -\ln(|x-1|) |_{0}^{1} = \infty $$

References:
1. Conroy, M. (2020). _A Collection of Dice Problems with solutions and useful appendices (a work continually in progress)_. [online] Available at: https://www.madandmoonly.com/doctormatt/mathematics/dice1.pdf.
2. Rolls, E. (2023). _Expected Rolls To Obtain a $6$ Given that $6$ Comes Before $5$_. [online] Mathematics Stack Exchange. Available at: https://math.stackexchange.com/questions/4806318/expected-rolls-to-obtain-a-6-given-that-6-comes-before-5 [Accessed 1 Jan. 2025].
3. Openquant.co. (2024). _Ten Floor Building - OpenQuant_. [online] Available at: https://openquant.co/questions/ten-floor-building [Accessed 5 Jan. 2025].
4. Openquant.co. (2024). _Burning Ropes - OpenQuant_. [online] Available at: https://openquant.co/questions/burning-ropes [Accessed 7 Jan. 2025].
5. riddle, I. (2021). _Interesting riddle about heights_. [online] Mathematics Stack Exchange. Available at: https://math.stackexchange.com/questions/4136049/interesting-riddle-about-heights [Accessed 7 Jan. 2025].

‌

‌

‌
