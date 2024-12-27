+++
title = 'Kullback-Leibler Divergence'
date = 2024-09-10
categories = ["Statistics"]
tags = ["Machine Learning", "Statistics"]
keywords = ["Kullback-Leibler Divergence", "KL Divergence"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](/images/daniela-turcanu-wABdckxoj90-unsplash.jpg)
[Image by Daniela Turcanu](https://unsplash.com/@protopopica?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)
***
**Introduction**

This article will cover the key features of Kullback-Leibler Divergence (KL divergence), a formula invented in 1951 by the mathematicians Soloman Kullback and Richard Leibler. This formula is used in the background of many of the modern day machine learning models focused around probabilistic modelling. These including Variational Autoencoders (VAEs), Generative Models, Reinforcement Learning, and Natural Language Processing. Additionally, this article will cover some of KL divergence's key properties and briefly cover one of its applications.

**KL Divergence**

In essence, KL divergence gives us a way to tell how much one probability distribution varies from another. KL divergence quantifies this result as the amount of information lost when approximating one distribution from another.

In the discrete setting, for probability distributions $P$ and $Q$ defined over sample space $\mathcal{X}$, the formula takes the form:

$$D_{\text{KL}}(P || Q) = \sum_{x\in\mathcal{X}} P(x) \log \frac{P(x)}{Q(x)}.$$

This formula quantifies how close distribution $Q$ is to the approximating distribution $P$. More specifically, it measures the divergence of the distribution $Q$ from distribution $P$. This is interpreted as the amount of extra information required to encode samples from $P$ using distribution $Q$.

KL divergence for continuous probability distributions $P$ and $Q$ follow:

$$D_{\text{KL}}(P || Q) = \int_{-\infty}^{\infty} p(x) \log \frac{p(x)}{q(x)} dx,$$

where $p$ and $q$ refer to the probability densities of distribution $P$ and $Q$ respectively.

Before continuing, it is important to mention that in other texts, KL divergence is often referred to relative entropy. This must not be confused with Shannon entropy which measures the uncertainty in just one probability distribution.

**Key Properties of KL Divergence**

**Asymmetry**

The first key property of KL divergence is that this metric is asymmetrical,

$$D_{\text{KL}}(P || Q) \neq D_{\text{KL}}(Q || P).$$

This indicates that the divergence of distribution $P$ from $Q$ often gives a different result to the divergence of distribution $Q$ from $P$.

The lack of symmetry, along with the fact that the triangle inequality is not satisfied, are key reasons why this measure is not referred to as a distance. Instead, in information theory, it is classified as a type of divergence.

An alternative symmetric measure to quantify the difference between two probability distributions is Jeffery's Divergence. This divergence is defined as the sum of divergences between distributions $P$ and $Q$ in both directions.

$$J(P, Q) = \frac{1}{2} D_{\text{KL}}(P \parallel Q) + \frac{1}{2} D_{\text{KL}}(Q \parallel P)$$

Jeffery's measure provides a way to measure the total difference between two distributions.

On initial inspection, Jeffery's may seem more appropriate than KL divergence, however there's a few reasons why Kl divergence may be preferred. First KL divergence has a higher sensitivity to differences in distributions while Jefferys is a more smoothed version of KL divergence, which is less sensitive to these finer differences. The finer tuning ability is often preferred in practice.

Secondly, in situations where one distribution is a "target" or "true" distribution and the second is one is a distribution trying to approximate the first. KL divergence encapsulates this problem well, while Jeffery's does not. The reasons for this is because Jeffery's will incorporate information about the divergence of the true distribution from the approximating distribution. This is unwanted information, which hinders are inferences.

**Non-Negativity**

The second important property of KL divergence is that it is non-negative and equals zero iff (if and only if) the two distributions are identical almost everywhere. In this case, there is no divergence between the two distributions. Mathematically, this non-negativity property is written as $D_{\text{KL}}(P | Q) \geq 0$. This result is known as Gibbs’ inequality.

The term “almost everywhere” refers to the distributions being identical except on a subset of the domain with measure zero. This idea is analogous to the concept of “almost surely” in probability theory. Essentially, KL divergence is zero iff the two distributions are identical everywhere except on a small subset of measure zero.

**Convexity**

KL divergence is convex for any pair of probability measures $P$ and $Q$. For example, choose $(P_{1}, P_{2})$ and $(Q_{1}, Q_{2})$ to be two pairs of probability measures. Then the following property is satisfied.

$$D_{\text{KL}}(\lambda P_{1} + (1 - \lambda) P_{2} \| \lambda Q_{1} + (1-\lambda)Q_{2}) \leq \lambda D_{\text{KL}}(P_{1} \| Q_{1} ) + (1 - \lambda) D_{\text{KL}}(P_{2} \| Q_{2} ), \\ \text{ for } 0 \leq \lambda \leq 1.$$

**No upper bound exists**

Another important property of KL divergence is that, in general, it does not have an upper bound. However, an upper bound does exist in a specific case: when $P$ and $Q$ are discrete probability distributions over the same discrete set of outcomes. In this situation, a maximum value for $D_{\text{KL}}(P | Q)$ can be determined.

**Example:**

Given probability distributions $P$ and $Q$ with discrete outcomes from the sample space $\{0,1,2\}$. The distributions's outcome probabilities are in the table below.

|x|0|1|2|
|---|---|---|---|
|Distribution P(x)|1/2|1/3|1/6|
|Distribution Q(x)|1/3|1/3|1/3|

The KL divergence for $Q$ from $P$ and $P$ from $Q$ is written as:

$$\begin{aligned} D_{\text{KL}}(P\|Q) &= \sum_{x \in \mathcal{X}} P(x) \log \left( \frac{P(x)}{Q(x)} \right) \\ &= 1/2 \log(\frac{1/2}{1/3}) + 1/3 \log(\frac{1/3}{1/3}) + 1/6 \log(\frac{1/6}{1/3}) \\ &= 0.038 \\ D_{\text{KL}}(Q\|P) &= \sum_{x \in \mathcal{X}} Q(x) \log \left( \frac{Q(x)}{P(x)} \right) \\ &= 1/3 \log(\frac{1/3}{1/2}) + 1/3 \log(\frac{1/3}{1/3}) + 1/3 \log(\frac{1/3}{1/6}) \\ &= 0.042\end{aligned} $$

In many real-world scenarios, the distributions $P$ and $Q$ are derived from frequency distributions. As a result, there may be instances where one distribution contains events that have not been observed in the other. To account for these unobserved events, a smoothing method is applied. This method assigns a small probability to the events missing from both distributions, ensuring that all possible outcomes are represented.

|x|0|1|2|
|---|---|---|---|
|Distribution P(x)|1/2|1/2|0|
|Distribution Q(x)|0|2/3|1/3|

Here a small smoothing operator $\epsilon=10^{-3}$ smoothen $P$ and $Q$. This gives us the following table.

|x|0|1|2|
|---|---|---|---|
|Distribution P(x)|1/2 - ε/2|1/2 - ε/2|ε|
|Distribution Q(x)|ε|2/3 - ε/2|1/3 - ε/2|

Then the KL divergence of $P$ from $Q$ and $Q$ from $P$ can be calculated using the same formula as above.

**Applications of KL**

One application of KL divergence is in Variational Inference (VI), a method in Bayesian Machine Learning used to approximate complex posterior distributions. The process involves selecting a simpler family of distributions, $Q$, to approximate the true but intractable posterior distribution, $P$. This approximating distribution $Q$ is referred to as the variational distribution.

This approximation is crucial since directly finding the true posterior distribution is often infeasible. To estimate $P$, we first express the distribution in terms of the latent variable ($Z$) and the observed data ($X$), leading to the following equation:

$$ P(Z|X) = \frac{P(X|Z)P(Z)}{P(X)} = \frac{P(X|Z)P(Z)}{\int_{Z'}P(X|Z') dZ'}.$$

The challenge with this formula arises from the marginal term $P(X)$. Integrating over all possible values of $Z$ is often intractable, especially when $Z$ is a high-dimensional vector, as this makes the integration computationally expensive. To address this intractability, we introduce an approximating function $Q$, which serves as a simpler and more tractable version of the true posterior $P$.

The difference between the distributions $Q$ and $P$ is measured by a dissimilarity function, $d(Q, P)$. This function can take various forms, with KL divergence being one of the most commonly used.

As a result, the goal becomes minimizing the divergence between $Q$ and $P$. This optimization problem is typically framed as maximizing the Evidence Lower Bound (ELBO), which can be expressed as follows:

$$\begin{aligned} \text{ELBO} &= \mathbb{E}_{Q(Z, \phi)}\left[\log(P(X,Z)) - \log(Q(Z,\phi))\right]\\ &= D_{KL}(P\|Q(Z, \phi)) - \log(P(X)) \end{aligned} $$

where $\phi$ are the parameters of distribution $Q$, these are the parameters which need to be optimised to make distribution $Q(Z, \phi)$ approximate the true posterior. Since the term $\log(P(X)$ is constant, maximising the ELBO is equivalent to minimising the KL divergence.

****Conclusion****

In conclusion, KL divergence is a useful tool used in information theory, statistics, and even machine learning. This measure of divergence is a crucial for quantifying the difference between two probability distributions. Understanding KL divergence will undoubtedly enhance your ability to interpret probabilistic models and it will serve as a good stepping stone into many key ML models and algorithms used today.

****References:****

Wikipedia. (2024). __Kullback–Leibler divergence__. [online] Available at: https://en.wikipedia.org/wiki/Kullback_Leibler_divergence [Accessed 26 Jul. 2024].

Wikipedia. (2022). __Variational Bayesian methods__. [online] Available at: https://en.wikipedia.org/wiki/Variational_Bayesian_methods.

Shannon Entropy and Kullback-Leibler Divergence. (n.d.). Available at: https://www.stat.cmu.edu/~cshalizi/754/2006/notes/lecture-28.pdf [Accessed 23 Apr. 2019].

2.4.8 Kullback-Leibler Divergence. (n.d.). Available at: https://hanj.cs.illinois.edu/cs412/bk3/KL-divergence.pdf.

‌

‌
