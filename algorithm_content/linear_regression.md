# Linear Regression

Linear Regression is a type of supervised learning algorithm in which the target variable is continuous in nature. It is one of the most widely used algorithms in machine learning. It is used to predict the continuous output variable based on one or more input features.

## Formula

The formula for simple linear regression is given by:

y = β0 + β1x + ε

where,

*   y is the target variable
*   x is the feature or input variable
*   β0 is the intercept or bias term
*   β1 is the coefficient of the feature
*   ε is the error term

## Image

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/1200px-Linear_regression.svg.png" alt="Linear Regression" width="500">


## Example

Suppose we have a dataset of exam scores and hours studied, and we want to predict the score of a student based on the number of hours studied. The data is given below:

| Hours Studied | Exam Score |
| --- | --- |
| 1 | 80 |
| 2 | 85 |
| 3 | 90 |
| 4 | 95 |
| 5 | 100 |

Using linear regression, we can fit a line that best predicts the exam score based on the hours studied. The equation of the line is given by:

Exam Score = 75 + 5 \* Hours Studied

This equation can be used to predict the exam score of a student based on the number of hours studied. For example, if a student studied for 5 hours, the predicted exam score is 100.


## Assumptions

*   The relationship between the independent variable and the dependent variable should be linear.
*   The independent variable should be continuous in nature.
*   The residuals should be normally distributed.
*   The residuals should have constant variance.
*   There should be no correlation between the residuals.
*   The independent variable should not be correlated with each other.



## Cost Function
The cost function, specifically the Mean Squared Error (MSE) in the context of linear regression, quantifies the difference between the actual output values (y) and the predicted output values (y') by the model. It measures the average of the squares of the errors, where the error is the difference between the actual and predicted values. The formula for MSE is:

MSE = (1/n) * Σ(yᵢ - y'ᵢ)²

where,

- yᵢ is the actual output value for the i-th data point.
- y'ᵢ is the predicted output value for the i-th data point.
- n is the total number of data points.

### Detailed Explanation


1. **Error Calculation**: For each data point, calculate the error, which is the difference between the actual value (yᵢ) and the predicted value (y'ᵢ).

2. **Squaring the Errors**: Each error is squared to ensure that negative and positive errors do not cancel each other out. Squaring also penalizes larger errors more than smaller ones, which emphasizes the importance of minimizing larger errors.

3. **Averaging the Squared Errors**: Sum up all the squared errors and divide by the number of data points (n) to get the average squared error. This average provides a single number representing the model's performance across all data points.

4. **Interpretation**: A smaller MSE value indicates a better fit of the model to the data, as it means the predicted values are closer to the actual values. Conversely, a larger MSE indicates a poorer fit.

The MSE is a crucial component in the training process of linear regression, as minimizing the MSE through optimization techniques like Ordinary Least Squares (OLS) leads to the determination of the most appropriate coefficients (β₀ and β₁) for the regression line.



## Optimization

The optimization algorithm used in linear regression is the Ordinary Least Squares (OLS). It is given by:

β = (X<sup>T</sup> * X)<sup>-1</sup> * X<sup>T</sup> * y

where,

*   X is the feature matrix
*   y is the target vector
*   β is the coefficient vector



## Advantages

*   It is easy to implement.
*   It is interpretable.
*   It is fast.
*   It does not require a lot of data.



## Disadvantages

*   It is sensitive to outliers.
*   It is not suitable for non-linear relationships.
*   It assumes that the residuals are normally distributed.
*   It assumes that the residuals have constant variance.



## Applications

*   Predicting continuous values.
*   Analyzing the relationship between variables.
*   Identifying the most important features.
