+++
title = 'Dynamic Programming in Solving Palindrome Partitioning'
date = 2024-08-24
categories = ["Algorithms"]
tags = ["Dynamic Programming", "Algorithms"]
keywords = ["Dynamic Programming", "Palindrome", "Algorithms"]
description = "SEO Description Here"
draft = false
[params.math]
  math = true
+++

![Image](/images/danny-greenberg-cbN8rxHr5S0-unsplash.jpg)
[Image by Danny Greenberg](https://unsplash.com/@by_danny_g?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)
### **Summary**

This article explores dynamic programming (DP), a technique used to tackle complex problems in computer science. We will specifically apply DP to two problems involving palindrome partitioning.

****Requirements****

A basic understanding of dynamic programming and some experience with DP problems are recommended before reading this article.

****Definitions****

• ****Palindrome****: A string is a palindrome if it reads the same backward as forward. For example, “aba” is a palindrome, while “aab” is not.

• ****Substring****: A substring is a contiguous sequence of characters within a string.

## Q1: Palindromic Substrings

Before delving into this question I'd recommend attempting it on Leetcode [here](https://leetcode.com/problems/palindromic-substrings/description/).

This question is as follows. Given a string `s`, return the number of palindromic substrings in it.

****Brute Force Approach****

At first glance, a brute force approach might seem viable. For a string like `abc`, you would check each of its 6 substrings (`a`, `b`, `c`, `ab`, `bc`, and `abc`) to see if they are palindromes. Given a string of length $n$, there are $\frac{n(n-1)}{2}$ possible substrings to check. Each palindrome check operation is $\mathcal{O}(n)$, leading to an overall complexity of $\mathcal{O}(n^3)$ for the brute force algorithm. While this approach works for small values of $n$, it becomes computationally expensive as $n$ grows larger.

To achieve a lower complexity, we can consider more efficient strategies. Dynamic programming is one such approach that can significantly reduce the time complexity. By storing intermediate results and avoiding redundant calculations, dynamic programming can optimise the process of checking palindromes and solving related problems.

****DP Approach****

Given that dynamic programming (DP) can be applied to this problem, let’s explore how it can be utilized effectively. To apply DP, we need to ensure the problem meets the two key requirements: optimal substructure and overlapping sub-problems.

****Overlapping Sub-Problems****

To illustrate overlapping sub-problems, consider a string like `aabc`. If we know whether a substring like `ab` is a palindrome, this information can help determine if `aabc` is a palindrome. Specifically, since `ab` is not a palindrome, `aabc` cannot be a palindrome either. This principle also extends to longer strings. For example, if `ab` is not a palindrome, then `aaabca` cannot be a palindrome. This shows that smaller sub-problems overlap and their solutions contribute to solving the larger problem.

In general, if the middle portion of a string is not a palindrome, the whole string cannot be a palindrome. Conversely, if the first and last characters of a string are the same, there is a possibility that the string could be a palindrome, provided the substring between them is also palindromic. If the first and last characters do not match, the string is definitely not a palindrome.

****Optimal Substructure****

Optimal substructure means that the solution to a problem can be constructed from the solutions to its sub-problems. For palindrome checking, the problem can be broken down by determining whether a substring is palindromic or not. The optimal solution to any of the subproblem is either a True or False boolean. Consequently, any solution to the subproblem is the optimal solution. 

Given the solution to this problem can be constructed using overlapping sub-problems and optimal substructure, DP can be used, more specifically we'll be implementing bottom-up DP. We'll illustrate this example by using the string `abaa` as the example problem for the rest of this section.

We'll create bottom-up DP table where each index in the array corresponds to a substring of the string `abaa`. Specifically, row index i and column index j corresponds to the substring from index i to j .

||0|1|2|3|
|---|---|---|---|---|
|0|||||
|1|||||
|2|||||
|3|||||

Let’s start by filling out the DP table for substrings of length 1. Since every single character is inherently a palindrome, the cells corresponding to substrings of length 1 will all be True.

||0|1|2|3|
|---|---|---|---|---|
|0|T||||
|1||T|||
|2|||T||
|3||||T|

For substrings of length 2, we check whether each pair of adjacent characters in the string are the same. A substring of length 2 is a palindrome if and only if both characters are identical.

||0|1|2|3|
|---|---|---|---|---|
|0|T|F|||
|1||T|F||
|2|||T|T|
|3||||T|

Now this is where the algorithm could get tricky to understand. Starting at string from index 0 to index 2 (`aba`). In this example, we first check that the first and last letter align. Next we would need to check if the substring between the first and last letter is a palindrome (substring `b`). Since we have computed smaller subproblems and stored their values within the grid we can check position row 1 and column 1. This is True. Hence (`aba`) is a palindrome.

Next we'll look at substring from index 1 to 3 (`baa`). Since the first and last letters do not align, we know this substring cannot be a palindrome. So we fill the corresponding grid position with False.

||0|1|2|3|
|---|---|---|---|---|
|0|T|F|T||
|1||T|F|F|
|2|||T|T|
|3||||T|

The final substring to check is from index 0 to 3 (`abaa`). Since the first and last letters align, we'll next check if the substring `ba` is a palindrome. To determine this we check the cell in the grid corresponding to row 1 and column 2 (substring `ba`). This gives a value of False, so we know `abaa` is not a palindrome.

||0|1|2|3|
|---|---|---|---|---|
|0|T|F|T|F|
|1||T|F|F|
|2|||T|T|
|3||||T|

Summing over the number of True values in the grid above tells us that there are 6 substring palindromes.

This application of DP may seem trivial however, we have now reduced the run-time complexity of the algorithm to $\mathcal{O}(n^{2})$. This is a consequence of storing the smaller subproblems which are used to solve the larger palindromes later on.

```python
def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = n

        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    ans += 1
        
        return ans
```

## Q2: Palindromic Partitioning II

Given a string `s`, partition `s` such that every  substring of the partition is a palindrome.Return the minimum cuts needed for a palindrome partitioning of `s`.

Similar to the question above, I'd recommend trying out this question beforehand [here](https://leetcode.com/problems/palindrome-partitioning-ii/description/).

There are 3 different approaches to solving this problem. First the brute force approach, second the DP approach, and finally the optimised DP approach.

****Brute Force Approach****

Given a string of length n, there are n-1 potential places to cut the string, which gives $2 ^{n}$ ways we could cut the string. Checking that each cut has produced palindromes is an $\mathcal{O}(n)$ operation. As a result, this method has a complexity of $\mathcal{O}(n 2 ^{n})$. For large n this method is computationally expensive.

****DP Approach****

Similar to the last question, we'll check to see if DP is appropriate here by checking for optimal substructure and overlapping sub-problems.

****Optimal Substructure****

The optimal substructure is somewhat harder to recognize. For a substring `abc` of string `abcd`, the optimal number of cuts for `abc` (2 cuts) can be used to determine the optimal number of cuts for `abcd` (3 cuts). However, this approach has a complication due to edge cases where palindromic strings contain non-palindromic substrings. For example, the substring `ab` of string `abba` is not palindromic, however its parent string is a palindrome. Therefor, the number of cuts for `ab` does not need to be used in string `abba`.

****Overlapping Subproblems****

The overlapping subproblems should be easy to spot. For example, if we have a non-palindromic string `abcd`, the number of cuts needed for the substring `abc` (2 cuts) could be used to help determine the number of cuts needed to cut string `abcd` (3 cuts). Similarly, the cuts from the substring `abc` can help determine the number of cuts needed for the substring `aabcd`. Consequently, there are overlapping subproblems.

To implement DP for this problem, we need to create two arrays. The first array will indicate whether substrings are palindromic or not, using the same method as in the first question. This array helps handle edge cases where the entire string is a palindrome but its substrings are not.

The second array is a 2D DP array that will determine the number of cuts needed for any substring. Similar to the previous question, each cell in this array corresponds to a substring starting at index x and ending at index y in the original string. The value in the cell represents the optimal number of cuts required for that substring.

To demonstrate this method, we will be trying to figure out the optimal number of cuts needed for string `abaa` such that each cut substring is palindromic.

||0|1|2|3|
|---|---|---|---|---|
|0|||||
|1|||||
|2|||||
|3|||||

Similar to the last question, we'll start with the substrings of length 1. Since every string of length 1 is palindromic, 0 cuts are needed.

||0|1|2|3|
|---|---|---|---|---|
|0|0||||
|1||0|||
|2|||0||
|3||||0|

Now we move onto the strings of length two starting from indexes 0 to 1 (substring `ab`). Checking the corresponding index positions in the first DP array tells us that this string is not a palindrome. So a cut is needed. Perform the same procedure for the two other substrings of length 2 gives:

||0|1|2|3|
|---|---|---|---|---|
|0|0|1|||
|1||0|1||
|2|||0|0|
|3||||0|

The final substring between indexes 2 and 3 (`aa`) required 0 cuts. This is because when we checked the corresponding indexes in our first DP array, it indicated that the substring was a palindrome, so no cuts were needed.

Next, we check substrings of length 3, starting from indexes 0 to 2 (`aba`). By referencing the first array, we see that this substring is also a palindrome, so 0 cuts are needed.

For the next substring (`baa`), we know it is not a palindrome. To determine the optimal cuts, we loop through the potential cut positions and evaluate which cut yields the best result. Let’s start with a cut between `b` and `aa`. Checking row 1 and column 1 in the DP array, we find that the substring `b` requires 0 cuts to be a palindrome. Similarly, checking row 2 and column 3 shows that `aa` also requires 0 cuts. Therefore, making a cut here would result in 1 cut to make the entire substring a palindrome.

Next, we check the cut between `ba` and `a`. The corresponding indexes in the array show that `ba` requires 1 cut to become a palindrome, while `a` requires 0 cuts.

Consequently, the minimum number of cuts for the substring `baa` is 1, which occurs when we cut between `b` and `aa`. We fill the DP cell with this value, as it represents the fewest additional cuts needed.

||0|1|2|3|
|---|---|---|---|---|
|0|0|1|0||
|1||0|1|1|
|2|||0|0|
|3||||0|

For the final string we again check the first DP array to see if it's a palindrome. It is not, so now we have to go through the 3 cut positions to see which produces the fewest remaining cuts.

The cut positions we'll check are `a` and `baa`, `ab` and `aa`, and `aba` and `a`. Checking the corresponding substring positions in the DP array tells us that substring `aba` and `a` require the fewest number of additional cuts (0 additional cuts). So we'll fill in the cell with 1 (for our first cut).

||0|1|2|3|
|---|---|---|---|---|
|0|0|1|0|1|
|1||0|1|1|
|2|||0|0|
|3||||0|

Checking the final value at row 0 column 3 gives us 1. So 1 cut is needed to make all substrings palindromic.

```python
def minCut(self, s: str) -> int:

    n = len(s)
    dp_pali = [[False]*n for _ in range(n)]

    for i in range(n):
        dp_pali[i][i] = True
        for j in range(i):
            if s[j] == s[i] and (i-j<=2 or dp_pali[j+1][i-1]):
                dp_pali[j][i] = True
    
    dp_cuts = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        dp_cuts[i][i] = 0

    for j in range(1, n):
        for i in range(j, -1, -1):
            if dp_pali[i][j]:
                dp_cuts[i][j] = 0   
            for k in range(0, j):
                dp_cuts[i][j] = min(1+dp_cuts[i][k]+dp_cuts[k+1][j], dp_cuts[i][j])


    return dp_cuts[0][-1]
```

This method works but under time complexity requirements, this method needs to be further optimised. This algorithm suffers from complexity $\mathcal{O}(n^{3})$ as a consequence of $\mathcal{O}(n^{2})$ substrings being checked, with each check being an $\mathcal{O}(n)$ operation.

I'd recommend watching the video by Tushar [here](https://www.youtube.com/watch?v=lDYIvtBVmgo&t=1s) to gain a deeper understanding of this question.

****Optimised DP Approach****

This optimised DP approach reduces the complexity of the previous DP approach to $\mathcal{O}(n^{2})$ by reducing the complexity of the partitioning cuts from $\mathcal{O}(n^{3})$ to $\mathcal{O}(n^{2})$.

Rather than checking every substring to determine the minimum number of cuts needed, only the $n$ substrings starting from index 0 will be checked. For example, for the string `abaa` we will only check string `a`, `ab`, `aba`, and `abaa` to determine the minimum number of cuts needed.

We'll create a 1 dimensional DP array, where index x corresponds to the minimum cuts needed to make a substring from index 0 to x a palindrome and we'll also be using our DP array from question 1 to determine whether the substring is a palindrome or not.

Iterate through the $n$ substrings from smallest to largest. If the substring is a palindrome (found using our first DP array) then we know 0 cuts are needed. So we'll set the corresponding column index to 0. If we are at index x and the substring from index 0 to x is not a palindrome then we iterate through the indexes from 0 to x checking to see if the substring from our new index to x is a palindrome. If so we know 0 cuts are needed to convert the subsequent string to a palindrome and we'll know the minimum cuts needed to make the previous substring a palindrome (since it was stored in our DP array in a previous iteration of this method).

This is best explained with an example. Let's use the final substring `abaa`. Since this is not a palindrome we'll iterate from 0 to x, checking to see if the subsequent substring is a palindrome. `baa` is not, so we go to the next index. `aa` is a palindrome. With this information we know that no more cuts are needed to make the subsequent substring (`aa`) a palindrome and we have stored the minimum cuts needed to make `ab` a palindrome from a previous iteration.

```python
def minCut(self, s: str) -> int:

    n = len(s)
    dp_pali = [[False]*n for _ in range(n)]

    for i in range(n):
        dp_pali[i][i] = True
        for j in range(i):
            if s[j] == s[i] and (i-j<=2 or dp_pali[j+1][i-1]):
                dp_pali[j][i] = True
    
    dp_cuts = [float('inf')]*n

    for i in range(n):
        if dp_pali[0][i]:
            dp_cuts[i] = 0
        else:
            for j in range(i):
                if dp_pali[j+1][i]:
                    dp_cuts[i] = min(dp_cuts[i], 1 + dp_cuts[j])


    return dp_cuts[-1]
```

  

### Conclusion

This article delved into 2 DP approaches used to solve problems related to palindrome partitions.