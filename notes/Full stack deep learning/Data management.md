---
title: Data management
tags: Full stack deep learning
---

# Table of Contents
[toc]

# Sources
**Motivation**.
* Semi-supervised learning, self-supervised learning, etc. are not practical enough to put in production now

    $\to$ Focus on labeling data, rather than puting interesting models in production
* If we use publicly available datasets, then we have no competitive advantage
* We usually have to spend tons of dollars and time to label our own data

**Data flywheel**. Enable rapid improvement with user labels
* *Motivation*. Top tier companies have much more data than us, thus our models cannot be as accurate as their models

    $\to$ If we wait until our models until it is as accurate as their ones, then we will never ship product
* *Solution*. 
    1. Ship a model, which is not quite good, but at least has high precision and low recall
    2. Use data flywheel to collect user labels, e.g. capcha

**Semi-supervised learning**. Use parts of data to label other parts
* *Usage*. When we have a lot of unlabeled data

**Data augmentation**. Crucial and must-do thing, especially for computer vision

>**NOTE**. Hook augmentation step in our `torch.utils.data.Dataset` to do in CPU workers in parallel to GPU training

* *Tools*. albumentations, fast.ai, etc.

**Synthetic data**. Under-rated idea that is almost always worth starting with

>**NOTE**. Experiments show that synthetic data works, but if we want to achieve good accuracy, we still need labeled data

* *Usage*. OCR, self-driving cars, robotics, etc.

**Related fields**. Few-shot learning

# Data labeling
## User interfaces
**Standard set of features for labeling computer vision tasks**. Bounding boxes, segmentations, keypoints, cuboids (3D data), set of applicable classes

**Training annotators**. This is a crucial part of the annotation phase
* *Writing good instructions for annotators*.
    * Include all rules and examples of right and wrong annotations according to each rule
    * Include all annotation edge cases in the labeling instruction
* *Quality assurance*. Quality assurance is key
    * *Quality assureance tasks*.
        * Assure the progress meets the deadlines
        * Assure that the output labels are good

## Sources of labor
**Approach 1**. Hire our own annotators, and promote the best ones to quality control, and have them train other ones
* *Pros*. Secure, fast (once hired), less QC required
* *Cons*. Expensive, slow to scale, admin overhead

**Approach 2**. Crowdsource, e.g. capcha
* *Pros*. Cheaper, more scalable
* *Cons*. Not secure, significant QC effort required

**Approach 3**. Full-service data labeling companies
* *Pros*. No need to train annotators, QC, etc.
* *Cons*. Expensive

## Service companies
**Motivation**. Data labeling requires separate software stack, temporary labor, and quality assureance

$\to$ It makes sense to outsource this 

**Choosing service companies**. We should dedicate several days to selecting the best service companies for labeling our data
1. Label gold standard data by ourself
2. Hand the gold standard data (without labels) to different contenders
3. Ask the contenders to work on the sample data
4. Compare the contenders' results and our results, and choose the best one with good pricing

**Recomended tools**.
* *Top tier service companies*. Scale.ai
* *Labeling software*. CVAT, Prodigy, etc.

**Conclusion**.
* Outsource to full-service company if we can afford it
* Otherwise, at least use existing software for labeling
* Hiring part-time labors makes more sense than trying to make crowdsourcing work
    * *Explain*. Due to extra complexity when working with crowdsourcing

# Storage
## Building blocks of data storage
**File system**. Foundation layer of storage
* *Fundamental unit*. A file, which can be text or binary, is not versioned, and is easily overwritten
* *Types of file systems*. 
    * *Local file system*. A hard disk containing all the files we need
    * *Remote file system*. A remote server, which is accessible over network by multiple machines
    * *Distributed file system*. Data is stored and accessed over multiple machines
* *Access pattern*. Should be fast and parallel (trade-off)

**Object storage**. An API over the file system, which provides GET, PUT, DELETE requests to modify files in the file system, without worrying where they are actually stored
* *Fundamental unit*. Object, e.g. image, sound file, etc.
* *Versioning*. When we modify an existing file, the API will treat the uploaded file as a new version of that file to the storage, rather than deleting the existing file
* *Redundancy*. When we upload a file, it will be stored in multiple storages
* *Example*. Amazon S3, Ceph

**Database**. Persistent, fast, scalable storage and retrieval of structured data
* *Mental model*. Everything is actually in RAM, but software ensures that everything is logged to disk and never lost
* *Usage*. Store references to our actualy data, rather than storing the binary files
* *Example*. Rather than storing images, we store a DB of metadata of images

    $\to$ We only need to download what we need
* *Tools*. Postgres is the right choice for more than 90% of the time
    * *Explain*. Postgres is flexible enough for NoSQL applications

**Data lake**. An aggregation of data from multiple sources, e.g. databases, logs, expensive data transformations, etc.

<div style="text-align:center">
    <img src="/media/pF6G0Me.png">
    <figcaption>Data lake illustration</figcaption>
</div>

* *Schema on read*. Dump everything in, then transform for specific needs later
* *Industry standard for data lake*. Amazon Redshift, Snowflake

**Feature store**. Transform raw data into features first, then store the features in the feature store

>**NOTE**. It is more practical to use data lake, rather than feature store

## What goes where
**What goes where**.
* *Binary data (images, sound files, etc.)*. Stored as objects, not necessarily as a file in a file system
    * *Example*. Objects allow versioning, parallel accessing
* *Metadata (labels, user activities, etc.)*. Stored in database
* *Features which are not obtainable from database (logs)*. Set up data lake and a proces to aggregate required data

**Data usage**. At training time, copy the required data onto file system (local or networked) 

**References**. Designing data-intensive applications (book)

# Versioning
**Levels of versioning**.
* *Level 0*. Unversioned
* *Level 1*. Versioned data via snapshot at training time
* *Level 2*. Versioned as a mix of assets and code
* *Level 3*. Specialized data versioning solution

## Level 0
**Problem**. Deployments must be versioned

$\to$ Models should be versioned
* *Model versioning*. Deployed machine learning models are part code, part data

$\to$ If data is not versioned, deployed models are not versioned
* *Consequence*. Inability to get back to a previous level of performance

## Level 1
**Description**. Everytime we train, we store a snapshot of everything at training time

$\to$ We can version deployed models, and get back to past performance, but this solution is super hacky

**Consequence**. It would be much better to version data just as easily as code

## Level 2
**Description**. Data is versioned as a mix of assets and code
* *Examples*.
    * Heavy files stored in some storage system, with unique IDs
    * Training data is stored as JSON or similar, referring to these IDs and include relevant metadata, e.g. labels, etc.
* *Consequence*. JSON files can get big, but using git-lfs lets us store them as easily as code

    >**NOTE**. We can use lazydata, i.e. only syncing files which are required

## Level 3
**Description**. Use specialized solutions for versioning data

>**NOTE**. Avoid this until we can explain how they will improve our project

* *Leading solutions*. DVC, Pachyderm, Quill, DoIt

# Appendix
## Discussions
**Comments from experts**.
* One of the biggest failure I see in junior ML/CV engineers is a complete lack of interest in building data sets. While it is boring grunt work I think there is so much to be learned in putting together a dataset. It is like half the problem
* As a data scientist in 2019, I spend most of (60%+) my time cleaning and moving data, i.e.
    * 6% people asked said that they spend most of their time picking features and models
    * 67% people asked said that they spend most of their time cleaning and moving data
    * 4% people asked said that they spend most of their time deplying models in production
    * 23% people asked said that they spend most of their time analyzing and presenting data
* For my last few ML projects, the complexity has not been in the modeling and training, it has been in input preprocessing. Find myself running out of CPU more than GPU and in one project I am actually unsure how to optimize the python further

**Questions**.
* *What is the decent amount of data to start with*. Depend on the difficulty of the problem, but the required amount of data is pretty small
    * *Tricks*.
        1. Start from a pretrained network on large datasets, e.g. ImageNet
        2. Transfer to pretrained model to the target problem
* *How to deal with very unbalanced datasets*. 
    * Use class weights, e.g. based on frequency
    * Use focal loss
    * Start with the whole dataset, train and evaluate dataset, put wrong predicted examples into the train dataset, or increase the weights of wrongly predicted examples, then retrain again
* *In case we cannot afford QC, how to make models more robust to outliers and bad samples*. It is hard to say the model is robust against certain parts of the data distribution if we do not have that distribution as part of our dataset

    $\to$ The only way to tell is have a validation dataset
* *How to ensemble data labels*. Depend on the problem we are working on
    * *Suggested solution*. Rank labels based on the performance of the annotators

**Using public datasets in production**.
1. Start building the product with public datasets and deploy something
2. Gather user data to finetune the model