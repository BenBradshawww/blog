+++
title = 'Martingale Theory'
date = 2024-11-01
categories = ["Probability"]
tags = ["Probability"]
keywords = ["Martingales", "Optional-Stopping Theorem"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](/images/sq-lim-aWm7fAUNPEc-unsplash.jpg)
[Image by sq lim](https://unsplash.com/@sql)

Today's article will look at one of the more difficult areas in probability called martingale theory. We will cover the basic theory and look at 2 examples which use martingale theory (the drunk man and the ABRACADABRA problem).



## The Theory

Before jumping into the problem, we have to cover some of the theory behind martingales. It is important to mention we will be skipping over many of the measure theory definitions and theorems. These will be covered at a later time. If you wish to read up more about this area of mathematics, I'd recommend reading the paper by T. Smith [here](https://math.uchicago.edu/~may/REU2012/REUPapers/Smith.pdf). This paper was the basis for this article [1].

To work with martingales, we will need to working within a filtered space.

****Definition.**** A filtered space is defined on,

$$(\Omega, \mathcal{F}, \mathcal{F}_n, \mathbb{P}),$$

where $\Omega$ is the sample space and consists of elements $\omega$ which are called sample points. $\mathbb{P}$ is called the probability measure where $\mathbb{P}(\Omega)=1$. $\{ \mathcal{F} : n \geq 0 \}$ is called a filtration. A filtration is an increasing family of sub-$\sigma$-algebras of $\mathcal{F}$ such that,

$$\mathcal{F}_0 \subseteq \mathcal{F}_1\subseteq \cdots \ \subseteq \mathcal{F}_n$$

and $\mathcal{F}_\infty$ is defined as

$$\mathcal{F}_{\infty} = \sigma (\cup_n \mathcal{F}_n ) \subseteq \mathcal{F},$$

where $\sigma$ is a $\sigma$-algebra on $\mathcal{F}$. A sigma algebra is a collection of events where the sample space itself is in $\mathcal{F}$, it is closed under complement, and it is closed under countable unions.

A filtration $\mathcal{F}_n$ can be thought of as all the information available up to time $n$. A random variable $X_n$ is $\mathcal{F}_n$ measurable if ${X_n \leq x} \in \mathcal{F}_n$, i.e. $\mathcal{F}_n$ contains all the previous information and the information at time $t$.

****Definition.**** A process $X = (X_{n} : n \geq 0)$ is adapted to the filtration $\mathcal{F}_n$ if for each $n, X_n$ is $\mathcal{F}_{n}$-measurable.

This means that any stochastic process $X_n(w)$ is known at time n and the stochastic process $X_n(w)$ is only dependent on the information we have up to and including time n and the process does not depend on any information in the future.

Now we can cover what is a martingale.

****Definition.**** A process $X$ is a martingale if:

1. $X$ is adapted,
2. $\mathbb{E}[|X_{n}|] < \infty, \forall n,$
3. $\mathbb{E}[X_{n} | \mathcal{F}_{n-1}] = X _{n-1}, \text{ almost surely } (n \geq 1).$

****Definition.**** A supermartingale is defined the same as a martingale but with (3) replaced by

$$\mathbb{E}[X_n | \mathcal{F}_{n-1}] \leq X _{n-1} $$

****Definition.**** A submartingale is defined the same as a martingale but with (3) replaced by

$$\mathbb{E}[X_n | \mathcal{F}_{n-1}] \geq X _{n-1} $$

****Definition.**** A stopping time $T:\omega \rightarrow 0, 1, 2, \cdots, \infty $ is called a stopping time if

$$\begin{align*}\{T \leq n\} &= \{w : T(w) \leq n \} \in \mathcal{F}_{n}, \forall n \leq \infty, \\ \text{or } \{T =n\} &= \{w : T(w) \leq n\} \in \mathcal{F}_{n}, \forall n \leq \infty . \end{align*}$$

This means, for a stopping time $T$, it is possible to tell whether $\{ T \leq n \}$ has occurred based on a filtration $\mathcal{F}_n$. In other words, the event $\{T \leq n\}$ is $\mathcal{F}_n$-measurable.

****Theorem.**** If X is a super martingale and $T$ is a stopping time, then the stopped process $X^{T} = (X_{T \wedge n}: n \in \mathbb{Z}^{+})$ is a supermartingale and

$$\mathbb{E}[X_{T \wedge n}] = \mathbb{E}[X_0], \forall n.$$

This does not imply that $\mathbb{E}[X_T] = \mathbb{E}[X_0]$.

The next theorem is the most important theorem for solving martingale based problems.

****Theorem (Doob's Optional-Stopping Theorem).**** a) Let $T$ be a stopping time and let $X$ be a supermatingale. Then $X_T$ is integrable and

$$\mathbb{E}[X_T] \leq \mathbb{E}[X_0]$$

in each of these 3 situations:

1. $T$ is bounded. (for some $N \in \mathcal{N}, T(w) \leq N, \forall w$),
2. $X$ is bounded (for some $K \in \mathbb{R}^{+}, |X_n(w)| \leq K \text{ for every } n \text{ and every } w$),
3. $\mathbb{E}[T] < \infty$ and for some $K \in \mathbb{R}^{+}, |X_n(w) - X_{n-1}(w)| \leq K, \forall (n,w)$.

b) If any of conditions 1-3 hold and $X$ is a martingale, then $$\mathbb{E}[X_T] = \mathbb{E}[X_0].$$

The results imply that the stopped process retains the expected outcome of that process.

****Definition.**** A process $C = (C_n : n \in N) $ is previsible if $C_n$ is $\mathcal{F}_{n-1}$ measurable for $n \geq 1$.

This means that the process's value at any time can be determined based on the information up to that time but not including that time. They help define strategies that depend only on the current and past information.

****Corollary.**** Suppose $M$ is a martingale, the increments $M_n - M_{n-1}$ are bounded by constant $K_1$, $C$ is a previsible process bounded by constant $K_2$ and $T$ is a stopping time such that $\mathbb{E}[T] < \infty$. Then

$$\mathbb{E}[\sum_{1\leq k \leq T} C_k(M_k - M_{k-1})] = \mathbb{E}[C . M]_T = 0.$$

This means that assuming you have no knowledge of future events, you cannot beat a fair game.

****Lemma.**** If $T$ is a stopping time where for some $N \in \mathbb{N}$ and some $\epsilon > 0$, we have, for every $n \in \mathcal{N}$:

$$\mathbb{P}[T < n + N | \mathcal{F}_n) > \epsilon, \text{almost surely}.$$

Then $\mathbb{E}[T] < \infty$.

## The Drunk Man

A man had too much to drink and is standing on a bridge that is 100 meters long. He is currently at the $17_{\text{th}}$ meter but has a tendency to either move forward or backward one meter with a $50 \%$ chance for each step he takes. What are the chances that he reaches the end of the bridge (the $100_{\text{th}}$ meter) before he returns to the beginning (the $0_{th}$ meter)? How many steps is he expected to take to reach either end of the bridge?

To solve this problem, martingale theory can be used. Assume the man starts at the point 0 and stops either at -17 or 83.

Let $X_i$ denote the random variable modelling the direction of the step at time $i$ and let $S_n$ denote the sum of the random variables $X_i$ for $i \in \{1, 2, \cdots, n\}$. Specifically, $S_n$ is the position of the man at step $n$.

We can prove that the random variable $S_n$ and $S_n^{2} -n$ are martingales.

1. $S_n$ is adapted because it is a sum of random variables $X_i$ for $i \in \{1, 2, \cdots, n\}$.
2. The process $S_n$ is bounded by -17 and 83, i.e. $\mathbb{E}[|S_n|] \leq \mathbb{E}[|S_T|] \leq \max(17, 83) = 83 < \infty$, where $T$ denotes the time that the sum of the steps $S_n$ hits -17 or 83.
3. Finally, $\mathbb{E}[S_{n+1} | \mathcal{F}_n] = \mathbb{E}[S_{n} + X_{n+1} | \mathcal{F}_n] = \mathbb{E}[S_{n}| \mathcal{F}_n] + \mathbb{E}[ X_{n+1} | \mathcal{F}_n] = S_n + \mathbb{E}[X_{n+1}] = S_n + (-1.(1/2) + 1. (1/2)) = S_n$.

Now for $S_n^{2} -n$.

1. $S_n^{2} -n$ is adapted as it is the squared sum of random variables $X_i$ for $i \in \{1, 2, \cdots, n\}$.
2. For any time step n i.e. $\mathbb{E}[|S_n^{2} - n|] \leq \mathbb{E}[S_n^{2}] + n \leq 83^{2} + n < \infty$. Consequently, $\mathbb{E}[|S_{n}^{2} - n|] < \infty, \forall n$.
3. Finally, $\mathbb{E}[S_{n+1}^{2} - (n+1) | \mathcal{F}_n] = \mathbb{E}[(S_{n} + X_{n+1})^{2} | \mathcal{F}_n] - (n+1) = \mathbb{E}[S_{n}^{2}| \mathcal{F}_n] + 2 \mathbb{E}[ S_{n}X_{n+1} | \mathcal{F}_n] +\mathbb{E}[X_{n+1}^{2} | \mathcal{F}_n] - (n+1) = S_n^2 + 2S_n\mathbb{E}[X_{n+1}] + \mathbb{E}[X_{n+1}^{2}] - (n+1)= S_n^2 + 2 S_n . 0 + 1 - (n+1)= S_n^2 - n$. c

Each of these two martingales will be used to solve the first and second problem in this question.

Now that we know both random variables are martingales we can now apply Doob's Optional-Stopping Theorem. To do this, we'll need to satisfy one of its 3 conditions. For the first martingale, we can satisfying condition 2, by seeing that the martingale is bounded by 83.

Applying Doob's Optional-Stopping Theorem for the second martingale is a bit more tricky. We will choose to prove condition 3 is satisfied. For any time K, if the man is at position $x$ on the bridge between -17 and 83, there exists a probability greater than zero that in the next $83-x$ or $-17-x$ steps the man will hit either -17 or 83. Consequently, $\mathbb{E}[T] < \infty$.

For the second condition,

$$\begin{align*}|M_n - M_{n-1}| &= |(S_n^2 - n) - (S_{n-1}^2 - (n-1))| \\ &= |S_n^2 –S_{n-1}^2 + 1| \\ &\leq |S_n^2| + |S_{n-1}^2| + 1 \\ &\leq 2 . 83^2 + 1 \\ &< \infty\end{align*}$$

Suppose at time step $T$ the drunk man has reached -17 or 83. To determine the probability he has reached 17 or 83 we will use the first martingale and Doob's Optional-Stopping Theorem.

$$\mathbb{E}[S_T] = -17.(1-p) + 83.p = S_0 = 0$$

Solving this equation gives $p=17/100$.

To find the expected number of steps we'll use the second martingale and Doob's Optional-Stopping Theorem again.

$$\mathbb{E}[S_T - T] = (-17)^{2}.(1-p) + 83^{2}.p - \mathbb{E}[T] = S_0^{2} - 0 = 0.$$

This gives $\mathbb{E}[T] = 1411$.

In general, for any two points $\alpha$ and $-\beta$, $p_\alpha = \frac{\alpha}{\alpha + \beta}$ and $\mathbb{E}[N] = \alpha \beta$.

## The ABRACADABRA Problem

A monkey types letters at random, one per each unit of time, producing an infinite sequence of identically independent random letters. If the monkey is equally likely to type any of the 26 letters, how long on average will it take him to produce the sequence ABRACADABRA?

To solve this problem, we'll need to model these sequence of events as a gambling game. Suppose for each time $n = 1, 2, 3, \cdots$ a gambler arrives and makes a bet on which letter will be drawn. For the first bet, he bets £1 for the first letter A. If he wins, he will receive £26 but if he loses he gets £0 and must leave. In the situation he wins, the gambler will bet all his winnings (£26) on the next letter B. If he wins again he will receive £$26^{2}$ but if he loses he gets nothing and must leave. This process is repeated till we reach the sequence ABRACADABRA where the game will finish. We will choose $T$ to denote the time that a gambler has reached the sequence ABRACADABRA. This will correspond to the time taken for a monkey to produce the sequence ABRACADABRA.

Let $M_n^j$ denote the martingale of the payoffs after the n bets for jth gambler. To prove $M_n^j$ is a martingale we must show

1. $M_n^j$ is adapted. The payoff for the gambler at time $n$ is solely dependent of the letters drawn at and before time $n$ so the process must be adapted.
2. $\mathbb{E}[|M_n^j|] < \infty, \forall n$. Well, $\mathbb{E}[|M_n^j|] = \mathbb{E}[M_n^j] \leq 26^n \leq \infty$. Consequently, this condition must be satisfied.
3. $\mathbb{E}[M_n^j | F_{n-1}] = M_{n-1}^j$. For this there are two situations. First, the 4th gambler loses before time $n$. Then $\mathbb{E}[M_n^j | F_{n-1}] = M_{n-1}^j$.

Now that $M_n^j$ is a martingale, we would like to use Doob's Optional-Stopping Theorem. However, applying Doob's Theorem to martingale $M_n^j$ will lead us to a dead end. In general, to solve this problem, we'll want to create a function which uses the random variable $T$ such that when we take the expectation, we will have a formula for $\mathbb{E}[T]$. To do this, we'll actually need to create a new martingale $X_n$ based on $M_n^j$.

$$X_n = \sum_{j=1}^n M_n^j.$$

This new random variable can be thought of as the payoff for the $n$ gamblers who have been betting up to time $n$. Using the property that the sum of a martingale is a martingale. We can now try to apply Doob's Optional-Stopping Theorem.

To do so, we need to satisfy one of its 3 conditions. Let's choose the third one where $\mathbb{E}[T] \leq \infty$ for some $K \in \mathbb{R}^{+}, |X_n(w) - X_{n-1}(w)| \leq K, \forall (n,w)$. From $K=11$, there exists the probability of the event occurring w.p. $(1/26)^{11}$ and in general, for any $K$ there exists a probability greater than 0 that the next 11 letters will form $ABRACADABRA$. Therefore the first condition is satisfied.

Next, we'll need to prove the second condition. Notice that,

$$|X_n - X_{n-1}| \leq 26^{11} + 26^4 + 26.$$

This works because $|X_n - X_{n-1}|$ can be thought of as the payoff at time $n$. The maximum payoff that could occur, occurs at time $T$ when the letters $ABRACADABRA$ is formed. When this happens for the jth gambler, we will also have the j+7th gambler winning $26^4$ and the j+11th gambler winning 26 because each unit of time introduces a new gambler and that gambler must always bet on $A$, then $B$, then $R$ etc.

Now that Doob's Optional Stopping Theorem is attained. We can use $\mathbb{E}[X_T] = \mathbb{E}[X_0]$. At time step $T$, the players have gained $26^{11} + 26^4 + 26$ but they have lost $T$ because $T$ players have bet £1. Consequently,

$$\mathbb{E}[X_T] = 26^{11} + 26^4 + 26 - \mathbb{E}[T] = 0.$$

So, $\mathbb{E}[T] = 26^{11} + 26^4 + 26$.

### Conclusion

This article briefly covered martingales and showed their application in solving two probabilistic problems.

### References:

1. Smith, T. (n.d.). __MARTINGALES AND A BASIC APPLICATION__. [online] Available at: https://math.uchicago.edu/~may/REU2012/REUPapers/Smith.pdf [Accessed 12 Oct. 2024].
