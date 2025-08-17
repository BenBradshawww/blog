+++
title = "Welch's T-test"
date = 2025-09-03
categories = ["Statistics", "Hypothesis Testing"]
tags = ["Statistics"]
keywords = ["Statistics", "Hypothesis Testing"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++


![Wexor Tmg](/images/turtle.jpg)
[Image by Wxor Tmg](https://unsplash.com/@wexor)

In hypothesis testing, there are a host of methods that could be used to perform your test. Today we'll look at Welch's T-test. This test excels in situations where two sample means vary significantly, specifically, if the samples have unequal variances or unequal sample sizes.

In general, this test should be used when:
* Comparing two independent groups.
* Unequal variances.
* Unequal sample sizes.

The Welch's _t_-test is designed for unequal population variances, a relaxation of the Student's t-test that assumes the two groups have equal variance. But similar to the Student's t-test, Welch's test shares the assumption that the data must follow a normal distribution.

The t-statistic for a Welch's t-test follows:

$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

Where:
* $\bar{X}_1$, $\bar{X}_2$: The sample means for each sample.
* $s_1^2, s_2^2$: The sample variances for each sample.
* $n_1, n_2$: The sample sizes for each sample.

The sample variances are given by the formula:

$$s^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \bar{X})^2$$
The proof of this formula can be found in the appendix[1].


The t-statistic is then compared against a t-distribution with degrees of freedom:

$$df = \frac{\left( \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \right)^2}{\frac{\left( \frac{s_1^2}{n_1} \right)^2}{n_1 - 1} + \frac{\left( \frac{s_2^2}{n_2} \right)^2}{n_2 - 1}}$$

This formula is known as the Welch-Satterthwaite approximation. It aims to answer the question: "if we were using a t-distribution to approximate the actual distribution of this test statistic (which involves estimated variances), what degrees of freedom would best match the shape?".

## Advantages & Disadvantages

Advantages:
* Welch's t-test is more robust than a Student's t-test. It maintains type 1 errors close to nominal for unequal variances and for unequal sample sizes under normality.
* The power of Welch's _t_-test comes close to that of Student's _t_-test, even when the population variances are equal and sample sizes are balanced.
* Welch's _t_-test can be generalised to more than 2-samples, which is more robust than one-way analysis of variance (ANOVA).
* Rather than testing the variances of the two distributions before deciding to go for a Student's t-test or Welch's t-test, it is recommend to directly apply Welch's test. This avoids the "double-dipping" bias — making your choice dependent on the data and then testing again on the sam data.
* Welch’s t-test remains robust for skewed distributions and large sample sizes. Thanks to the Central Limit Theorem, for larger samples, the sample mean becomes approximately normal, even when the data is skewed.

Limitation:
* Reliability decreases for skewed distributions and smaller samples, where one could possibly perform Welch’s t-test. In this situation, a non-parametric test would be prefered, such as the Mann-Whitney U test, that don't assume normality.

## Python

Below is an example on how you could perform a Hypothesis test in Python. The null hypothesis assumes the two groups have the same mean. The alternative hypothesis believes the mean of these two groups is different.

Suppose you are running the test with a significance level of 0.05. If we saw a $p$ value of less than 0.025 we could then assume there is sufficient evidence to reject the null hypothesis.

```python
from scipy.stats import ttest_ind, Normal

group1 = Normal(mu=5, sigma=1).sample(10)
group2 = Normal(mu=10, sigma=2).sample(15)

# Welch's t-test (equal_var=False)
t_stat, p_value = ttest_ind(group1, group2, equal_var=False)

print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")
```


## References

1. Wikipedia Contributors (2019). _Welch’s t-test_. [online] Wikipedia. Available at: https://en.wikipedia.org/wiki/Welch%27s_t-test.


## Appendix

**Sample Variance Proof**

The goal of this proof is to get $\mathbb{E}[s^2] = \sigma^2$.

Using the identity:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2$$

Where $\mu$ is the true mean of the distribution for $X$.

Taking the expectation of $s^2$  gives:

$$\mathbb{E}[s^2] = \frac{1}{n - 1} \mathbb{E}\left[\sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2\right]$$

Using the linearity of expectation, we get:

$$\mathbb{E}[S^2] = \frac{1}{n - 1} \left[ \sum_{i=1}^n \mathbb{E}[(X_i - \mu)^2] - n \mathbb{E}[(\bar{X} - \mu)^2] \right]$$

Since

$$
\begin{align*}\mathbb{E}[(X_i - \mu)^2] &= \sigma^2 \\
\mathbb{E}[(\bar{X} - \mu)^2] &=  \text{Var}[\bar{X}] = \frac{\sigma^2}{n} \end{align*}

$$

Substituting these into the formula above gives:

$$\mathbb{E}[s^2] = \frac{1}{n - 1} \left[n \sigma^2 - n \cdot \frac{\sigma^2}{n} \right] = \frac{1}{n - 1} \left(n \sigma^2 - \sigma^2 \right) = \frac{(n - 1)\sigma^2}{n - 1} = \sigma^2$$

Hence $s^2$ is an unbiased estimate of the true underlying variance $\sigma^2$.

