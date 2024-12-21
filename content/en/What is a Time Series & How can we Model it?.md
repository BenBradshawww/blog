+++
title = 'What is a Time Series & How can we Model it?'
date = 2024-10-05
categories = ["Time Series"]
tags = ["Statistics", "Time Series"]
keywords = ["Time Series"]
description = "SEO Description Here"
draft = false
[params.math]
  math = true
+++

![Image](images/oguzhan-kiran-wj0l2BJKmkU-unsplash.jpg)
[Image by Oğuzhan Kıran](https://mathstoml.ghost.io/ghost/#/editor/post/66eb4a6473445600016630bb)

This article will cover what is a time series, what does it mean for a time series to be stationary, and how could an autoregressive process or moving average process be used to model the time series.

Before starting this article, I would like to mention the Cambridge notes from [here](https://www.statslab.cam.ac.uk/~rrw1/timeseries/t.pdf) form the foundation of this content.

## What is a Time Series?

In short, time series is area of statistics which focuses on describing a set of data points which are collected on regular intervals by fitting low-dimensional models and making forecasts.

Any time series data can be broken down into 4 components:

1. Trend $(T_{t})$: The long term movements of the mean.
2. Seasonal effects $(I_{t})$: Calendar based fluctuations.
3. Cycles $(C_{t})$: Cyclical fluctuations.
4. Residuals $(E_{t})$: The random fluctuations.

Using these 4 components, any time series sample $X_{t}$ can be decomposed into these 4 components either additively or multiplicatively:

$$X_{t} = T_{t} + I_{t} + C_{t} + E_{t},$$

$$X_{t} = T_{t} \cdot I_{t} \cdot C_{t} \cdot E_{t}.$$

The distribution of a sequence of time series $(X_{t}, \dots, X_{t+k})$ can take many forms with some examples including:

- Normal Distribution: The samples could follow a normal distribution where most data is concentrated around the mean and has fewer points on the tail.
- Skewed Distribution: The time series exhibits skewness where the distribution is skewed to the left or right and so the data is not symmetric around the mean.
- Heavy-Tailed: Here the time series has a greater number of outliers.
- Discrete Distribution: In this example, the time series could only take discrete values.

Time series can be split into two categories depending on the properties of the time series: stationary or non-stationary. A stationary time series has a fixed mean, variance, and autocorrelation which helps us capture the time series's patterns and relationships allowing for more accurate forecasts. A non-stationary time series may have trends, seasonality, or changing volatility, making it harder to create forecasts.

## Stationary Time Series

Given a sequence of data points $\{ X_{t}, t \in \mathbb{Z} \}$, the sequence is ****strongly stationary**** or ****strictly stationary**** if

$$\left( X_{t_{1}}, \dots, X_{t_{k}}\right) \overset{d}{=} \left( X_{t_{1} + h}, \dots, X_{t_{k} + h}\right),$$

for all the time points $t_{1}, \dots, t_{k}$ and integer $h$. Note that when we use $X \overset{d}{=} Y$, this means the CDF of the two probability distributions $X$ and $Y$ are the same, formally, $\mathbb{P}(X \leq x) = \mathbb{P}(Y \leq x)$. This implies the mean, variance, and higher moments are the same.

A sequence is ****weakly stationary**** or ****second order stationary**** if

$$\begin{aligned} \mathbb{E}(X_{t}) &= \mu \\ \text{and} \quad \text{Cov}(X_{t}, X_{t+k}) &= \mathbb{E}[(X_{k} - \mu)(X_{t+k} - \mu)] = \gamma_{k}, \end{aligned}$$

where $\mu$ is constant and $\gamma_{k}$ is independent of $t$ and the sequence $\{ \gamma_{k}, k \in \mathbb{Z} \}$ is called the autocovariance function. At the lag 0, $\gamma_{0} = \mathbb{E}[(X_{k} - \mu)^{2}] = \text{Var}(X_{k})$.

Further define,

$$\begin{aligned}\rho_{k} = \gamma_{k} / \gamma_{0} &= \frac{\mathbb{E}[(X_{k} - \mu)(X_{t+k} - \mu)]}{\sqrt{\text{Var}(X_{t})\text{Var}(X_{t+k})}} \\ &= \frac{\mathbb{E}[(X_{k} - \mu)(X_{t+k} - \mu)]}{\text{Var}(X_{t})} \\ &= \text{Corr}(X_{t}, X_{t+k}),\end{aligned}$$

where $\rho_{k}$ is the autocorrelation at lag k and the plot of the autocorrelations $\{\rho_0, \dots, \rho_k \}$ is referred to as the autocorrelation function. The autocorrelation function helps identify patterns in the time series, such as periodicity (repeating cycles) or trends. If the autocorrelation decays slowly as the lag h increases, it suggests a trend or long-term dependence. If the autocorrelation exhibits periodic patterns, it indicates seasonality or cycles in the data.

In general, weak stationarity is a weaker condition than strong stationarity because the weakly stationary time series may have a fixed mean, variance, and autocorrelation, however the time series may not follow the same probability distribution and the weakly stationary time series moments (see the appendix) may vary overtime.

Properties of a stationary time series:

- A strictly stationary process is weakly stationary.
- If $X_{t}$ is truly random, then $\gamma_{0} = \text{Var}(X_{t}) > 0$.
- By symmetry $\text{Cov}(X_t, X_{t-k}) = \text{Cov}(X_{t-k}, X_t)$, so $\gamma_{k} = \gamma_{-k} \ \forall k$.

Now that we know the difference between the type of time series data, we can start to model it.

## Autoregressive Process

The first way to model any stationary time series is as an autoreggresive process where the current value of the series is expressed as a linear combination of its past values and a random error term (or white noise). Specifically, an autoregressive process of order $p$ is denoted as AR($p$) and can be written as:

$$X_{t} = \sum_{r=1}^{p} \phi_{r} X_{t-r} + \epsilon_{t},$$

where $\phi_{1}, \dots, \phi_{r}$ are fixed constants referred to as autoregressive coefficients which determine how much influence each lagged coefficient has on the current and $\{\epsilon_{t}\}$ is a sequence of independent random variables with mean 0 and variance $\sigma^{2}$, this random variable is often referred to as white noise.

To find the parameters of this model, we'll need to use the autocovariance function. For simplicity, we'll use the AR(1) process:

$$\begin{equation} X_{t} = \phi X_{t-1} + \epsilon_{t},\end{equation}$$

First by multiplying (1) by $X_{t-k}$ and taking the expected value gives:

$$\begin{aligned} \mathbb{E}[X_{t}X_{t-k}] &= \mathbb{E}[\phi X_{t-1}X_{t-k}] + \mathbb{E}[\epsilon_{t}X_{t-k}] \\\mathbb{E}[X_{t}X_{t-k}] &= \phi \mathbb{E}[X_{t-1}X_{t-k}] + \mathbb{E}[\epsilon_{t}] \cdot \mathbb{E}[X_{t-k}] \\ \gamma_k &= \phi \gamma_{k-1} + 0 \cdot \mathbb{E}[X_{t-k}] \\ \gamma_{k} &= \phi \gamma_{k-1}.\end{aligned}$$

Since the terms $\gamma_{k}$ can be solved using $\gamma_{k} = \frac{1}{N}\sum_{t=1}^{N-k}\mathbb{E}[(X_{t} - \bar{X})(X_{t+k} - \bar{X})]$, we now have a way to find the parameters $\phi$.

The final term to estimate is the white noise $\epsilon_{t}$. To find an equation for this term, we'll start by squaring (1) and then taking the expected value. This gives:

$$\begin{aligned} \mathbb{E}[X_{t}^{2}] &= \mathbb{E}[(\phi X_{t-1} + \epsilon_{t})^{2}] \\ \mathbb{E}[X_{t}^{2}] &= \phi_{1}^{2}\mathbb{E}[X_{t-1}^{2}] + 2 \phi_{1} \mathbb{E}[X_{t-1}\epsilon_{t}] + \mathbb{E}[\epsilon_{t}^{2}] \\ \gamma_{0} &= \phi_{1}^{2}\gamma_{0} + 0 + \sigma^{2}, \end{aligned}$$

so $ \gamma_{0} (1 - \phi_{1}^{2}) = \sigma^{2}$.

Now that we know how to find the parameters of an AR(1) model, we can define this for any AR process. Defining AR(p) as

$$\begin{equation}X_{t} = \phi_{1} X_{t-1} +\phi_{1} X_{t-1} \dots \phi_{p} X_{t-p} + \epsilon_{t}.\end{equation}$$

If we were to multiply (2) by $X_{t-k}$, take the expected value, and divide by $\gamma_{0}$ we will end up producing the Yule-Walker equations:

$$\rho_{t} = \phi_{1} \rho_{t-1} +\phi_{1} \rho_{t-1} \dots \phi_{p} \rho_{t-p}, \quad k=1, 2, \dots$$

This can be solved using the autocovariance matrix (a Toeplitz matrix):

$$\begin{pmatrix} \gamma_0 & \gamma_1 & \cdots & \gamma_{p-1} \\ \gamma_1 & \gamma_0 & \cdots & \gamma_{p-2} \\ \vdots & \vdots & \ddots & \vdots \\ \gamma_{p-1} & \gamma_{p-2} & \cdots & \gamma_0 \end{pmatrix} \begin{pmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_p \end{pmatrix} = \begin{pmatrix} \gamma_1 \\ \gamma_2 \\ \vdots \\ \gamma_p \end{pmatrix}$$

Now that the AR coefficients are estimated. The variance for the white noise $\sigma^{2}$ can be computed using:

$$\sigma^{2} = \gamma_0 - \sum_{i=1}^{p}\phi_i \gamma_i$$

## Moving Average Process

Given a centred time series, an alternative way to model this time series is by using a moving average process of order $q$ denoted by $MA(q)$ is defined as

$$X_{t} = \sum_{i=0}^{q} \theta_{i} \epsilon_{t-i},$$

where $\theta_{1}, \dots, \theta_{q}$ are fixed constants where $\theta_{0} = 1$ and $ \{\epsilon_{0},\dots ,\epsilon_{t} \}$ is an independent random variable with mean 0 and variance $\sigma^{2}$, we'll call this term the white noise term.

A moving average process uses the idea that time series data contains fluctuations which can be exploited to model the short-term variations in the time series.

Fitting the moving average model is no more complicated than fitting an autoregressive model. Given an MA(1) model:

$$\begin{equation} X_{t} = \theta_{1} \epsilon_{t-1} + \epsilon_{t}\end{equation}$$

First we'll create an equation for $\theta_1$ and $\sigma^{2}$ using $\gamma_0$ by multiplying (3) by $X_{t}$ and taking the expectation giving:

$$\gamma_{0} = \mathbb{E}[X_{t}^{2}] = \mathbb{E}[(\epsilon_t + \epsilon_{t-1}\theta_1)^{2} ] = \sigma^{2}(1 + \theta_{1}^{2})$$

The second equation will be formed by multiplying (3) by $X_{t-1}$ and taking the expectation:

$$\gamma_1 = \mathbb{E}[X_{t} X_{t-1}] = \mathbb{E}[(\epsilon_t + \epsilon_{t-1}\theta_1) (\epsilon_{t-1} + \epsilon_{t-2}\theta_1)] = \theta_1 \sigma^{2}.$$

Next using the autocorrelation at lag 1:

$$\rho_1 = \frac{\gamma_{1}}{\gamma_0} = \frac{\theta_1 \sigma^2}{\sigma^2(1 + \theta_1^2)} = \frac{\theta_1}{1 + \theta_1^2}.$$

For larger models, with more parameters, the combination of the Yule Walkers equations and the Toeplitz matrix will be the easiest way to find the model's parameters.

Moving average processes are particularly effective when a time series exhibits short-term dependencies, as they are designed to capture the immediate correlations between shocks. However, their primary limitation lies in this very reliance on short-term relationships, making them less suited to modelling long-term dependencies in the data.

## Conclusion

Today we covered what is a time series and how we could model a time series using basics processing techniques such as AR and MA. The next article will build on these methods introducing the ARMA models which combine both the AR and MA processes.

## Appendix

****Moments:**** Moments are quantitative measures of distribution used to describe its shape and characteristics.

****First Moment:**** The first moment (mean) is a measure to determine the central tendency of data. For a random variable from a continuous probability distribution, the first moment is written as:

$$\text{MEAN} = \mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) d x.$$

****Second Moment:**** The second moment measures the spread of the distribution. It is written as:

$$\text{VARIANCE} = \text{Var}[X] = \mathbb{E}[(X - \mathbb{E}[X])^{2}].$$

****Third Moment:**** The third moment measures the asymmetry of a distribution. It is written as:

$$\text{SKEWNESS} = \frac{\mathbb{E}[(X - \mathbb{E}[X])^{3}]}{\sigma^{3}}.$$

If the skewness if positive, than the distribution has a longer tail on the left and the bulk of the data is concentrated on the right. If the skewness is negative, then the distribution has a longer tail on the right and the bulk of the data is concentrated on the left. If the skewness is 0, the data is symmetric.

****Fourth Moment:**** The fourth moment measures the peakedness of a distribution and tells us how of the variance is a result of extreme outliers. It can be written as:

$$\text{KURTOSIS} = \frac{\mathbb{E}[(X - \mathbb{E}[X])^{4}]}{\sigma^{4}}.$$

Interpretation:

- High Kurtosis (Leptokurtic): The kurtosis is greater than 3, than the distribution has more extreme values (fatter tails).
- Low Kurtosis (Platykurtic): The kurtosis is less than 3, than the distribution has fewer extreme values (thinner tails).
- Normal Kurtosis (MesoKurtic): A kurtosis of 3 is the same as a normal distribution.

****Fixed Form Solution:**** A fixed-form solution (also known as a closed-form solution) refers to a solution to a problem that can be written down in a finite number of operations, without the need for iterative methods, approximation, or numerical optimization.

## References:

TIME SERIES Contents. (n.d.). Available at: https://www.statslab.cam.ac.uk/~rrw1/timeseries/t.pdf.

‌