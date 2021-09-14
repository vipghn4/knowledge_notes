<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Regression](#regression)
  - [Introduction](#introduction)
  - [Regression model](#regression-model)
  - [Underlying assumptions](#underlying-assumptions)
  - [Interpolation and extrapolation](#interpolation-and-extrapolation)
  - [Power and sample size calculation](#power-and-sample-size-calculation)
<!-- /TOC -->

# Regression
## Introduction
**Regression analysis** is a set of statistical processes for estimating the relationships between a dependent variable (often called the *outcome variable*) and one or more independent variables (often called *predictors*, *covariates*, or *features*). The most common form of regression analysis is *linear regression*, which is to find the line that most fits the data according to a specific mathematical criterion.
* Example: given the basement area and total living area of a house, predict the price of that house
    * Predictors: the basement area and the total living area of the house
    * Outcome variable: the price of the house

For specific mathematical reasons, regression analysis allows us to estimate the **conditional expectation** (or population average value) of the dependent variable when the independent variables take on a given set of values.

**Usages of regression analysis**:
* Widely used for prediction and forecasting, where its use has substantial overlap with the field of *machine learning*
* Used to infer causal relationships between the independent and dependent variables

>**NOTE**: regressions, by themselves, only reveal relationships between **a dependent variable** and a collection of independent variables in a fixed dataset

>**NOTE**: to use regressions for prediction, or to infer causal relationships, one must carefully justify why existing relationships have predictive power for a new context, or why a relationship between two variables has a causal interpretation

## Regression model
**Regression model**: $Y_i = f(X_i, \beta) + e_i$
* Unknown parameters $\beta$
* Independent variables $X_i$
* Dependent variable $Y_i$
* Error terms $e_i$, which aren't directly observed in data

**Goal of regression**: estimate $f(X_i, \beta)$ which most closely fits the data

**Steps of regression analysis**:
* Step 1: the form of $f$ must be specified
    * Option 1: based on knowledge about $Y_i$ and $X_i$ and doesn't rely on the data
    * Option 2: without prior knowledge, a flexible or convenient form of $f$ is chosen (e.g. linear regression)
* Step 2: perform regression techniques
    * Least squares method (most widely use): find $\hat{\beta}$ which minimizes $\sum_i [Y_i - f(X_i, \beta)]^2$
        * Formal: $\hat{\beta} = \arg \min_{\beta} \sum_i [Y_i - f(X_i, \beta)]^2$
        * Why most widely used: $f(X_i, \hat{\beta})$ approximates $E(Y_i|X_i)$ 
* Step 3: inference with regression model:
    * Use the fitted value $\hat{Y}_i = f(X_i, \hat{\beta})$ for prediction
    * Use the fitted value $\hat{Y}_i = f(X_i, \hat{\beta})$ to access the accuracy of the model in explaining the data

**Notices to least squares**:
* There must be sufficient data to estimate a regression model
    * Explain: the number of equations must be at least the number of variables
    * Degrees of freedom: $\text{n_data_points} - \text{n_params}$
* The independent variables $(X_{1i}, X_{2i}, ..., X_{ki})$ must be linearly independent

## Underlying assumptions
**Underlying assumptions of regression analysis**:
* The sample is representative of the population at large
* The independent variables are measured with no error
* Assumptions on the noise term $e_i$:
    * The expected noise is zero (white noise) $E(e_i|X_i) = 0$
    * The variance of $e_i$ is constant across observations
    * The errors $e_i$ are uncorrelated with one another

## Interpolation and extrapolation
**Prediction with regression models**: regression models predict a value of $Y$ given known values of $X$
* Interpolation: prediction within the range of values in the training dataset
* Extrapolation: prediction outside the range of values in the training dataset

**Tricks for performing extrapolation**: attach the estimated value $\hat{Y}_i$ with a prediction interval which represents the uncertainty

>**NOTE**: the prediction interval should expand rapidly as the values of the independent variables moved outside the range covered by the observed data

## Power and sample size calculation
**Rule of thumb**: $N = m^n$
* $N$ is the sample size
* $n$ is the number of independent variables
* $m$ is the number of observations needed to reach the desired precision, if the model had only one independent variable