<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Maximum entropy classifier](#maximum-entropy-classifier)
- [BONUS](#bonus)
- [NEW WORD](#new-word)
<!-- /TOC -->

# Maximum entropy classifier
**Introduction**:
* Definition: a classification method that generalizes logistic regression to multi-class problems
    * Input: a set of independent variables
    * Output: a categorically distributed dependent variable
* Other names:
    * Multinomial logistic regression
    * Softmax regression
    * Conditional maximum entropy model
* Idea: use a linear combination of the observed features and some problem-specific parameters to estimate the probability of each particular value of the dependent variable

**Independence of irrelevant alternatives (IIA)**:
* Other names: "binary independence" or "independence axiom"
* Definition:
    * Definition 1 (social choice theory): the social preferences between alternatives x and y depend only on the individual preferences between x and y
    * Definition 2: if $A$ is preferred to $B$ out of the choice set $\{A,B\}$, introducing a third option $X$, expanding the choice set to $\{A,B,X\}$, must not make $B$ preferable to $A$
        * Explain: preferences for $A$ or $B$ should not be changed by the inclusion of $X$, (i.e. $X$ is irrelevant to the choice between $A$ and $B$)
* Example: the relative probabilities of taking a car or bus to work don't change if a bicycle is added as an additional probability
* IIA and its effects on multinomial classifiers:
    * IIA assumption in multinomial logit: $\frac{\text{Pr}(X_i \in C_j)}{\text{Pr}(X_i \in C_k)} = \frac{\exp(\beta_j X_i)}{\exp(\beta_k X_i)}$
        * $X_i \in C_j$ indicates that example $i$ belongs to class $j$
    * Effect: IIA allows the choice of $K$ alternatives to be modeled as a set of $K-1$ independent binary choices
        * Explain: one alternative is chosen as a "pivot" and other $K-1$ compared against it, one at a time
    * Consequence: when multinomial logit is used to model choices, it may, in some cases, impose too much constraint on the relative preferences between the different alternatives
    
    $\hspace{1.0cm} \rightarrow$ This point is especially important to take into account if the analysis aims to predict how choices would change if one alternative was to disappear

**Assumptions**:
* Case-specific data: each independent variable has a single value for each case
* Imperfect prediction: the dependent variable cannot be perfectly predicted from the independent variables for any case
* Low collinearity: 
    * The independent variables needn't to be statistically independent from each other
    * Collinearity is assumed to be relatively low
        * Explain: it's difficult to differentiate between the impact of several variables if it's not the case
* Independence of irrelevant alternatives (IIA) is assumed

>**NOTE**: this assumption isn't always desirable

**Idea**: as in many other statistical classification techniques, we want to construct a linear predictor function that constructs a score from a set of weights that are linearly combined with the features using a dot product
* Formal: $\text{score}(\textbf{X}_i, k) = \beta_k \cdot \textbf{X}_i$
    * $\textbf{X}_i$ is the vector of features describing observation $i$
    * $\beta_k$ is a vector of weights (i.e. regression coefficients) correspond to outcome $k$
    * $\text{score}(\textbf{X}_i, k)$ is the score associated with assigining observation $i$ to category $k$
    
    >**NOTE**: in discrete choice theory, $\text{score}(\textbf{X}_i, k)$ is seen as the utility associated with person $i$ choosing outcome $k$
    
* Final prediction: the one with the highest score
* Advantage of multinomial logistic model over other methods (e.g. SVM, LDA, etc.): the score in multinomial logit model can be directly converted to a probability value
    * Consequence: we can incorporating the prediction of a particular multinomial logit model into a larger procedure involving multiple predictions (each with a possibility of error)
        * Effect: without combing predictions, errors tend to multiply
            * Explain: if we make a single optimal prediction (e.g. one-vs-rest SVM) instead of predict probabilities of each possible outcome
            
            $\hspace{1.0cm} \rightarrow$ The error will be propagated
        * Example: consider a predictive model as below
            * Architecture: 
                *A predictive model is broken down into a series of sub-models
                * The prediction of a given sub-model is used as the input of another sub-model
            * Observations: if each sub-model as 90% accuracy in its prediction and there are 5 models in the series
            
            $\hspace{1.0cm} \rightarrow$ The overall accuracy is $0.9^5 = 59%$
    * Error propagation: the issue that the error is multiplied
        * Error propagation in practice: a series problem in real-world predictive models, which are composed of numerous parts

**Multinomial logistic classifier as linear predictor**: $f(k, i) = \beta_k \textbf{x}_i$
* $f(k, i)$ is the estimation of the probability that observation $i$ has outcome $k$
* $\beta_k$ is the set of regression coefficients associated with outcome $k$
* $\textbf{x}_i$ (a row vector) is the set of features associated with observation $i$

**Multinomial logistic classifier as independent binary regressions**:
* Assumptions:
    * The number of possible outcomes is $K$
* Procedure: 
    * Step 1: choose one outcome as a "pivot" and the other $K-1$ outcomes are separately regressed against the pivot outcome
        * Formal (example): outcome $K$ (the last outcome) is chosen as the pivot
    * Step 2: run $K-1$ independent binary logistic regression models
        * Formal: $\ln \frac{\text{Pr}(Y_i = j)}{\text{Pr}(Y_i = K)} = \beta_j \textbf{X}_i$ $\forall j \in [1, K-1]$
* Observations:
    * $\ln \frac{\text{Pr}(Y_i = j)}{\text{Pr}(Y_i = K)} = \beta_j \textbf{X}_i$
    
    $\hspace{1.0cm} \leftrightarrow \text{Pr}(Y_i = j) = \text{Pr}(Y_i = K) \exp(\beta_j \textbf{X}_i)$
    * $\text{Pr}(Y_i = K) = 1 - \sum_{j = 1}^{K-1} \text{Pr}(Y_i = j)$
    
    $\hspace{1.0cm} \leftrightarrow \text{Pr}(Y_i = K) = \frac{1}{1 + \sum_{i = 1}^{K-1} \exp(\beta_j \textbf{X}_i)}$
    * From above, $\text{Pr}(Y_i = j) = \frac{\exp(\beta_j \textbf{X}_i)}{1 + \sum_{i = 1}^{K-1} \exp(\beta_j \textbf{X}_i)}$ $\forall j \in [1, K-1]$

**Multinomial logistic classifier as log-linear model**: 
* Idea: model $\text{Pr}(Y_i = j)$ as $\ln \text{Pr}(Y_i = j) = \beta_j \cdot \textbf{X}_i - \ln Z$ $\forall j \in [1, K]$
    * $\ln Z$ as extra term to ensure that the whole set of probabilities forms a probability distribution
* Partition function for the distribution: $Z$
* Observations:
    * $\text{Pr}(Y_i = j)$ as $\ln \text{Pr}(Y_i = j) = \beta_j \cdot \textbf{X}_i - \ln Z$
    
    $\hspace{1.0cm} \leftrightarrow \text{Pr}(Y_i = j) = \frac{\exp(\beta_j \textbf{X}_i)}{Z}$
    * $\sum_j \text{Pr}(Y_i = j) = 1$
    
    $\hspace{1.0cm} \rightarrow Z = \sum_{j = 1}^K \exp(\beta_j \textbf{X}_i)$
* Log-linear model and independent binary regressions:
    * Observations:
        * If we add a constant $C$ to every coefficient $\beta_j$
        
        $\hspace{1.0cm} \rightarrow \text{Pr}(Y_i = j)$ remains the same
        * From above, if we add $C = - \beta_K$ to every $\beta_j$
        
        $\hspace{1.0cm} \rightarrow$ Log-linear model becomes independent binary regressions
    * Conclusion: log-linear model and independent binary regressions are equivalent

---

# BONUS
* "Nomial" (statistics) is equivalent to "categorical"
* Softmax function: $\text{softmax}(k, x_1, ..., x_n) = \frac{\exp(x_k)}{\sum_{i = 1}^n \exp(x_i)}$
    * "Softmax": "softmax" doesn't mean "soft-max", it means "soft-argmax"
        * Explain: "softmax" is a smooth approximation of the argmax function where "argmax" is defined as $\arg \max(z_1, ..., z_n) = (0, ..., 0, 1, 0, ..., 0)$
        * Consequence: "softmax" is used to estimate the one-hot vector which indicates the label of an example
    * The effect of exponentiating $x_1, ..., x_n$: exaggerate the difference between $x_1, ..., x_n$
        * $\text{softmax}(k, x_1, ..., x_n) \to 0$ if $x_k$ is significantly less than $\max_i x_i$
        * $\text{softmax}(k, x_1, ..., x_n) \to 1$ if $x_k$ is close to $\max_i x_i$

# NEW WORD
* Exaggerate (v): phóng đại