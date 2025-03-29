+++
title = "Gambler's Ruin for a Symmetric Random Walk"
date = 2024-08-24
categories = ["Algorithms"]
tags = ["Probability", "Random Walk"]
keywords = ["Probability", "Symmetry", "Random Walk"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image by Jacob Owens: https://unsplash.com/@jakobowens1](/images/jakob-owens-EroR0Ah9hqI-unsplash.jpg)

A gambler starts with i dollars and bets $1 on a fair coin toss, winning $1 on heads and losing $1 on tails. The game stops when the gambler reaches 0 or N dollars.

• Derive the probability $p_i$ that the gambler reaches N dollars (i.e. “wins”) before going broke.

We'll cover 3 ways to approach this questions.

## Solution 1

Let $p_i$ denote the probability of reaching N dollars given he currently has i dollars.

Using the law of total probability [1], we can write:

$$p_i = \frac{1}{2} p_{i+1} + \frac{1}{2}p_{i-1}.$$
Similarly,

$$p_{i-1} = \frac{1}{2} p_{i} + \frac{1}{2}p_{i-2}.$$

We also have the boundary conditions where $p_0 = 0$ and $p_{20} = 1$.

Using these two boundary conditions and the formula above. We may iteratively create a formula for $p_i$ from $p_{i-1}$ and a formula for $p_i$ from $p_{i+1}$.

$$\begin{aligned}p_1 &= \frac{1}{2} p_0 + \frac{1}{2} p_2 =  \frac{1}{2} p_2 \\ p_2 &= \frac{1}{2} p_1 + \frac{1}{2} p_3 =  \frac{1}{2} (\frac{1}{2} p_2)  + \frac{1}{2} p_3 = \frac{2}{3} p_3 \\ p_3 &= \frac{1}{2} p_2 + \frac{1}{2} p_4 =  \frac{1}{2} (\frac{2}{3} p_3)  + \frac{1}{2} p_4 = \frac{3}{4} p_4 \\ &\vdots  \end{aligned}$$

Similarly,

$$\begin{aligned}p_{19} &= \frac{1}{2} p_{18} + \frac{1}{2} p_{20} +  =  \frac{1}{2} + \frac{1}{2} p_{18} \\ p_{18} &= \frac{1}{2} p_{17} + \frac{1}{2} p_{19} =  \frac{1}{2} p_{17}  + \frac{1}{2}(\frac{1}{2} +\frac{1}{2} p_{18}) = \frac{1}{3}  + \frac{2}{3}p_{17} \\ p_{17} &= \frac{1}{2} p_{16} + \frac{1}{2} p_{18} =  \frac{1}{2}p_{16}  + \frac{1}{2} (\frac{1}{3}  + \frac{2}{3}p_{17}) = \frac{1}{4} +  \frac{3}{4} p_{16} \\ &\vdots  \end{aligned}$$


By observing the pattern from the two iterations above, we can use substitute these formula into:

$$p_{10} = \frac{1}{2} p_{9} + \frac{1}{2} p_{11} = \frac{1}{2} (\frac{9}{10}p_{10}) + \frac{1}{2}(\frac{1}{10} +  \frac{9}{10} p_{10}) = \frac{1}{2}$$

Consequently, the probability of reaching 20 dollars before going broke is $\frac{1}{2}$.


## Solution 2

This solution is similar to the method above, but without the use of iteration. Starting from:

$$p_i = \frac{1}{2} p_{i+1} + \frac{1}{2}p_{i-1}.$$

We can rearrange this formula to get:

$$p_{i+1} - p_i = p_i - p_{i-1}.$$

This tells us that the difference between successive values of $p_i$ is the same at every step. Specifically, the step size does not depend on i. This is the defining property of a linear function. As a result, we know the general formula for this equation takes the form of:

$$p_i = Ai+B.$$

To determine the constants, we solve the formula at the boundary conditions.

At $i=0, p_0 = 0$.

$$0 = p_0 = A .0 + B \Rightarrow B = 0.$$

And at $i=20, p_{20} = 1$.

$$1 = p_0 = A .20 \Rightarrow A = \frac{1}{20}. $$

At $i=10$:

$$p_{10} = \frac{1}{20} 10 = \frac{1}{2}.$$

## Solution 3

The final solution uses Martingale Theory. Let $X_i$ be the random variable denoting the amount of wealth at time $i$.

Our goal is to use the Doob's Optional Stopping Theorem.

****Theorem (Doob's Optional-Stopping Theorem).**** a) Let $T$ be a stopping time and let $X$ be a supermatingale. Then $X_T$ is integrable and

$$\mathbb{E}[X_T] \leq \mathbb{E}[X_0]$$

in each of these 3 situations:

1. $T$ is bounded. (for some $N \in \mathcal{N}, T(w) \leq N, \forall w$),
2. $X$ is bounded (for some $K \in \mathbb{R}^{+}, |X_n(w)| \leq K \text{ for every } n \text{ and every } w$),
3. $\mathbb{E}[T] < \infty$ and for some $K \in \mathbb{R}^{+}, |X_n(w) - X_{n-1}(w)| \leq K, \forall (n,w)$.

b) If any of conditions 1-3 hold and $X$ is a martingale, then $$\mathbb{E}[X_T] = \mathbb{E}[X_0].$$
As a result, to use Doob's Optional Stopping theorem we need to show that $X$ is a random variable. A process $X$ is a martingale if:
1. $X$ is adapted,
2. $\mathbb{E}[|X_{n}|] < \infty, \forall n,$
3. $\mathbb{E}[X_{n} | \mathcal{F}_{n-1}] = X _{n-1}, \text{ almost surely } (n \geq 1).$

We'll show how $X$ satisfies each of these conditions below:
1. The random variable $X_i$ is a function of random Bernoulli variables up to time $i$. So it must be adapted.
2. The process is bounded below by 0 and above by 20 such that $\mathbb{E}[|X_i|] \leq 20 < \infty$.
3. Finally, let $B_i$ denote a Bernoulli Random variable for the toss as time $i$.

$$\begin{aligned} \mathbb{E}[X_i | \mathcal{F}_{n-1}] &= \mathbb{E}[X_{i-1} + B_{i}| \mathcal{F}_{n-1}] \\ &= \mathbb{E}[X_{i-1} ] + \mathbb{E}[ B_{i}| \mathcal{F}_{n-1}] \\ &= \mathbb{E}[X_{i-1} ]+ \mathbb{E}[ B_{i}] \\ &= \mathbb{E}[X_{i-1} ] + \frac{1}{2}. -1 + \frac{1}{2}.1 \\ &= \mathbb{E}[X_{i-1} ].\end{aligned}$$

To use Doob's Optional Stopping Theorem, we must satisfy 1 of the 3 conditions. We'll choose to show $X$ is bounded. Since the game stops, when $X$ is 20 or 0. The condition must be bounded by 20. As a result, we can say that $\mathbb{E}[X_T] = \mathbb{E}[X_0]$.


$$10 = \mathbb{E}[X_0] = \mathbb{E}[X_T] = 20p + 0.(1-p) = 20p \Rightarrow p = \frac{1}{2}.$$
