# Regularization in Machine Learning

Regularization is a technique used in machine learning to prevent overfitting by adding a penalty to the loss function. This helps to ensure that the model generalizes well to unseen data.

## Why Regularization?

In many machine learning models, especially those with a large number of features, there is a risk of overfitting. Overfitting occurs when a model learns the noise in the training data instead of the underlying pattern. Regularization helps to mitigate this issue by constraining the model complexity.

## Types of Regularization

1. **L1 Regularization (Lasso)**:
   - Adds the absolute value of the coefficients as a penalty term to the loss function.
   - Can lead to sparse models where some feature weights are exactly zero.

2. **L2 Regularization (Ridge)**:
   - Adds the squared value of the coefficients as a penalty term to the loss function.
   - Helps to keep all feature weights small but does not lead to sparsity.

3. **Elastic Net**:
   - Combines both L1 and L2 regularization.
   - Useful when there are multiple features correlated with each other.

## Implementation

Here is a simple example of how to implement L2 regularization in Python using scikit-learn: