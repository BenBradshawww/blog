+++
title = 'Eulerian Numbers'
date = 2024-04-05
categories = ["Probability"]
tags = ["Probability"]
keywords = ["Probability"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](stephanie-leblanc-JLMEZxBcXCU-unsplash.jpg)
[Image by Stephanie LeBlanc](https://unsplash.com/@sleblanc01)

I was recently doing a few probability questions and then I stumbled upon this one:

## Question

A frog began its journey on the first stone in a sequence of seven stones, numbered 1 through 7 from left to right. With each move, the frog hopped to a stone it hadn't already landed on. What is the probability that after touching all the stones, the frog made precisely one jump to the left during its hops.

## Eulerian Numbers

I got really stuck on this question but its turns out the answer is simple. I needed to use something called a Eulerian number. [1]

In combinatorics, a Eulerian number $A(n, k)$ is the number of permutations of the numbers 1 to $n$ in which $k$ elements are greater than the previous element (permutations with k ascents).

Euclidean numbers come from Eulerian polynomials $A_n(t)$ where they are defined by the exponential generating function:

$$\sum_{n=0}^\infty A_n(t)\frac{x^n}{n!} = \frac{t-1}{t - e^{(t-1)x}} = (1 - \frac{e^{(t-1)x}-1}{t-1})^{-1}.$$

The Eulerian numbers are the coefficients of the Eulerian polynomial.

$$A_n(t) = \sum_{k=0}^n A(n, k)t^k,$$

where the formula for $A(n, k)$ follows :

$$A(n,k)= \sum_{i=0}^k (-1)^i \binom{n+1}{i}(k + 1 - i)^n.$$


For small values of $n$, this can be calculated manually, but for large values of $n$ a recursive formula could be used:

$$A(n,k) = (n-k)A(n-1, k-1) + (k-1)A(n-1,k).$$

## Properties
* For a fixed $n$, there exists a single permutation which has 0 ascents. $(n, n-1, n-2, ..., 1)$. For all $n$, $A(n, 0) = 0$. This formally includes the empty collection of numbers $n=0$. And so $A_0(t) = A_1(t) = 1$.
* For $k=1$ the formula implies $A(n,1) = 2^n - (n+1)$ with a sequence of $n$ following 0,0,1,4,11,26,57,....
* Fully reversing a permutation of $k$ ascent gives another permutation of $n-k-1$ ascents. As such, $A(n,k) = A(n,n-k-1)$.
* A lavish upper bound is $A(n,k) \leq (k+1)^n \cdot (n+2)^k$.
* For $k \geq n > 0$ the values are 0.

The tabulation of Eulerian numbers are found in a triangular array called Euler's triangle and shares some of the properties of Pascal's Triangle.

## Identities

There is one important identity of the Eulerian number. This states that the partitioning of a finite set into smaller finitely many smaller sets, the sum of the cardinalities of the smaller set is equal to the cardinality of the bigger set. Since the Eulerian numbers partition the permutations of $n$ elements, their sum is also equal to the factorial $n!$.

$$\sum_{k=0}^{n-1} A(n,k) = n!, \quad \text{for } n>0.$$

As well $A(0,0) = 0!$

## Solution

Now equipped with this information we can reattempt the question. Given the frog starts at stone 1, there are 6 possible stones to jump on. This gives us $6! = 720$ combination of jumps.

If there is only 1 leftward jump (1 descent), then there must be 4 ascents. As such, we need to calculate the Eulerian number for $n=6$ and $k=4$. Using the property that $A(n,n-k-1)= A(n,k)$. We know that $A(6, 4) = A(6, 1)$.

Using:

$$A(n,k)= \sum_{i=0}^k (-1)^i \binom{n+1}{i}(k + 1 - i)^n,$$

gives:

$$A(6,1) = \sum_{i=0}^1 (-1)^i \binom{7}{i}(2 - i)^6 = 2^6 - 7 = 57. $$

This gives a final probability of

$$\frac{57}{720}.$$


## References:
1. Wikipedia Contributors (2025). _Eulerian number_. Wikipedia.

‌
