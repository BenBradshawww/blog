+++
title = 'Why Do Trees Outperform Neural Networks on Tabular Data?'
date = 2024-06-27
categories = ["Machine Learning", "Trees"]
tags = ["Machine Learning", "Trees"]
keywords = ["Trees", "Machine Learning", "ML", "Random Forests", "Random Forest"]
description = "SEO Description Here"
draft = false
[params.math]
math = true
+++

![Image](/images/photo-1458966480358-a0ac42de0a7a.avif)
[Image by Todd Quackenbush](https://unsplash.com/@toddquackenbush?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)

For the past 30 years, tree-based algorithms such as Adaboost and Random Forests have been the go-to methods for solving tabular data problems. While neural networks (NNs) have been used in this context, they have historically struggled to match the performance of tree-based methods. Despite recent advancements in NN capabilities and their success in tasks from computer vision, language translation, and image generation, tree-based algorithms still outperform neural networks when it comes to tabular data. This article will introduce several reasons behind the continued dominance of tree-based methods in this domain.

1. ****Smoothness of Neural Networks****:

Tabular data often has high dimensionality due to the large number of features each of different types. From these features, many of them have multidimensional relationships which can be complicated to model.

One issue with NNs is that they are inherently too smooth for most tabular data target functions (see definition at the end of the paper), which tend to be irregular in order to capture the complex tabular feature relations and structure. NNs are biased towards low-frequency functions, whereas tree-based algorithms, which are based on decision trees, use piecewise continuous functions. This gives trees an advantage in handling the irregularities common in tabular data and helps them model these complexities.

2. ****Handling Uninformative Features****:

Tree-based algorithms, being greedy, can effectively disregard uninformative features during the split process, using a splitting criteria such as entropy or the Gini index. In contrast, the neural networks initially assign weights to all features (including uninformative ones) by either giving each feature the same weight or assigning a random weight to the features. Even when there are small weights applied to these features, they can negatively impact the model’s performance. Consequently, it takes the NN model longer to learn which features are uninformative and then assign them a small weight which won't impact the model's performance.

3. ****Rotational Invariance of Neural Networks****:

In the paper by Grinsztajn on why trees outperform NNs on tabular data, Grinsztajn stated that Neural networks, particularly MultiLayer Perceptrons (MLPs), are naturally "rotationally invariant" and do not preserve the natural orientation of the data.

In this context, the MLP's rotational invariance corresponds to MLPs being unable to capture the natural orientation and relationships of the features. This must not be confused with the rotational invariance found in Geometric Neural Networks (GNNs) where if the features are rotated by applying a rotation matrix, the model's predictions will remain the same.

Similarly in this context, the natural orientation of the feature refers to the inherent structure and relationships between the features. The structure refers to the meaning of the feature, data types, data ranges, and feature distribution. The relationships refer to the interactions between features, correlations dependencies, and the hierarchical or sequential relationships.

The NNs initially treats each feature to be independent of one another. Additionally, the NNs do not have built-in mechanisms to preserve the natural relationships between features. For the NN to learn these structures and relationships between the features, more training and data is needed and a change in architecture may be required.

On the contrary, tree-based models and their ensembles inherently preserve natural orientation of features. Trees follow a greedy procedure which splits the data on the specific feature which achieves the highest splitting criteria. Each of these splits conserves the original meaning of the feature and its interactions. Consequently, these splits maintain the structure and relationships present in the data. For neural networks, these structures and relationships need to be learnt. This gives the tree-based models an inductive bias.

****Conclusion:****

Tree-based algorithms are easier and quicker to train compared to neural networks, making them a more practical choice for most tabular data problems. However, this does not mean that neural networks are entirely unsuitable for tabular data; with the right hyperparameters, NNs can potentially outperform tree-based models in specific scenarios.

****Reference****

This summary is based on the following paper, which provides a deeper understanding of the content covered here:

Grinsztajn, L., Oyallon, E. and Varoquaux, G. (n.d.). __Why do tree-based models still outperform deep learning on tabular data?__ [online] Available at: [https://arxiv.org/pdf/2207.08815](https://arxiv.org/pdf/2207.08815)

****Definitions:****

• ****Target Function****: The underlying function that maps inputs to outputs, representing the true relationship between features and labels. The goal in practice is to approximate this function as accurately as possible.





