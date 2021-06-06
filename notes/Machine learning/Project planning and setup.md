---
title: Project planning and setup
tags: Machine learning
---

**Source**. https://www.youtube.com/watch?v=tBUK1_cHu-8

[toc]

### Life cycle of a machine learning project

<div style="text-align:center">
    <img src="/media/lVKdqIX.png">
    <figcaption>Per-project activities</figcaption>
</div>

**Per-project activities**
1. *Planning and project setup*.
    * Determine the problem of interest
    * Determine project goals
    * Determine project requirements, i.e. what we need and what we have
2. *Data collection and labeling*.
    * Define which type of data we need
    * Determine the data acquisition procedure
    * Determine the data annotation procedure
3. *Training and debugging*.
    * Implement a simple baseline, e.g. OpenCV
    * Survey and find SoTA model, then try to reproduce on public datasets
    * Debug our implementation
    * Improve model for our task
4. *Deploying and testing*.
    * Deploy our model in a controlled setting, e.g. lab environment
    * Write tests to prevent regressions
    * Deploy in production (if sufficiently good)

>**NOTE**. During the life cycle of a machine learning project, if we are stuck at some step, we may want to go back to previous steps rather than moving towards

**Potential problems**.
* Data acquisition and annotation is too costly
    * *Solution*. Revisit step 1
* The task of interest is infeasible, i.e. cannot be solved
    * *Solution*. Revisit step 1
* Our model works well on training and validation sets but fails in real world environment
    * *Solution*. Revisit training and data collection, i.e. step 2 and 3
        * Fix data mismatch between training data and real world data
        * Collect more data
        * Mine hard cases for training
* Our evaluation metrics does not reflect our objectives
    * *Solution*. Revisit our assumptions, i.e. step 1

**Other concerns**.
* Understand the SoTA in your domain, i.e.
    * Understand what is possible
    * Know what to try next

**Cross-project infrastructure**.
* *Team and hiring*
* *Infrastructure and tooling*

### Planning and project setup
#### Prioritizing projects and choosing goals

<div style="text-align:center">
    <img src="/media/GyqJfrZ.png">
    <figcaption>A general framework for prioritizing projects</figcaption>
</div>

**Aspects deciding the importance of a project**
* *Impact*. High-impact machine learning problems.
    * Automate complex parts of some pipeline
    * Places where cheap prediction is valuable
* *Feasibility*. Cost of machine learning projects. 
    * Mainly driven by data availability
    * Accuracy requirements play the second main role

**High-impact machine learning projects**. 
* Where we can take advantage of cheap prediction
    * *Cheap prediction*. Prediction can be made everywhere
    * *Explain*.
        * AI reduces cost of prediction
        * Prediction is central for decision making
* Where we can automate complicated manual software pipelines

<div style="text-align:center">
    <img src="/media/YT8y4Wx.png">
    <figcaption>Accuracy and project cost</figcaption>
</div>

**Cost drivers of machine learning projects**. (sorted by difficulty)
1. *Data availability*, i.e. data acquisition, annotation, and sample size
2. *Accuracy requirement*, i.e. cost of wrong predictions, how frequent the system must work well, etc.
3. *Problem difficulty*, i.e. existing solutions, resources for training and deployment, etc.

#### Choosing metrics

**Key points for choosing a metric**. We need to pick a formula for combining metrics 
* *Explain*. 
   * The real world is very complex, thus we usually care about lots of metric
   * Machine learning systems work best when optimizing a single number

>**NOTE**. The evaluation metric can and will change throughout the project

**Combining evaluation metrics**.
* Average / weighted sum of metrics, e.g. F1 score
* Threshold $n-1$ metrics and evaluate the $n$th metric
    * *Choose metrics to threshold*.
        * Based on domain judgement
        * Choose metrics which are least sensitive to model choice
        * Choose metrics which are closest to desirable values
    * *Choose threshold values*.
        * Based on domain judgement
        * Based on baseline model's performance
        * Based on the importance of the metric, at the time of evaluation
* More complex / domain-specific formula

**Evaluation process**.
1. Enumerate requirements, i.e. to choose appropriate metrics
2. Evaluate current performance, i.e. how well we are doing
3. Compare current performance to requirements, i.e. choose which metric to optimize
4. Revisit metric as our performance improve

#### Chossing baselines

**Purposes**. Baselines give us a lower bound on expected model performance

>**NOTE**. The tighter the lower bound, the more useful the baseline

**Finding good baselines**.
* *External baselines*
   * Business / engineering requirements
   * Published results (make sure the comparison is fair)
* *Internal baselines*
    * Scripted baselines, e.g. OpenCV, rule-based method, etc.
    * Simple machine learning baselines

**Creating good human baselines**.

<div style="text-align:center">
    <img src="/media/0yPlj1N.png">
    <figcaption>Cost of creating human baselines</figcaption>
</div>



###  Discussions
* Do not evaluate your model ont test set frequently, otherwise it may lead to overfitting
* Should we do fine-tuning? If the dataset is similar to our desired dataset and our data is limited then we should do that 
* Data size for deep learning
    * Deep learning system hardly works well with less tham 10,000 examples
    * Vision systems start working well with hundreds of thousands of examples
* Product design can reduce the need of accurac