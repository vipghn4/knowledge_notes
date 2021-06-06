---
title: Testing and deployment
tags: Full stack deep learning
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Testing and deployment](#testing-and-deployment)
  * [Project structure](#project-structure)
  * [Machine learning test code](#machine-learning-test-code)
  * [CI and testing](#ci-and-testing)
  * [Monitoring](#monitoring)
* [Appendix](#appendix)
  * [Questions](#questions)
<!-- /TOC -->

# Testing and deployment
## Project structure

<div style="text-align:center">
    <img src="/media/LGKTQzd.png">
    <figcaption>Project structure for testing and deployment</figcaption>
</div>

**Training system**. Generate the prediction system
* *Purpose*.
    * Process raw data
    * Run experiments
    * Manage the results
* *Data*. Training and validation data

**Prediction system**. The model that makes prediction
* *Purpose*.
    * Process input data
    * Construct networks with trained weights
    * Make predictions
    * Postprocess output
* *Data*. Validation data

**Serving system**.
* *Purpose*
    * Serve predictions
    * Scale to demand
* *Data*. Production data

**Functionality tests**. Test the functionality of prediction system
* *Purpose*.
    * Test prediction system on a few important examples
    * Run in less than 5 minutes (during development)
    * Catch code regressions
* *Data*. Raw data that the system will actually see in production

**Validation tests**. Test the prediction on a larger validation set
* *Purpose*.
    * Run in less than 1 hour (every code push)
    * Catch model regressions
* *Data*. Processed data

**Training system tests**. Test the full pipeline
* *Purpose*.
    * Test full training pipeline
    * Run in less than 1 day (nightly)
* *Data*. Raw data

**Monitoring**.
* Alert to down-time, errors, distribution shifts, etc.
* Catch service and data regression

## Machine learning test code

<div style="text-align:center">
    <img src="/media/VvWiKk7.png">
    <figcaption>Traditional software</figcaption>
</div>

<div style="text-align:center">
    <img src="/media/p6tolVh.png">
    <figcaption>Machine learning software</figcaption>
</div>

**Data test**.
* Feature expections are captured in a schema
* All features are beneficial
* No feature's cost is too much
* Feature adhere to meta-level requirements
    * *Explain*. There is some business reason to have a specific feature, and we have to obey that
* The data pipeline has appropriate privacy controls
    * *Explain*. To make sure that no sensitive data is leaked
* New features can be added quickly
* All input feature code is tested

**Model tests**.
* Model specs are reviewed and submitted
* Offline and online metrics correlate
* All hyperparameters have been tuned
* The impact of model staleness is known
* A simpler model is not better
* Model quality is sufficient on important data slices
* The model is tested for considerations of inclusion

**ML infrastructure tests**.
* Training is reproducible
* Model specs are unit tested
* The ML pipeline is integration tested
* Model quality is validated before serving
* The model is debuggable
* Models are canaried before serving
* Serving models can be rolled back

**Monitoring tests**.
* Dependency changes result in notification
* Data invariants hold for inputs
* Training and serving are not skewed
* Models are not too stale
* Models are numerically stable
* Computing performance has not regressed
* Prediction quality has not regressed

**Scoring the test**.

<div style="text-align:center">
    <img src="/media/mYveFPD.png">
    <figcaption>Average testing results at Google</figcaption>
</div>

| Points | Description |
| --- | --- |
| 0 | More of a research project than a productionized system |
| (0, 1] | Not totally untested, but it is worth considering the possibility of serious holes in reliability |
| (1, 2] | There has been first pass at basic productionization, but additional investment may be needed |
| (2, 3] | Reasonably tested, but it is possible that more of those tests and procedures may be automated |
| (3, 5] | Strong levels of automated testing and monitoring, appropriate for mission-critical systems |
| > 5 | Exceptional levels of automated testing and monitoring |

## CI and testing
**Types of tests**.
* *Unit / integration tests*.
    * *Unit test*. Test for individual module functionality
    * *Integration tests*. Test for the whole system, and the public interface of our system
* *Continuous integration*. Tests are run everytime new code is pushed to the repository, before updated model is deployed

**Containerization via Docker**. A self-enclosed environment for running the tests

**SaaS for CI**. CircleCI, Travis, Jenkins, Buildkite
* *CircleCI*.
    * Every push kicks off a cloud job, which can be defined as commands in a Docker container
    * Job results can be stored for later review
    * No GPU is available
    * Circle CI has a free plan for solo practitioner
* *Jenkins and Buildkite*.
    * Nice option for running CI on our own hardware, in the cloud, or mixed
    * Good option for a scheduled training test
    * Very flexible

## Monitoring
**Monitoring**. Have a monitoring software running around our system
* *Purpose*. Alarm for when things go wrong, and records for tuning things
    * *Example*.
        * If our machine learnind model predicts wrong results too frequently
        * If the data is skewed or not

>**NOTE**. Anything which can be logged can be monitored, e.g. data skew

>**NOTE**. It is important to log data coming to our system

**Data distribution monitoring**. There is no actual automatical way to do this
* *Tools*. Domino data lab

**Closing the flywheel**.
* Important to monitor the business uses of the model, not just its own statistics, e.g. how users interact with the system
* Important to be able to contribute failures back to training dataset
    * *Example*. Compare expectation of human user with our model
*

# Appendix
## Questions
>**NOTE**. For different systems, e.g. training system, prediction sytem, etc. should be within one repo onl
